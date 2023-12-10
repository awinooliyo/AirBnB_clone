#!/usr/bin/python3

"""
tests module
"""

import unittest
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """
        Test if the BaseModel instance initializes correctly
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
        Create a BaseModel instance with
        specific data using keyword arguments
        """
        data = {
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(base_model.created_at.isoformat(), data['created_at'])
        self.assertEqual(base_model.updated_at.isoformat(), data['updated_at'])

    @patch('models.storage.new')
    def test_save(self, mock_storage_new):
        """
        Test if the save method updates the 'updated_at'
        attribute and calls storage.new
        """
        base_model = BaseModel()
        base_model.save()
        self.assertIsInstance(base_model.updated_at, datetime)
        mock_storage_new.assert_called_once()

    def test_to_dict(self):
        """
        Test the to_dict method to ensure it returns the
        expected dictionary format
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
