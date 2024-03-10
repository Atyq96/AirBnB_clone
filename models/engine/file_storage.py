#!/usr/bin/python3
"""File Storage"""

import json
from models.base_model import BaseModel


class FileStorage:
    """defines a FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_object = {}
        for n in self.__objects:
            json_object[n] = self.__objects[n].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_object, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                for n,y in json.load(f).items():
                    attri_value = eval(y["__class__"])(**y)
                    self.__objects[n] = attri_value
        except FileNotFoundError:
            pass
