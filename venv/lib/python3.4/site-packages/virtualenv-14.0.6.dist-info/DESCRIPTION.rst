Virtualenv
==========

`Mailing list <http://groups.google.com/group/python-virtualenv>`_ |
`Issues <https://github.com/pypa/virtualenv/issues>`_ |
`Github <https://github.com/pypa/virtualenv>`_ |
`PyPI <https://pypi.python.org/pypi/virtualenv/>`_ |
User IRC: #pypa
Dev IRC: #pypa-dev

Introduction
------------

``virtualenv`` is a tool to create isolated Python environments.

The basic problem being addressed is one of dependencies and versions,
and indirectly permissions. Imagine you have an application that
needs version 1 of LibFoo, but another application requires version
2. How can you use both these applications?  If you install
everything into ``/usr/lib/python2.7/site-packages`` (or whatever your
platform's standard location is), it's easy to end up in a situation
where you unintentionally upgrade an application that shouldn't be
upgraded.

Or more generally, what if you want to install an application *and
leave it be*?  If an application works, any change in its libraries or
the versions of those libraries can break the application.

Also, what if you can't install packages into the global
``site-packages`` directory?  For instance, on a shared host.

In all these cases, ``virtualenv`` can help you. It creates an
environment that has its own installation directories, that doesn't
share libraries with other virtualenv environments (and optionally
doesn't access the globally installed libraries either).

.. comment: 

Release History
===============

14.0.6 (2016-02-07)
-------------------

* Upgrade setuptools to 20.0

* Upgrade wheel to 0.29.0

* Fix an error where virtualenv didn't pass in a working ssl certificate for
  pip, causing "weird" errors related to ssl.


14.0.5 (2016-02-01)
-------------------

* Homogenize drive letter casing for both prefixes and filenames. #858


`Full Changelog <https://virtualenv.pypa.io/en/latest/changes.html>`_.

