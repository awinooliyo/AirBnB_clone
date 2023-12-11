#!/usr/bin/python3
"""Defines Unittests for FileStorage class"""
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up method to initialize instances before tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up method after each test"""
        del self.storage

    def test_save_method_saves_to_file(self):
        """Test if the 'save' method saves data to a file"""
        user = User()
        user.name = "Alice"
        self.storage.new(user)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, "r") as file:
            data = json.load(file)
            self.assertIn(f"User.{user.id}", data)
            self.assertEqual(data[f"User.{user.id}"]["name"], "Alice")

    def test_reload_method_loads_from_file(self):
        """Test if the 'reload' method loads data from a file"""
        user = User()
        user.name = "Bob"
        self.storage.new(user)
        self.storage.save()

        # Clear the current storage object to simulate reloading from the file
        del self.storage

        new_storage = FileStorage()
        new_storage.reload()

        self.assertEqual(len(new_storage.all()), 1)
        self.assertIn(f"User.{user.id}", new_storage.all())
        self.assertEqual(new_storage.all()[f"User.{user.id}"].name, "Bob")


if __name__ == '__main__':
    unittest.main()
