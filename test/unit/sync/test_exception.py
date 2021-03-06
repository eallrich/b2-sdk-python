######################################################################
#
# File: test/unit/sync/test_exception.py
#
# Copyright 2020 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################
from .test_base import TestBase

from .deps_exception import (
    EnvironmentEncodingError,
    InvalidArgument,
    IncompleteSync,
    UnSyncableFilename,
)


class TestExceptions(TestBase):
    def test_environment_encoding_error(self):
        try:
            raise EnvironmentEncodingError('fred', 'george')
        except EnvironmentEncodingError as e:
            assert str(e) == """file name fred cannot be decoded with system encoding (george).
We think this is an environment error which you should workaround by
setting your system encoding properly, for example like this:
export LANG=en_US.UTF-8""", str(e)

    def test_invalid_argument(self):
        try:
            raise InvalidArgument('param', 'message')
        except InvalidArgument as e:
            assert str(e) == 'param message', str(e)

    def test_incomplete_sync(self):
        try:
            raise IncompleteSync()
        except IncompleteSync as e:
            assert str(e) == 'Incomplete sync: ', str(e)

    def test_unsyncablefilename_error(self):
        try:
            raise UnSyncableFilename('message', 'filename')
        except UnSyncableFilename as e:
            assert str(e) == 'message: filename', str(e)
