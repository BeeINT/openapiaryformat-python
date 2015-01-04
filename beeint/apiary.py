import beeint
import datetime

class Apiary(object):

    def __init__(self, name='', enable_history = False):
        self.enable_history = False # deactivate this in the beginning to NOT have a history of the initial setup
        self.__history = []
        self.type = beeint.TYPE_APIARY + "ASD"
        self.name = name
        self.enable_history = enable_history
        

    def add_history(self, key, value_old, value_new, date=None):
        entry = {
            "date": datetime.datetime.now(),
            "old":{
                key: value_old,
            },
            "new": {
                key: value_new,
            }

        }
        self.__history.append(entry)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if self.enable_history:
            self.add_history("name", getattr(self, "__name", ""), value)
        self.__name = value
        

    def __str__(self):
        return self.name

    def dumps(self):
        print self.__history