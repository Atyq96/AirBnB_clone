#!/usr/bin/python3
"""Base Model"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """defines a BaseModel"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if kwargs:
            for x, y in kwargs.items():
                if x == "created_at":
                    y = datetime.strptime(y, '%Y-%m-%dT%H:%M:%S.%f')
                if x == "updated_at":
                    y = datetime.strptime(y, '%Y-%m-%dT%H:%M:%S.%f')
                if x != "__class__":
                    setattr(self, x, y)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns printable string representation"""
        namo = self.__class__.__name__
        return "[{}] ({}) {}".format(namo, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary with all keys/value of the instance"""
        instance_dict = self.__dict__.copy()

        instance_dict['__class__'] = self.__class__.__name__

        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
