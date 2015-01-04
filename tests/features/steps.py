from lettuce import *

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

from beeint import Apiary

@step
def have_an_apiary(step):
    u'^Given I have a new Apiary$'
    world.apiary = Apiary()

@step
def have_an_apiary_with_name(step, name):
    u'^Given I have a new Apiary with the name "([^"]*)"$'

    world.apiary = Apiary(name)



@step
def set_the_name(step, name):
    u'I set the name to "([^"]*)"'
    world.apiary.name = name


@step
def see_the_name(step, name):
    u'I see the name "([^"]*)"'
    assert world.apiary.name == name, "Got %s" % world.apiary.name
