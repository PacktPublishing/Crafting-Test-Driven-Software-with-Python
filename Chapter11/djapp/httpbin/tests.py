import json

from django.test import TestCase


class HttpbinTests(TestCase):
    def test_home(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello World")

    def test_GET(self):        
        response = self.client.get("/get").content.decode("utf-8")

        assert '"Host": "httpbin.org"' in response
        assert '"args": {}' in response

    def test_GET_params(self):
        response = json.loads(self.client.get("/get?alpha=1").content)

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}

    def test_POST(self):
        response = json.loads(self.client.post(
            "/get?alpha=1", {"beta": "2"}
        ).content)

        assert response["headers"]["Host"] == "httpbin.org"
        assert response["args"] == {"alpha": "1"}
        assert response["form"] == {"beta": "2"}

    def test_DELETE(self):
        response = self.client.delete(
            "/anything/27"
        ).content.decode("utf-8")
        
        assert '"method": "DELETE"' in response
        assert '"url": "http://httpbin.org/anything/27"' in response