from lettuce import *

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

from beeint import Apiary, Hive


@step
def have_an_apiary(step):
    u'^Given I have a new Apiary$'
    world.testobj = Apiary()


@step
def have_an_apiary_with_name(step, name):
    u'^Given I have a new Apiary with the name "([^"]*)"$'
    world.testobj = Apiary(name)


@step
def have_a_hive(step):
    u'^Given I have a new Hive$'
    world.testobj = Hive()


@step
def have_a_hive_with_name(step, name):
    u'^Given I have a new Hive with the name "([^"]*)"$'
    world.testobj = Hive(name)


@step
def set_the_attribute(step, attribute, value):
    u'I set the ([^"]*) to "([^"]*)"'
    setattr(world.testobj, attribute, value)


@step
def see_the_attribute(step, attribute, value):
    u'I see the ([^"]*) is "([^"]*)"'
    assert getattr(world.testobj, attribute) == value, "Got %s" % getattr(world.testobj, attribute)


@step
def see_the_attribute_is_false(step, attribute):
    u'I see the ([^"]*) is False'
    assert getattr(world.testobj, attribute) is False, "Got %s" % getattr(world.testobj, attribute)


@step
def see_the_attribute_is_of_size(step, attribute, size):
    u'I see the ([^"]*) is of size ([^"]*)'
    assert len(getattr(world.testobj, attribute)) == int(size), "Got %s, size %s" % (getattr(world.testobj, attribute), int(size))


@step
def activate_history(step):
    u'I activate the history'
    world.testobj.enable_history = True


@step
def deactivate_history(step):
    u'I deactivate the history'
    world.testobj.enable_history = False


@step
def default_representation(step, value):
    u'the default representation of the apiary object is "([^"]*)"'
    assert str(world.testobj) == value, "Got %s" % str(world.testobj)


@step
def dumps_string_returnsize(step, value):
    u'dumps\(\) should return a string of ([^"]*) characters'
    assert len(world.testobj.dumps()) == int(value), "Got %s" % str(len(world.testobj.dumps()))
