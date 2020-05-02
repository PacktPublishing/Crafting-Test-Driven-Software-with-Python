import pathlib
import unittest
from unittest import mock


from todo.db import BasicDB 


class TestBasicDB(unittest.TestCase):
    def test_load(self):
        mock_file = mock.MagicMock(
            read=mock.Mock(return_value='["first", "second"]')
        )
        mock_file.__enter__.return_value = mock_file    
        mock_opener = mock.Mock(return_value=mock_file)
        
        db = BasicDB(pathlib.Path("testdb"), _fileopener=mock_opener)
        loaded = db.load()

        self.assertEqual(
            mock_opener.call_args[0][0], 
            pathlib.Path("testdb")
        )
        mock_file.read.assert_called_with()
        self.assertEqual(loaded, ["first", "second"])

    def test_missing_load(self):
        mock_opener = mock.Mock(side_effect=FileNotFoundError)

        db = BasicDB(pathlib.Path("testdb"), _fileopener=mock_opener)
        loaded = db.load()

        self.assertEqual(
            mock_opener.call_args[0][0], 
            pathlib.Path("testdb")
        )
        self.assertEqual(loaded, [])

    def test_save(self):
        mock_file = mock.MagicMock(write=mock.Mock())
        mock_file.__enter__.return_value = mock_file    
        mock_opener = mock.Mock(return_value=mock_file)
        
        db = BasicDB(pathlib.Path("testdb"), _fileopener=mock_opener)
        loaded = db.save(["first", "second"])

        self.assertEqual(
            mock_opener.call_args[0][0:2], 
            (pathlib.Path("testdb"), "w+")
        )
        mock_file.write.assert_called_with('["first", "second"]')
