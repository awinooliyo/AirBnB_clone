#!/usr/bin/python3
"""Unittests for Amenity Class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_amenity_instance(self):
        """Test if an instance of Amenity is created and its inheritance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attribute_default(self):
        """Test default attribute values of the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()  # Run the test cases if this script is executed directly
