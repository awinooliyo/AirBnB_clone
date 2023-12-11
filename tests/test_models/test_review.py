#!/usr/bin/python3
"""Defines Unittests for review class"""
import unittest
from models.review import Review  # Assuming your module is in models/review.py
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_review_instance(self):
        """Test if an instance of Review is created and its inheritance"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_review_attribute_default(self):
        """Test default attribute values of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()  # Run the test cases if this script is executed directly
