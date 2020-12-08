import json
from httpclient import HTTPClient
import requests_mock


class TestHTTPClient:
    def test_GET(self):
        client = HTTPClient(url="http://httpbin.org/get")
        
        with requests_mock.Mocker() as m:
            m.get(client._url, text='{"Host": "httpbin.org", "args": {}}')
            response = client.GET()

        assert '"Host": "httpbin.org"' in response
        assert '"args": {}' in response

    def test_GET_params(self):
        client = HTTPClient(url="http://httpbin.org/get?alpha=1")
        
        with requests_mock.Mocker() as m:
            m.get(client._url, text='''{"headers": {"Host": "httpbin.org"},
                                        "args": {"alpha": "1"}}''')
            response = client.GET()

        response = json.loads(response)
        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}

    def test_POST(self):
        client = HTTPClient(url="http://httpbin.org/post?alpha=1")
        
        with requests_mock.Mocker() as m:
            m.post(client._url, json={"headers": {"Host": "httpbin.org"},
                                      "args": {"alpha": "1"},
                                      "form": {"beta": "2"}})
            response = client.POST(beta=2)

        response = json.loads(response)
        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}
        assert response["form"] == {"beta": "2"}

    def test_DELETE(self):
        client = HTTPClient(url="http://httpbin.org/anything/27")
        
        with requests_mock.Mocker() as m:
            m.delete(client._url, json={
                "method": "DELETE", 
                "url": "http://httpbin.org/anything/27"
            })
            response = client.DELETE()

        assert '"method": "DELETE"' in response
        assert '"url": "http://httpbin.org/anything/27"' in response

    def test_follow(self):
        client = HTTPClient(url="http://httpbin.org/anything")

        assert client._url == "http://httpbin.org/anything"

        client2 = client.follow("me")

        assert client2._url == "http://httpbin.org/anything/me"

