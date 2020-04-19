import unittest
import threading
import queue


from todo.app import TODOApp


class TestTODOAcceptance(unittest.TestCase):
    def setUp(self):
        self.inputs = queue.Queue()
        self.outputs = queue.Queue()

        self.fake_output = self.outputs.put
        self.fake_input = lambda: self.inputs.get(timeout=1)

    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))
        
        app_thread = threading.Thread(target=app.run)
        app_thread.start()

        welcome = self.outputs.get(timeout=1)
        self.assertEqual(welcome, """TODOs:


> """)

        self.inputs.put("add buy milk")
        welcome = self.outputs.get(timeout=1)
        self.assertEqual(welcome, """TODOs:
1. buy milk

> """)

        self.inputs.put("add buy eggs")
        welcome = self.outputs.get(timeout=1)
        self.assertEqual(welcome, """TODOs:
1. buy milk
2. buy eggs

> """)

        self.inputs.put("del 1")
        welcome = self.outputs.get(timeout=1)
        self.assertEqual(welcome, """TODOs:
1. buy eggs

> """)

        self.inputs.put("quit")
        app_thread.join()

        self.assertEqual(self.outputs.get_nowait(), "bye!")