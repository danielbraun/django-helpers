from django.http import HttpResponse


def http_unauthorized(realm):
    response = HttpResponse('Unauthorized', status=401)
    response["WWW-Authenticate"] = "Basic realm=\"%s\"" % realm
    return response


def ip_from_request(request):
    return request.META.get("REMOTE_ADDR")
