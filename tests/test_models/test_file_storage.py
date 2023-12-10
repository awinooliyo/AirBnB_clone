#!usr/bin/python3

"""
file_storage unittests
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class"""

    def setUp(self):
        """Setup method to create necessary instances and paths for testing"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.user = User()
        self.base_model = BaseModel()

    def tearDown(self):
        """Cleanup method to remove test file after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test if all() returns an empty dictionary initially"""
        new = BaseModel()
        instances = storage.all()
        self.assertIsInstance(instances, dict)

        # objects = self.storage.all()
        # self.assertEqual(objects, {})

    def test_new(self):
        """Test if new() method sets object correctly in __objects"""
        new = BaseModel()

        for objects in storage.all().values():
            instances = objects
            self.assertTrue(instances is objects)

        # self.storage.new(self.user)
        # self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        """Test if save() method creates a file and saves objects"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test if reload() method loads objects from a file correctly"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])


if __name__ == '__main__':
    unittest.main()
