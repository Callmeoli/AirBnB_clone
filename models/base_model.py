#!/usr/bin/python3
""""Base Model Class """


import uuid
from datetime import datetime


class BaseModel():
    """ Basemodel class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
    def __str__(self):
        """string rep of  class object"""
        return f'[{__class__.__name__}] ({self.id}) ({self.__dict__})'
    def save(self):
        """updates datetime"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        """d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d
        """
        d = {}
        d['__class__'] = __class__.__name__
        for k ,v in self.__dict__.items():
            if "created_at" == k or "updated_at" == k:
                d[k] = v.isoformat()
                continue
            d[k] = v
        return d