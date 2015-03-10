from django.conf.urls import patterns
from django.http import HttpResponse, HttpResponseForbidden
import json
import basicauth


def basic_authenticate_request(username, password, request):
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    user_credentials = basicauth.decode(auth_header) if auth_header \
        else (None, None)
    return user_credentials[0] == username and user_credentials[1] == password


def json_response(list_of_dictionaries):
    return HttpResponse(json.dumps(list_of_dictionaries,
                                   default=str,
                                   sort_keys=True),
                        content_type="application/json")


def forbid_view(view_function):
    def f(*args, **kwargs):
        return HttpResponseForbidden()
    return f


def resource_patterns(resource_root, resource):
        return patterns(
            "",
            (r'^%s/$' % resource_root, resource_view,
             {"resource": resource}, resource_root + "-list"),
            (r'^%s/new/$' % resource_root, resource_view,
             {"resource": resource, "new": True}, resource_root + "-new"),
            (r'^%s/(?P<id>\d+)/$' %
             resource_root, resource_view, {
                 "resource": resource}, resource_root + "-details"),
            (r'^%s/(?P<id>\d+)/(?P<subresource>\w+)/$' %
             resource_root, resource_view, {"resource": resource}))


def resource_view(request, resource=None, id=None, subresource=None,
                  subresource_id=None, new=False):
    return resource[subresource](request, id) if subresource else \
        resource["index"](request) if (request.method == "GET" and
                                       not id and
                                       resource.get("index")) else \
        resource["show"](request, id) if (request.method == "GET" and
                                          id and
                                          resource.get("show")) else \
        resource["new"](request) if (request.method == "GET" and
                                     new and
                                     not id and
                                     resource.get("new")) else \
        resource["create"](request) if ((request.method == "POST") and
                                        not new and
                                        not id and
                                        not subresource and
                                        resource.get("create")) else \
        HttpResponse(
            status=405)
