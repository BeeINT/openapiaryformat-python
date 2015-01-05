openapiaryformat-python
=======================


|travis| |coverall|

This is a reference implementation and example scripts for the openapiaryformat. Take a look at the description at https://github.com/BeeINT/openapiaryformat-reference

Example Simple
-----------------

Take a look at the ``example_simple.py`` script on how to get a quick and basic introduction.


Example Advanced
-----------------

``example_advanced.py`` will cover the more indepth information.


Tests
------

The tests infrastructure uses a combination of tox_, coveralls_ and `Travis CI`_.

For your personal tests, you can execute ``python setup test`` in the project root. This will use tox and execute all the environments.

You can also use tox directly and executing specific build targets. For example: ``tox -v -e pypy`` or ``tox -e pep8``. 

Take a look at the ``tox.ini`` or ``.travis.yml`` for the current configurations of executed tests for each git push.





.. |travis| image:: https://api.travis-ci.org/BeeINT/openapiaryformat-python.png
    :alt: Travis Status
    :scale: 100%
    :target: https://travis-ci.org/BeeINT/openapiaryformat-python


.. |coverall|  image:: https://coveralls.io/repos/BeeINT/openapiaryformat-python/badge.png?branch=master
    :target: https://coveralls.io/r/BeeINT/openapiaryformat-python?branch=master


.. _tox: https://tox.readthedocs.org/
.. _Travis CI: https://travis-ci.org/BeeINT/openapiaryformat-python
.. _coveralls: https://coveralls.io/r/BeeINT/openapiaryformat-python
