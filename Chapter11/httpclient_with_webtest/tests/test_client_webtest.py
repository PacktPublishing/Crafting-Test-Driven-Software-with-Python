import json

import webtest

from wsgiwebtest import Application
from httpclient import HTTPClient


class TestHTTPClientWebTest:
    def test_GET(self):
        client = HTTPClient(url="http://httpbin.org/get",
                            requests=webtest.TestApp(Application()))
        
        response = client.GET()

        assert '"Host": "httpbin.org"' in response
        assert '"args": {}' in response

    def test_GET_params(self):
        client = HTTPClient(url="http://httpbin.org/get?alpha=1",
                            requests=webtest.TestApp(Application()))
        
        response = client.GET()
        response = json.loads(response)

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}

    def test_POST(self):
        client = HTTPClient(url="http://httpbin.org/post?alpha=1",
                            requests=webtest.TestApp(Application()))
        
        response = client.POST(beta=2)
        response = json.loads(response)

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}
        assert response["form"] == {"beta": "2"}

    def test_DELETE(self):
        client = HTTPClient(url="http://httpbin.org/anything/27",
                            requests=webtest.TestApp(Application()))
        
        response = client.DELETE()

        assert '"method": "DELETE"' in response
        assert '"url": "http://httpbin.org/anything/27"' in response
