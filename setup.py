#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

tests_require = [
    'virtualenv',
    'tox',
]

dependency_links = [
]


install_requires = [

]

setup(
    name='beeint',
    version='0.1',
    author='Dennis Schwertel',
    author_email='s@digitalkultur.net',
    description='',
    long_description=__doc__,
    package_dir={'': 'beeint'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': Tox},
    dependency_links = dependency_links,
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)