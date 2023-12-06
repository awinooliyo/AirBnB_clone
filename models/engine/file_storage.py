#!/usr/bin/python2
import json
# from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        return self.__objects


    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        try:
            my_dictionary = {}

            for k, v in self.__objects.items():
                my_dictionary[k] = 

            with open(self.__file_path, "w") as file:
                json.dump(my_dictionaryeModel, file)
        except FileNotFoundError:
            pass

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                content = json.load(file)
        except FileNotFoundError:
            pass

