import unittest
import unittest.mock

from chat.client import ChatClient
from chat.server import new_chat_server


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        with new_chat_server() as srv:
            user1 = ChatClient("John Doe")
            user2 = ChatClient("Harry Potter")

            user1.send_message("Hello World")
            messages = user2.fetch_messages()
            
            assert messages == ["John Doe: Hello World"]

    def test_smoke_sending_message(self):
        with new_chat_server() as srv:
            user1 = ChatClient("User1")
            user1.send_message("Hello World")


"""
class TestChatMultiUser(unittest.TestCase):
    def test_many_users(self):
        with new_chat_server() as srv:
            firstUser = ChatClient("John Doe")

            for uid in range(5):
                moreuser = ChatClient(f"User {uid}")
                moreuser.send_message("Hello!")

            messages = firstUser.fetch_messages()
            assert len(messages) == 5
            
    def test_multiple_readers(self):
        with new_chat_server() as srv:
            user1 = ChatClient("John Doe")
            user2 = ChatClient("User 2")
            user3 = ChatClient("User 3")

            user1.send_message("Hi all")
            user2.send_message("Hello World")
            user3.send_message("Hi")

            user1_messages = user1.fetch_messages()
            user2_messages = user2.fetch_messages()
            
            self.assertEqual(user1_messages, user2_messages)
"""
