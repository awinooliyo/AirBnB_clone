#!/usr/bin/python3
"""Defines the Unittests for FileStorage Class"""
import unittest
from models.user import User
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up method to initialize instances before tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up method after each test"""
        del self.storage

    def test_all_method(self):
        """Test the 'all' method"""
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        """Test the 'new' method"""
        user = User()
        self.storage.new(user)
        self.assertIn(f"User.{user.id}", self.storage.all())

    def test_save_reload_methods(self):
        """Test the 'save' and 'reload' methods"""
        user = User()
        user.name = "Alice"
        self.storage.new(user)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(new_storage.all(), self.storage.all())


if __name__ == '__main__':
    unittest.main()
