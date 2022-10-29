#!/usr/bin/python3
""""Base Model Class """


import uuid
from datetime import datetime
import models
class BaseModel():
    """ Basemodel class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            var = vars()
            for k ,v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self,k,datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string rep of  class object"""
        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'
    def save(self):
        """updates datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d