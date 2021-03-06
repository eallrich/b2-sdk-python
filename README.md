# B2 Python SDK
&nbsp;[![Continuous Integration](https://github.com/Backblaze/b2-sdk-python/workflows/Continuous%20Integration/badge.svg)](https://github.com/Backblaze/b2-sdk-python/actions?query=workflow%3A%22Continuous+Integration%22)&nbsp;[![License](https://img.shields.io/pypi/l/b2sdk.svg?label=License)](https://pypi.python.org/pypi/b2)&nbsp;[![python versions](https://img.shields.io/pypi/pyversions/b2sdk.svg?label=python%20versions)](https://pypi.python.org/pypi/b2sdk)&nbsp;[![PyPI version](https://img.shields.io/pypi/v/b2sdk.svg?label=PyPI%20version)](https://pypi.python.org/pypi/b2sdk)&nbsp;[![Docs](https://readthedocs.org/projects/b2-sdk-python/badge/?version=master)](https://b2-sdk-python.readthedocs.io/en/master/)



This repository contains a client library and a few handy utilities for easy access to all of the capabilities of B2 Cloud Storage.

[B2 command-line tool](https://github.com/Backblaze/B2_Command_Line_Tool) is an example of how it can be used to provide command-line access to the B2 service, but there are many possible applications (including FUSE filesystems, storage backend drivers for backup applications etc).

# Documentation

The latest documentation is available on [Read the Docs](https://b2-sdk-python.readthedocs.io).

# Installation

The sdk can be installed with:

    pip install b2sdk

# Version policy

b2sdk follows [Semantic Versioning](https://semver.org/) policy, so in essence the version number is MAJOR.MINOR.PATCH (for example 1.2.3) and:
- we increase MAJOR version when we make incompatible API changes
- we increase MINOR version when we add functionality in a backwards-compatible manner, and
- we increase PATCH version when we make backwards-compatible bug fixes (unless someone relies on the undocumented behavior of a fixed bug)

Therefore when setting up b2sdk as a dependency, please make sure to match the version appropriately, for example you could put this in your `requirements.txt` to make sure your code is compatible with the `b2sdk` version your user will get from pypi:

```
b2sdk>=0.0.0,<1.0.0
```


# Release History

## Not released yet

* Drop Python 2 and Python 3.4 support :tada:

## 1.1.4 (2020-07-15)

* Allow specifying custom realm in B2Session.authorize_account

## 1.1.2 (2020-07-06)

* Fix upload part for file range on Python 2.7

## 1.1.0 (2020-06-24)

* Make sync treat hidden files as deleted
* Remove arrow warnings caused by https://github.com/crsmithdev/arrow/issues/612
* Add `list_file_versions` method to buckets.
* Add server-side copy support for large files
* Add ability to synthesize objects from local and remote sources
* Add AuthInfoCache, InMemoryCache and AbstractCache to public interface
* Ignore urllib3 "connection pool is full" warning
* Add ability to filter in ScanPoliciesManager based on modification time
* Add ScanPoliciesManager and SyncReport to public interface
* Add md5 checksum to FileVersionInfo
* Add more keys to dicts returned by as_dict() methods
* Fix handling of modification time of files

## 1.0.2 (2019-10-15)

Changes:

* Remove upper version limit for arrow dependency

## 1.0.0 (2019-10-03)

Changes:

* Minor bug fix.

## 1.0.0-rc1 (2019-07-09)

Changes:

* Deprecate some transitional method names to v0 in preparation for v1.0.0.

## 0.1.10 (2019-07-09)

Changes:

* Remove a parameter (which did nothing, really) from `b2sdk.v1.Bucket.copy_file` signature


## 0.1.8 (2019-06-28)

Changes:

* Add support for b2_copy_file
* Add support for `prefix` parameter on ls-like calls


## 0.1.6 (2019-04-24)

Changes:

* Fix transferer crashing on empty file download attempt
* Rename account ID for authentication to application key ID.
Account ID is still backwards compatible, only the terminology
has changed.


## 0.1.4 (2019-04-04)

Initial official release of SDK as a separate package (until now it was a part of B2 CLI)


# Developer Info

Please see our [contributing guidelines](CONTRIBUTING.md).
