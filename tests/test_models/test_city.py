#!/usr/bin/python3
"""Defines a Unittest for City class"""
import unittest
from models.city import City  # Assuming your module is in models/city.py
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_city_instance(self):
        """Test if an instance of City is created and its inheritance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_city_attribute_default(self):
        """Test default attribute values of the City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
