# coding: utf-8

from collections import UserDict, UserList
from functools import partial
from pydantic import TypeAdapter
import time
from typing import Any
from urllib.parse import urlparse

from cyperf import LinkNameException
from cyperf import ApiClient
from cyperf import ApiException
import cyperf.models

class DynamicList(UserList):
    def __init__(self, lst: any = None, api_client : ApiClient = None):
        super().__init__(lst)
        if isinstance(lst, DynamicList):
            self.data = lst.data
            self.dyn_data = lst.dyn_data
            self.api_client = lst.api_client
        else:
            self.data = lst
            self.dyn_data = [DynamicModel.dynamic_wrapper(i, api_client) for i in lst] if lst else []
        if api_client:
            self.api_client = api_client

    def __contains__(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return item in self.data

    def __getitem__(self, i):
        if isinstance(i, slice):
            con = self.data[i]
            dyn_con = self.dyn_data[i]
            other = DynamicList()
            other.data = con
            other.dyn_data = dyn_con
            other.api_client = self.api_client
            return other
        else:
            return self.dyn_data[i]

    def __setitem__(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data[i] = item.base_model
            self.dyn_data[i] = item
        else:
            self.data[i] = item
            self.dyn_data[i] = DynamicModel.dynamic_wrapper(item, self.api_client)

    def append(self, item):
        if isinstance(item.__class__, DynamicModel):
            self.data.append(item.base_model)
            self.dyn_data.append(item)
        else:
            self.data.append(item)
            self.dyn_data.append(DynamicModel.dynamic_wrapper(item, self.api_client))

    def insert(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data.insert(i, item.base_model)
            self.dyn_data.insert(i, item)
        else:
            self.data.insert(i, item)
            self.dyn_data.insert(i, DynamicModel.dynamic_wrapper(item, self.api_client))

    def pop(self, i=-1):
        self.data.pop(i)
        return self.dyn_data.pop(i)

    def remove(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        self.data.remove(item)

    def count(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return self.data.count(item)


    def index(self, item, *args):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return self.data.index(item, *args)

    def extend(self, other):
        if isinstance(other, DynamicList):
            self.data.extend(other.data)
            self.dyn_data.extend(other.dyn_data)
        else:
            self.data.extend([item.base_model if isinstance(item.__class__, DynamicModel) else item for item in other])
            self.dyn_data.extend([DynamicModel.dynamic_wrapper(item, self.api_client) if not isinstance(item.__class__, DynamicModel) else item for item in other])

class DynamicDict(UserDict):
    def __init__(self, dct: any = None, api_client : ApiClient = None):
        super().__init__(dct)
        if isinstance(dct, DynamicDict):
            self.data = dct.data
            self.dyn_data = dct.dyn_data
            self.api_client = dct.api_client
        else:
            self.data = dct
            self.dyn_data = {key:DynamicModel.dynamic_wrapper(i, api_client) for key,i in dct}
        if api_client:
            self.api_client = api_client

    def __contains__(self, item):
        if isinstance(item.__class__, DynamicModel):
            item = item.base_model
        return item in self.data

    def __getitem__(self, i):
        if isinstance(i, slice):
            con = self.data[i]
            dyn_con = self.dyn_data[i]
            other = DynamicList()
            other.data = con
            other.dyn_con = dyn_con
            other.api_client = self.api_client
        else:
            return self.dyn_data[i]

    def __setitem__(self, i, item):
        if isinstance(item.__class__, DynamicModel):
            self.data[i] = item.base_model
            self.dyn_data[i] = item
        else:
            self.data[i] = item
            self.dyn_data[i] = DynamicModel.dynamic_wrapper(item, self.api_client)

class DynamicModel(type):
    def __new__(cls, name, bases, dct):
        try:
            inner_model = getattr(cyperf.models, name)
        except AttributeError:
            raise Exception(f"Couldn't find model class {name}")
        local_fields = {}
        fields = []
        try:
            fields = inner_model.__fields__
        except AttributeError as e:
            pass
        for key in fields:
            dct[key] = property(fget=partial(cls.get_by_link, key), fset=partial(cls.set_base_attr, key))
            local_fields[key] = None
        dct['_model_fields'] = local_fields
        dct['__init__'] = lambda self, base_model: cls.init(self, base_model)
        if name == "AsyncContext":
           dct['await_completion'] = lambda self, get_final_result = True, poll_time = 1: cls.poll(self, get_final_result = get_final_result, poll_time = poll_time)
        c =  super().__new__(cls, name, bases, dct)
        c.update = lambda self: cls.update(self)
        c.refresh = lambda self: cls.refresh(self)
        c.link_based_request = lambda self, link_name, method, return_type = None, body = None, query=[]: cls.link_based_request(self, link_name, method, return_type, body, query)
        return c

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj._local_fields = {}
        for field in cls._model_fields:
            obj._local_fields[field] = None
        obj.api_client = None
        return obj

    @classmethod
    def init(cls, self, base_model):
        self.base_model = base_model

    @classmethod
    def dynamic_wrapper(cls, obj: any, api_client: ApiClient = None):
        if isinstance(obj, list):
            l = DynamicList(obj, api_client)
            for i in l:
                if isinstance(i.__class__, DynamicModel) and i.links:
                    i.refresh()
            return l
        if isinstance(obj, dict):
            d = {key:cls.dynamic_wrapper(obj[key], api_client) for key in obj}
            for k in d:
                if isinstance(d[k].__class__, DynamicModel) and d[k].links:
                    d[k].refresh()
            return d
        else:
            import cyperf.dynamic_models
            try:
                dyn_class = getattr(cyperf.dynamic_models, obj.__class__.__name__)
            except AttributeError:
                return obj
            dyn_obj = dyn_class(obj)
            dyn_obj.api_client = api_client
            return dyn_obj


    @classmethod
    def get_by_link(cls, key, self):
        if self._local_fields[key] != None:
           return self._local_fields[key]
        if key == 'links':
            self._local_fields[key] = self.base_model.links
            return self._local_fields[key]
        field = getattr(self.base_model, key)
        if field is None:
            field_info = self.base_model.__class__.__fields__[key]
            try:
                field = self.link_based_request(field_info.alias, "GET", return_type=field_info.annotation)
            except LinkNameException as e:
                field = self.link_based_request(key, "GET", return_type=field_info.annotation)
        setattr(self.base_model, key, field)
        field = getattr(self.base_model, key)
        self._local_fields[key] = cls.dynamic_wrapper(field, self.api_client)
        return self._local_fields[key]

    @classmethod
    def set_base_attr(cls, key, self, obj):
        self._local_fields[key] = cls.dynamic_wrapper(obj, self.api_client)
        setattr(self.base_model, key, obj)

    @classmethod
    def update(cls, self):
        try:
            d = self.base_model.to_dict()
            del d['links']
            self.link_based_request("self", "PATCH", body=d)
        except ApiException as e:
            if e.status != 405:
                raise e
            full_body = self.link_based_request("self", "GET", return_type=self.base_model.__class__, query=[("include", "all")])
            for field in (field for field in self._local_fields if self._local_fields[field] != None):
                val = self._local_fields[field]
                if isinstance(val.__class__, DynamicModel):
                    val = val.base_model
                setattr(full_body, field, val)
            self.link_based_request("self", "PUT", body=full_body)


    @classmethod
    def refresh(cls, self):
        self.base_model = self.link_based_request("self", "GET", return_type=self.base_model.__class__)
        for k in self._local_fields.keys():
            self._local_fields[k] = None
        self._local_fields["links"] = self.base_model.links

    @classmethod
    def poll(cls, self, get_final_result = True, poll_time = 1):
        op = self
        while op.state == "IN_PROGRESS":
            time.sleep(poll_time)
            op = cls.dynamic_wrapper(cls.link_based_request(op, None, "GET", return_type=self.base_model.__class__, href=self.url), api_client = self.api_client)
        if op.state == "ERROR":
            raise Exception(f"Error running operation {op.id} of type {op.type}: {op.message}")
        if op.result_url and get_final_result:
            return cls.link_based_request(op, None, "GET", return_type=Any, href=op.result_url)
        return op.result


    @classmethod
    def link_based_request(cls, self, link_name, method, return_type = None, body = None, query=[], href=""):
        if not href:
            if self.base_model.links == None:
                raise Exception("You must allow links to be present to use automatic retrieval functions.")
            if link_name == 'self':
                self_links = [link for link in self.base_model.links if link.rel == link_name]
            else:
                self_links = [link for link in self.base_model.links if link.rel == "child" and link.name == link_name]
            if len(self_links) == 0:
                raise LinkNameException(f"Missing {link_name} link.")
            href = self_links[0].href

        parsed_url = urlparse(href)
        href = parsed_url.path
        if not query:
            query = parsed_url.query
        _host = None
        _collection_formats: Dict[str, str] = {
        }
        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = query
        _header_params: Dict[str, Optional[str]] = {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None
        if isinstance(body.__class__, DynamicModel):
            body = body.base_model
        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )
        if 'Content-Type' not in _header_params:
            _header_params['Content-Type'] = self.api_client.select_header_content_type(
                [
                    'application/json'
                ]
        )
        _auth_settings: List[str] = [
            'OAuth2',
        ]
        _param = self.api_client.param_serialize(
            method=method,
            resource_path=href,
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=body,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host
        )
        response_data = self.api_client.call_api(
            *_param
        )
        response_data.read()
        if response_data.status > 299:
            ApiException.from_response(http_resp=response_data, body=response_data.data, data=None)
        if return_type != None:
            ta = TypeAdapter(return_type)
            return ta.validate_json(response_data.data)
