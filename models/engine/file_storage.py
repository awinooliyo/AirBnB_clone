"""file_storage module"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        try:
            my_dictionary = {}

            for key, value in self.__objects.items():
                my_dictionary[key] = value.to_dict()

            with open(self.__file_path, "w") as file:
                json.dump(my_dictionary, file)
        except FileNotFoundError:
            pass

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals().get(class_name)
                    if class_obj:
                        obj = class_obj(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
