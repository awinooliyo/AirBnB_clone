#!/usr/bin/python3
"""Defines the Unittests for models/user.py"""

import unittest
from models.user import User  # Assuming your module is in models/user.py
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing instatiation of user class"""

    def test_user_instance(self):
        """Test if an instance of User is created and its inheritance"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        """Test default attribute values of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
