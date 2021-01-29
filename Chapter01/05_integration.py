import unittest

class Authentication:
    USERS = [{"username": "user1",
              "password": "pwd1"}]

    def login(self, username, password):
        u = self.fetch_user(username)
        if not u or u["password"] != password:
            return None
        return u

    def fetch_user(self, username):
        for u in self.USERS:
            if u["username"] == username:
                return u
        else:
            return None


class Authorization:
    PERMISSIONS = [{"user": "user1",
                    "permissions": {"create", "edit", "delete"}}]

    def can(self, user, action):
        for u in self.PERMISSIONS:
            if u["user"] == user["username"]:
                return action in u["permissions"]
        else:
            return False


class TestAuthentication(unittest.TestCase):
    def test_login(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "testpass")
        
        assert resp == {"username": "testuser", "password": "testpass"}

    def test_failed_login(self):
        auth = Authentication()

        resp = auth.login("usernotexisting", "")

        assert resp is None

    def test_wrong_password(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        resp = auth.login("testuser", "wrongpass")

        assert resp == None

    def test_fetch_user(self):
        auth = Authentication()
        auth.USERS = [{"username": "testuser", "password": "testpass"}]

        user = auth.fetch_user("testuser")

        assert user == {"username": "testuser", "password": "testpass"}

    def test_fetch_user_not_existing(self):
        auth = Authentication()
                              
        resp = auth.fetch_user("usernotexisting")
              
        assert resp is None


class TestAuthorization(unittest.TestCase):
    def test_can(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]

        resp = authz.can({"username": "testuser"}, "create")

        assert resp is True

    def test_not_found(self):
        authz = Authorization()

        resp = authz.can({"username": "usernotexisting"}, "create")

        assert resp is False

    def test_unathorized(self):
        authz = Authorization()
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]
                      
        resp = authz.can({"username": "testuser"}, "delete")
                      
        assert resp is False


class TestAuthorizeAuthenticatedUser(unittest.TestCase):
    def test_auth(self):
        auth = Authentication()
        authz = Authorization()              
        auth.USERS = [{"username": "testuser", "password": "testpass"}]
        authz.PERMISSIONS = [{"user": "testuser", "permissions": {"create"}}]      

        u = auth.login("testuser", "testpass")
        resp = authz.can(u, "create")

        assert resp is True


if __name__ == '__main__':
    unittest.main()
