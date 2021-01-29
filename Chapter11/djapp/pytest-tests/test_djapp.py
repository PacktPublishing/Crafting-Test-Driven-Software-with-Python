import sys
import webtest

sys.path.append(".")
from djapp.wsgi import application as wsgiapp


class TestWSGIApp:
    def test_home(self):
        client = webtest.TestApp(wsgiapp)
        
        response = client.get("http://httpbin.org/").text

        assert 'Hello World' in response

    def test_GET(self):
        client = webtest.TestApp(wsgiapp)
        
        response = client.get("http://httpbin.org/get").text

        assert '"Host": "httpbin.org"' in response
        assert '"args": {}' in response

    def test_GET_params(self):
        client = webtest.TestApp(wsgiapp)

        response = client.get(url="http://httpbin.org/get?alpha=1").json

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}

    def test_POST(self):
        client = webtest.TestApp(wsgiapp)

        response = client.post(url="http://httpbin.org/get?alpha=1",
                               params={"beta": "2"}).json

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}
        assert response["form"] == {"beta": "2"}

    def test_DELETE(self):
        client = webtest.TestApp(wsgiapp)

        response = client.delete(url="http://httpbin.org/anything/27").text
        
        assert '"method": "DELETE"' in response
        assert '"url": "http://httpbin.org/anything/27"' in response