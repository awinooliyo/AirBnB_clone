#!/usr/bin/python3
"""Class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """A child of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
