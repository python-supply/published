=========
published
=========

Python library that serves as an example/template for a package publishing guide.

|pypi| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/published.svg
   :target: https://badge.fury.io/py/published
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/python-supply/published.svg?branch=main
   :target: https://travis-ci.com/python-supply/published

.. |coveralls| image:: https://coveralls.io/repos/github/python-supply/published/badge.svg?branch=main
   :target: https://coveralls.io/github/python-supply/published?branch=main

Purpose
-------
This library is an illustration of the various tasks and components involved in the process of publishing a small open-source Python package on PyPI, including establishment of linting standards, implementation of unit tests, measurement of coverage, and basic continuous integration.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install published

The library can be imported in the usual ways::

    import published
    from published import published

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configuration details)::

    nosetests

Alternatively, the unit tests that are included in the module itself can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python published/published.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint published

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
