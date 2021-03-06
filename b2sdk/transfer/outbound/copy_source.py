######################################################################
#
# File: b2sdk/transfer/outbound/copy_source.py
#
# Copyright 2020 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

from b2sdk.transfer.outbound.outbound_source import OutboundTransferSource


class CopySource(OutboundTransferSource):
    def __init__(self, file_id, offset=0, length=None):
        if length is None and offset > 0:
            raise ValueError('Cannot copy with non zero offset and unknown length')
        self.file_id = file_id
        self.length = length
        self.offset = offset

    def __repr__(self):
        return '<{classname} file_id={file_id} offset={offset} length={length} id={id}>'.format(
            classname=self.__class__.__name__,
            file_id=self.file_id,
            offset=self.offset,
            length=self.length,
            id=id(self),
        )

    def get_content_length(self):
        return self.length

    def is_upload(self):
        return False

    def is_copy(self):
        return True

    def get_bytes_range(self):
        if self.length is None:
            if self.offset > 0:
                # auto mode should get file info and create correct copy source (with length)
                raise ValueError('cannot return bytes range for non zero offset and unknown length')
            return None

        return (self.offset, self.offset + self.length - 1)

    def get_copy_source_range(self, relative_offset, range_length):
        if self.length is not None and range_length + relative_offset > self.length:
            raise ValueError('Range length overflow source length')
        range_offset = self.offset + relative_offset
        return self.__class__(self.file_id, range_offset, range_length)
