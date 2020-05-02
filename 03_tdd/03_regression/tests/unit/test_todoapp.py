import unittest
from unittest.mock import Mock


from todo.app import TODOApp 


class TestTODOApp(unittest.TestCase):
    def test_noloader(self):
        app = TODOApp(io=(Mock(return_value="quit"), Mock()), 
                      dbmanager=None)

        app.run()

        assert app._entries == []

    def test_load(self):
        dbmanager = Mock(
            load=Mock(return_value=["buy milk", "buy water"])
        )
        app = TODOApp(io=(Mock(return_value="quit"), Mock()), 
                      dbmanager=dbmanager)

        app.run()

        dbmanager.load.assert_called_with()
        assert app._entries == ["buy milk", "buy water"]

    def test_save(self):
        dbmanager = Mock(
            load=Mock(return_value=["buy milk", "buy water"]),
            save=Mock()
        )

        app = TODOApp(io=(Mock(return_value="quit"), Mock()), 
                      dbmanager=dbmanager)
        app.run()

        dbmanager.save.assert_called_with(["buy milk", "buy water"])
