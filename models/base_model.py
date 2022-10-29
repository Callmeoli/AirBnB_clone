#!/usr/bin/python3
""" Basemodel  Module
 crearte and Update ids for class
 and return dict represantation
 """


import copy
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base model """

    def __init__(self, *args, **kwargs):
        """public instance"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self,
                            key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return str representations"""
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Edit the updated time and save it to storage """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance"""
        dic = copy.deepcopy(self.__dict__)
        dic['id'] = dic['id']
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
