import unittest
import unittest.mock

from chat.client import ChatClient

from .fakeserver import FakeServer


class TestChatMessageExchange(unittest.TestCase):
    def setUp(self):
        self.fakeserver = unittest.mock.patch("multiprocessing.managers.listener_client", new={
            "pickle": (None, FakeServer())
        })
        self.fakeserver.start()

    def tearDown(self):
        self.fakeserver.stop()
    
    def test_exchange_with_server(self):
        c1 = ChatClient("User1")
        c2 = ChatClient("User2")

        c1.send_message("connected message")
        
        assert c2.fetch_messages()[-1] == "User1: connected message"

    def test_many_users(self):
        firstUser = ChatClient("John Doe")

        for uid in range(5):
            moreuser = ChatClient(f"User {uid}")
            moreuser.send_message("Hello!")

        messages = firstUser.fetch_messages()
        assert len(messages) == 5
            
    def test_multiple_readers(self):
        user1 = ChatClient("John Doe")
        user2 = ChatClient("User 2")
        user3 = ChatClient("User 3")

        user1.send_message("Hi all")
        user2.send_message("Hello World")
        user3.send_message("Hi")

        user1_messages = user1.fetch_messages()
        user2_messages = user2.fetch_messages()
            
        self.assertEqual(user1_messages, user2_messages)