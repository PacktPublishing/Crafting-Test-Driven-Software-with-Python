import unittest
import timeit

from chat.client import ChatClient
from chat.server import new_chat_server


class BenchmarkMixin:
    def bench(self, f, number):
        t = timeit.timeit(f, number=number)
        print(f"\n\ttime: {t:.2f}, iteration: {t/number:.2f}")


class BenchmarkChat(unittest.TestCase, BenchmarkMixin):
    def test_sending_messages(self):
        with new_chat_server() as srv:
            user1 = ChatClient("User1")

            self.bench(lambda: user1.send_message("Hello World"), number=10)
