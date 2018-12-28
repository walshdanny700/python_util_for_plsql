plsqlutil
=========================
|build-status| |coverage| |docs| |pypi| |version|

A utility module for working with PL/SQL

Getting Started
================
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
================
Requires Python 3.4 or higher

Installing
================
.. code-block:: python
    pip install plsqlutil

Usage
================
The following will import the function walk_pkg_gen

.. code-block:: python
    from plsqlutil.plsql_util import walk_pkg_gen

    directory = '.'
    for path_string, filename in walk_pkg_gen(directory)
        # use filename and path string


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
