import new

import requests


class BaseAPI(object):
    """
    Extend to store contants about your api such as api key,
    version, base url.
    """
    def __init__(self, base_url="http://example.com/"):
        self.base_url = base_url
        raise NotImplemented

    def _update_parameters(self, params):
        """
        Modify parameters with api contants like api keys.
        These parameters can override user provided parameters.
        """
        return params

    def _get_base_url(self):
        """
        Modify how the base_url gets built up and returned
        """
        if not self.base_url.endswith("/"):
            self.base_url = self.base_url + "/"
        return self.base_url

    def _process_json(self, data):
        """
        data is python data structure from json, sometime they need to be
        unwraped like a data or d key deferenced.
        """
        return data

    def _process_content(self, data):
        """
        data is basically text, what even is returned by requests
        response.content. This is chance to munge it.
        """
        return data

    @classmethod
    def _register(cls, api_call, name=None):
        """
        Bind the APIFunction class as a method.
        """
        method = new.instancemethod(api_call, None, cls)
        if not name: name = api_call.__name__
        setattr(cls, name, api_call)


class APIFunction(object):
    """
    Class that will represent the callable method of the API
    """
    path = None
    method = "GET"
    # name for positional arguments. If more arguments are provided then there are names they are ignored.
    arg_names = []

    def __init__(self, api, args, kwargs):
        self.api = api
        self.args = args
        self.kwargs = kwargs

        self.r = None

        # clean the path specification
        if self.path.startswith("/"): self.path = self.path[1:]

    def execute(self):
        if self.method is None:
            raise NotImplementedError(u'Subclass of APIFunction needs to '
                                      u'define a valid "method" attribute.')

        self.r = self._execute()

        json_data = self.r.json()
        if json_data is not None:
            return self.api._process_json(json_data)

        return self.api._process_content(self.r.content)

    def get_path(self, kwargs=None):
        return self.path

    def _get_parameters(self):
        params = self.kwargs

        if len(self.arg_names) > len(self.args):
            raise TypeError("%s requires %s arguments (%s given)" % (self.__class__.__name__,
                                                                     len(self.arg_names),
                                                                     len(self.args)))

        for name, arg in zip(self.arg_names, self.args):
            params[name] = str(arg)

        params = self.api._update_parameters(params)

        return params

    def _get_kwargs(self):
        kwargs = {}
        if self.method.lower() == "get":
            kwargs['params'] = self._get_parameters()
        else:
            kwargs['data'] = self._get_parameters()

        return kwargs

    def _execute(self):
        request_method = getattr(requests, self.method.lower())
        kwargs = self._get_kwargs()
        url = self.api._get_base_url() + self.get_path(kwargs)
        return request_method(url, **kwargs)


def binder(function_class):
    closed = function_class

    def _bound(api, *args, **kwargs):
        func = closed(api, args, kwargs)
        return func.execute()
    _bound.__name__ = function_class.__name__
    return _bound


def get_bind(api_cls):
    def bind(cls):
        """
        This decorator could probably be replace with a meta class?
        """
        api_cls._register(binder(cls))
        return cls

    return bind
