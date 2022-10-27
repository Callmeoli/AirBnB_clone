#!/usr/bin/python3
""" File storage """


import json
import os.path
from models.base_model import BaseModel


class FileStorage():
    """File storage class"""

    __file_path = "file.json"
    __object = {}
    def all(self):
        """ returns the dictionary __objects """
        return self.__object

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__object[obj.__class__.__name__ + "."+obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        for i in self.__object.keys():
            print(type(self.__object[i].to_dict()))
        new_dic = {key: self.__object[key].to_dict() for key in self.__object.keys()}
        with open(self.__file_path,"w") as f:
            f.write(json.dumps(new_dic))

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    self.__object[k] = eval(v['__class__'])(**v)