import sys
import urllib.parse
import requests


class HTTPClient:
    def __init__(self, url):
        self._url = url

    def follow(self, path):
        baseurl = self._url
        if not baseurl.endswith("/"):
            baseurl += "/"
        return HTTPClient(urllib.parse.urljoin(baseurl, path))

    def GET(self):
        return requests.get(self._url).text

    def POST(self, **kwargs):
        return requests.post(self._url, data=kwargs).text

    def DELETE(self):
        return requests.delete(self._url).text


def parse_args():
    cmd = sys.argv[0]
    args = sys.argv[1:]
    try:
        method, url, *params = args
    except ValueError:
        raise ValueError("Not enough arguments, "
                         "at least METHOD URL must be provided")

    try:
        params = dict((p.split("=", 1) for p in params))
    except ValueError:
        raise ValueError("Invalid request body parameters. "
                         "They must be in name=value format, "
                         f"not {params}")

    return method.upper(), url, params


def main():
    try:
        method, url, params = parse_args()
    except ValueError as err:
        print(err)
        return

    client = HTTPClient(url)
    print(getattr(client, method)(**params))