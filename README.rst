plsqlutil
=========================
|build-status| |coverage| |docs| |pypi| |version|

A utility module for working with PL/SQL

Getting Started
================
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
================
Requires Python 3.6 or higher

Installing
================
.. code:: python

    pip install plsqlutil

Usage
================
The function walk_pkg_gen is a generator that yields the path and filename of any file
that has the extensions pkb(package body) or pks(package specification).
The following example is how to use walk_pkg_gen

.. code:: python

    from plsqlutil.plsql_util import walk_pkg_gen
    import pathlib

    directory = pathlib.Path.cwd()
    for pathObject in walk_pkg_gen(directory)
        # use pathObject


License
================
This project is licensed under the MIT License

.. |build-status| image:: https://travis-ci.com/walshdanny700/python_util_for_plsql.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.com/walshdanny700/python_util_for_plsql

.. |coverage| image:: https://coveralls.io/repos/github/walshdanny700/python_util_for_plsql/badge.svg?branch=master
    :alt: Documentation Status
    :scale: 100%
    :target: https://coveralls.io/github/walshdanny700/python_util_for_plsql?branch=master

.. |docs| image:: https://readthedocs.org/projects/pip/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://readthedocs.org/projects/pip/badge/

.. |pypi| image:: https://badge.fury.io/py/plsqlutil.svg
    :alt: Documentation Status
    :scale: 100%
    :target: https://badge.fury.io/py/plsqlutil

.. |version| image:: https://img.shields.io/pypi/pyversions/plsqlutil.svg
    :alt: Documentation Status
    :scale: 100%
    :target: https://pypi.python.org/pypi/plsqlutil