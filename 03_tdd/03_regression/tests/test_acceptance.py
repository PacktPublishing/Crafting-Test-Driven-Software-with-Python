import unittest
import threading
import queue

from todo.app import TODOApp


class TestTODOAcceptance(unittest.TestCase):
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()

        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()

        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)

    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))
        
        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "\n"
            "\n"
            "> "
        ))

        self.send_input("add buy milk")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy milk\n"
            "\n"
            "> "
        ))

        self.send_input("add buy eggs")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy milk\n"
            "2. buy eggs\n"
            "\n"
            "> "
        ))

        self.send_input("del 1")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy eggs\n"
            "\n"
            "> "
        ))

        self.send_input("quit")
        app_thread.join(timeout=1)

        self.assertEqual(self.get_output(), "bye!\n")