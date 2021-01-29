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


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")

            assert c.get_messages()[-1] == "some message"



class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(message)
        return sent_message


from multiprocessing.managers import SyncManager
class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address)
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


if __name__ == '__main__':
    unittest.main()
