#!/usr/bin/python3
"""Defines Unittests for class State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_state_instance(self):
        """Test if an instance of State is created and its inheritance"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_state_attribute_default(self):
        """Test default attribute values of the State class"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()  # Run the test cases if this script is executed directly
