import json

from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello World')

def get(request):
    if request.META.get("SERVER_PORT") == "80":
        http_host = request.META.get("HTTP_HOST", "httpbin.org")
        host_no_default_port = http_host.replace(":80", "")
        request.META["HTTP_HOST"] = host_no_default_port
    host = request.META["HTTP_HOST"]

    response = HttpResponse(json.dumps({
        "method": request.META["REQUEST_METHOD"],
        "headers": {"Host": host},
        "args": {
            p: v for (p, v) in request.GET.items()
        },
        "form": {
            p: v for (p, v) in request.POST.items()
        },
        "url": request.build_absolute_uri()
    }, sort_keys=True))
    response['Content-Type'] = 'application/json'
    return response