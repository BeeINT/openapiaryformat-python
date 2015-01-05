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

The tests infrastructure uses a combination of lettuce_, tox_, coveralls_ and `Travis CI`_.

For your personal tests, you can execute tox directly executing specific build targets. The For example: ``tox -v -e py27`` for the lettuce tests or ``tox -e pep8`` for the pep8 checks. 

For coverage checks, you can get your report this way:

.. code-block:: bash

   cd tests  # change into tests directory
   coverage run `which lettuce`
   coverage report

Take a look at the ``tox.ini`` or ``.travis.yml`` for the current configurations of executed tests for each git push.





.. |travis| image:: https://api.travis-ci.org/BeeINT/openapiaryformat-python.png
    :alt: Travis Status
    :scale: 100%
    :target: https://travis-ci.org/BeeINT/openapiaryformat-python


.. |coverall|  image:: https://coveralls.io/repos/BeeINT/openapiaryformat-python/badge.png?branch=master
    :target: https://coveralls.io/r/BeeINT/openapiaryformat-python?branch=master

.. _lettuce: http://lettuce.it/
.. _tox: https://tox.readthedocs.org/
.. _Travis CI: https://travis-ci.org/BeeINT/openapiaryformat-python
.. _coveralls: https://coveralls.io/r/BeeINT/openapiaryformat-python
