import sys, json
from django.conf.urls import re_path
from django.conf import settings
from django.http import HttpResponse

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS=["httpbin.org"]
)


def home(request):
    return HttpResponse('Hello World')

def get(request):
    if request.META.get("SERVER_PORT") == "80":
        host_no_default_port = request.META["HTTP_HOST"].replace(":80", "")
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

urlpatterns = [
    re_path(r'^get$', get),
    re_path(r"^anything.*$", get),
    re_path(r'^$', home),
]

def make_application():
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                          'wbtframeworks.django.settings')

    return get_wsgi_application()
