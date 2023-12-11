#!/usr/bin/python3
"""Defines the Unittests for the Place Class"""
import unittest
from models.place import Place  # Assuming your module is in models/place.py
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_place_instance(self):
        """Test if an instance of Place is created and its inheritance"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_place_attribute_default(self):
        """Test default attribute values of the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
