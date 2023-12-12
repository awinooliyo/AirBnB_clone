#!/usr/bin/python3
"""Defines Unittests for FileStorage class"""

import unittest
import json
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up method to initialize instances before tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up method after each test"""
        if hasattr(self, 'storage') and \
                getattr(self, 'storage', None) is not None:
            del self.storage

    def test__filepath_method(self):
        """Test the '__filepath' method"""
        file_path = self.storage._FileStorage__file_path
        self.assertEqual(file_path, "file.json")

    def test__objects_method(self):
        """Test the '__objects' method"""
        objects = self.storage._FileStorage__objects
        self.assertEqual(objects, {})

    def test_all_method(self):
        """Test the 'all' method"""
        user1 = User()
        user1.name = "John"
        user2 = User()
        user2.name = "Alice"
        self.storage.new(user1)
        self.storage.new(user2)

        all_objects = self.storage.all()

        # Check if User objects are present in all_objects
        self.assertIn("User." + user1.id, all_objects.keys())
        self.assertIn("User." + user2.id, all_objects.keys())

        # Retrieve User objects by their IDs
        retrieved_user1 = all_objects.get("User." + user1.id)
        retrieved_user2 = all_objects.get("User." + user2.id)

        # Check if the retrieved User objects have the expected names
        self.assertEqual(retrieved_user1.name, "John")
        self.assertEqual(retrieved_user2.name, "Alice")

    def test_init_method(self):
        """Test the '__init__' method with keyword arguments"""
        # Create a user with specific ID and name
        user = User(id="123", name="John")
        self.storage.new(user)
        self.storage.save()

        # Clear the current storage object to simulate reloading from the file
        del self.storage
        new_storage = FileStorage()
        new_storage.reload()

        # Get all stored objects
        all_objects = new_storage.all()

        # Check if the specific user was stored and its name matches
        self.assertIn("User.123", all_objects)
        self.assertEqual(all_objects["User.123"].name, "John")

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

    def test_save_method_updates_updated_at(self):
        """Test if the 'save' method updates updated_at attribute"""
        user = User()
        self.storage.new(user)
        old_updated_at = user.updated_at
        self.storage.save()

        # Simulate a time delay
        user.name = "New Name"
        self.storage.save()

        new_updated_at = user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_method_does_not_write_to_file(self):
        """Test if the 'save' method updates objects without writing to file"""
        user = User()
        user.name = "Alice"
        self.storage.new(user)
        self.storage.save()

        objects_before_save = self.storage._FileStorage__objects.copy()
        user.name = "Updated Alice"
        self.storage.save()
        objects_after_save = self.storage._FileStorage__objects

        # Ensure that objects don't change after saving without file write
        self.assertEqual(objects_before_save, objects_after_save)

    def test_save_method(self):
        """Test the 'save' method"""
        user = User()
        user.name = "Alice"
        self.storage.new(user)
        self.storage.save()

        objects_before_save = self.storage._FileStorage__objects.copy()
        user.name = "Updated Alice"
        self.storage.save()
        objects_after_save = self.storage._FileStorage__objects

        # Ensure that objects don't change after saving without file write
        self.assertEqual(objects_before_save, objects_after_save)

    def test_save(self):
        """Test the 'save' method without arguments"""
        user = User()
        user.name = "John"
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()

        self.assertIn("User." + user.id, self.storage.all().keys())
        self.assertEqual(self.storage.all()["User." + user.id]["name"], "John")

    def test_reload_method_loads_from_file(self):
        """Test if the 'reload' method loads data from a file"""

        # Simulate storing some objects
        user1 = User()
        user2 = User()
        user3 = User()
        self.storage.new(user1)
        self.storage.new(user2)
        self.storage.new(user3)
        self.storage.save()

        # Clear the current storage object to simulate reloading from the file
        del self.storage
        new_storage = FileStorage()
        new_storage.reload()

        # Get all stored objects after reload
        all_objects = new_storage.all()

        self.assertEqual(len(all_objects), 3)

    def test_reload_method(self):
        """Test the 'reload' method"""
        user = User()
        user.name = "John"
        self.storage.new(user)
        self.storage.save()

        # Reset the storage object
        del self.storage
        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn("User." + user.id, new_storage.all().keys())
        self.assertEqual(new_storage.all()["User." + user.id]["name"], "John")


if __name__ == '__main__':
    unittest.main()
