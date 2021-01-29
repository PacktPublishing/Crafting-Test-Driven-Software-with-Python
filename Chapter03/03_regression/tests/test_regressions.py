import unittest
from unittest import mock
import io

from todo.app import TODOApp
from todo.db import BasicDB


class TestRegressions(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = mock.Mock()

        data = ["buy milk", 'install "Focal Fossa"']

        dbmanager = BasicDB(None, _fileopener=mock.Mock(
            return_value=fakefile
        ))

        dbmanager.save(data)
        fakefile.seek(0)
        loaded_data = dbmanager.load() 
        
        self.assertEqual(loaded_data, data)
