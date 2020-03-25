import unittest
import unittest.mock


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        with new_chat_server() as srv: 
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

    def test_client_fetch_messages(self):
        client = ChatClient("User 1")
        client.connection = unittest.mock.Mock()
        client.connection.get_messages.return_value = ["message1", "message2"]

        starting_messages = client.fetch_messages()
        client.connection.get_messages().append("message3")
        new_messages = client.fetch_messages()

        assert starting_messages == ["message1", "message2"]
        assert new_messages == ["message3"]



class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")

            assert c.get_messages()[-1] == "some message"

    def test_exchange_with_server(self):
        with unittest.mock.patch("multiprocessing.managers.listener_client", new={
            "pickle": (None, FakeServer())
        }):
            c1 = Connection(("localhost", 9090))
            c2 = Connection(("localhost", 9090))

            c1.broadcast("connected message")
            
            assert c2.get_messages()[-1] == "connected message"


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self._connection = None
        self._last_msg_idx = 0

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(sent_message)
        return sent_message

    def fetch_messages(self):
        messages = list(self.connection.get_messages())
        new_messages = messages[self._last_msg_idx:]
        self._last_msg_idx = len(messages)
        return new_messages

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
        return Connection(("localhost", 9090))


from multiprocessing.managers import SyncManager, ListProxy
class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages", proxytype=ListProxy)
        super().__init__(address=address, authkey=b'mychatsecret')
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


def new_chat_server():
    messages = []
    class _ChatServerManager(SyncManager):
        pass
    _ChatServerManager.register("get_messages", callable=lambda: messages, 
                                proxytype=ListProxy)    
    return _ChatServerManager(("", 9090), authkey=b'mychatsecret')


if __name__ == '__main__':
    unittest.main()
