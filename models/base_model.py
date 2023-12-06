#!/usr/bin/python3
"""Base Model"""

from datetime import datetime
import uuid
from models.__init__ import storage


class BaseModel:
    """Base model that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for the base class

        args:
            *args: none
            **kwargs: keyword arguments
        """
        # self.id = str(uuid.uuid4())

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if not k == '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.fromisoformat(kwargs[k])
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates yje public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing
        key/values of __dict__ of the instance
        """
        bnb_dictionary = self.__dict__.copy()
        bnb_dictionary['__class__'] = self.__class__.__name__
        bnb_dictionary['created_at'] = self.created_at.isoformat()
        bnb_dictionary['updated_at'] = self.updated_at.isoformat()
        return bnb_dictionary
