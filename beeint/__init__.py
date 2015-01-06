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
            self._add_history(function.__name__, getattr(self, "__{0}".format(function.__name__), False), args[1])
        return function(*args, **kwargs)
    return wrapper







class HistoryAware(object):

    history_attributes  = []


    @classmethod
    def __add_attribute(clas, attribute): 
        """Creates dynamic attributes on classes as propertys. It decorates the property setter with the "history_logging" function """
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

    @classmethod
    def finish_initialization(the_class):
        """ This function must be called after a child Class gets initialized. It creates the "history_attributes" for the child class."""
        the_class.initialized = True
        for attribute in the_class.history_attributes :
                the_class.__add_attribute( attribute)


    def __init__(self):
        if not getattr(self, "initialized", False):
            raise Exception("finish_initialization() was not called on the {0} Class".format(type(self).__name__))
        self.__history = []
        self.enable_history = False
        


    def _add_history(self, key, value_old, value_new, date=None):
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


    @property
    def history(self):
        return getattr(self, "_HistoryAware__history", False)



#import Classes for better importing in 3rd party code
from apiary import Apiary
from hive import Hive