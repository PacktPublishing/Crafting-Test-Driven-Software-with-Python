import json

import urllib.parse


class Application:
    def __call__(self, environ, start_response):
        start_response(
            '200 OK', 
            [('Content-type', 'application/json; charset=utf-8')]
        )

        form_params = {}
        if environ.get('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
            req_body = environ["wsgi.input"].read().decode("ascii")
            form_params = {
                k: v for k, v in urllib.parse.parse_qsl(req_body)
            }

        if environ.get("SERVER_PORT") == "80":
            host = environ["SERVER_NAME"]
        else:
            host = environ["HTTP_HOST"]

        return [json.dumps({
            "method": environ["REQUEST_METHOD"],
            "headers": {"Host": host},
            "url": "{e[wsgi.url_scheme]}://{host}{e[PATH_INFO]}".format(
                e=environ, 
                host=host
            ),
            "args": {
                k: v for k, v in urllib.parse.parse_qsl(environ["QUERY_STRING"])
            },
            "form": form_params
        }).encode("utf-8")]
