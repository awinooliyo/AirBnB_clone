#!/usr/bin/python3
"""Defines unittests for class BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up method to initialize instances before tests"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up method after each test"""
        del self.base_model

    def test_initialization(self):
        """Test if BaseModel initializes with proper attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ representation of BaseModel"""
        self.assertIn(self.base_model.__class__.__name__, str(self.base_model))
        self.assertIn(self.base_model.id, str(self.base_model))

    def test_save_method_updates_time(self):
        """Test if save method updates updated_at time"""
        old_time = self.base_model.updated_at
        self.base_model.save()
        new_time = self.base_model.updated_at
        self.assertNotEqual(old_time, new_time)

    def test_to_dict_method(self):
        """Test if to_dict method returns proper dictionary"""
        bnb_dict = self.base_model.to_dict()
        self.assertEqual(
            bnb_dict['__class__'],
            self.base_model.__class__.__name__
        )
        self.assertEqual(
            bnb_dict['created_at'],
            self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            bnb_dict['updated_at'],
            self.base_model.updated_at.isoformat()
        )

    def test_save_method_saves_to_storage(self):
        """Test if save method saves object to storage"""
        self.base_model.save()
        objects = storage.all()
        key = "{}.{}".format(
            type(self.base_model).__name__,
            self.base_model.id
        )
        self.assertIn(key, objects)


if __name__ == '__main__':
    unittest.main()
