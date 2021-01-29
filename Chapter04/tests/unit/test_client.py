import unittest
import unittest.mock

from chat.client import ChatClient


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"

    def test_send_message(self):
        client = ChatClient("User 1", connection_provider=unittest.mock.Mock())

        sent_message = client.send_message("Hello World")
        
        assert sent_message == "User 1: Hello World"

    def test_client_connection(self):
        connection_spy = unittest.mock.MagicMock()

        client = ChatClient("User 1", connection_provider=lambda *args: connection_spy)
        client.send_message("Hello World")

        connection_spy.broadcast.assert_called_with(("User 1: Hello World"))

    def test_client_fetch_messages(self):
        connection = unittest.mock.Mock()
        connection.get_messages.return_value = ["message1", "message2"]

        client = ChatClient("User 1", connection_provider=lambda *args: connection)
        
        starting_messages = client.fetch_messages()
        client.connection.get_messages().append("message3")
        new_messages = client.fetch_messages()

        assert starting_messages == ["message1", "message2"]
        assert new_messages == ["message3"]


