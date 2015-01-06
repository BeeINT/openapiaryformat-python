import datetime
import hashlib


TYPE_APIARY = 'apiary'
TYPE_HIVE = 'hive'
TYPE_LINK = 'link'


def generate_id(seed=False):
    """ tries to generate a unique id. Hives and Apiarys have unique ids"""
    return hashlib.sha224(str(seed) + str(datetime.datetime.now())).hexdigest()




def history_logging(function):
    """ decorator to enable history logging for subclasses of the HistoryAware object"""
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.enable_history:
            self.add_history(function.__name__, getattr(self, "__{0}".format(function.__name__), False), args[1])
        return function(*args, **kwargs)
    return wrapper



class HistoryAware(object):

    history_attributes  = []

    def __init__(self):
        self.__history = []
        self.enable_history = False
        for attribute in self.history_attributes :
            self.__add_attribute(Apiary, attribute)


    def add_history(self, key, value_old, value_new, date=None):
        entry = {
            "date": datetime.datetime.now(),
            "old": {
                key: value_old,
            },
            "new": {
                key: value_new,
            }

        }
        self.__history.append(entry)


    def __add_attribute(self, clas, attribute):   
        getter = lambda self: getattr(self, "_{0}__{1}".format(clas, attribute), False)
        getter.__name__ = attribute

        setter_intern = lambda self, value: setattr(self, "_{0}__{1}".format(clas, attribute), value)
        setter_intern.__name__ = attribute
        setter = history_logging(setter_intern)    

        setattr(clas, attribute, 
            property( 
                getter,
                setter
            )
        )




    @property
    def history(self):
        return getattr(self, "_HistoryAware__history", False)



#import Classes for better importing in 3rd party code
from apiary import Apiary
