import unittest
import unittest.mock


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        user1 = ChatClient("John Doe")
        user2 = ChatClient("Harry Potter")

        user1.send_message("Hello World")
        messages = user2.fetch_messages()
        
        assert messages == ["John Doe: Hello World"]


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"

    def test_send_message(self):
        client = ChatClient("User 1")
        client.connection = unittest.mock.Mock()

        sent_message = client.send_message("Hello World")
        
        assert sent_message == "User 1: Hello World"

    def test_client_connection(self):
        client = ChatClient("User 1")

        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(client, "_get_connection", 
                                        return_value=connection_spy):
            client.send_message("Hello World")

        connection_spy.broadcast.assert_called_with(("User 1: Hello World"))


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")
            messages = c.get_messages()
        
        assert messages[-1] == "some message"

    def test_exchange_with_server(self):
        import multiprocessing.managers
        multiprocessing.managers.listener_client["fake"] = (None, FakeServer())
        c1 = Connection(("localhost", 9090), serializer="fake")
        c2 = Connection(("localhost", 9090), serializer="fake")

        c1.broadcast("connected message")
        
        assert c2.get_messages()[-1] == "connected message"
        

class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self._connection = None

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(sent_message)
        return sent_message

    def fetch_messages(self):
        return list(self.connection.get_messages())

    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._get_connection()
        return self._connection

    @connection.setter
    def connection(self, value):
        if self._connection is not None:
            self._connection.close()
        self._connection = value

    def _get_connection(self):
        c = Connection(("localhost", 9090))
        c.connect()
        return c


from multiprocessing.managers import SyncManager, ListProxy
class Connection(SyncManager):
    def __init__(self, address, **kwargs):
        self.register("get_messages", proxytype=ListProxy)
        super().__init__(address=address, authkey=b'mychatsecret', **kwargs)
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


class FakeServer:
    def __init__(self):
        self.last_command = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        return self

    def send(self, data):
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args

    def recv(self, *args, **kwargs):
        if self.last_command == "dummy":
            return "#RETURN", None
        elif self.last_command == "create":
            return "#RETURN", ("fakeid", tuple())
        elif self.last_command == "append":
            self.messages.append(self.last_args[0])
            return "#RETURN", None
        elif self.last_command == "__getitem__":
            return "#RETURN", self.messages[self.last_args[0]]
        elif self.last_command in ("incref", "decref", "accept_connection"):
            return "#RETURN", None
        else:
            return "#ERROR", Exception("Unrecognised: %s" % self.last_command)

    def close(self):
        pass


if __name__ == '__main__':
    unittest.main()
