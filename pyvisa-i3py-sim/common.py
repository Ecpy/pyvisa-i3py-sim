# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2016 by Pyvisa-I3py-sim Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Common functionalities.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

import sys
import logging
import re
from string import Formatter
from io import StringIO

from pyvisa import logger

logger = logging.LoggerAdapter(logger, {'backend': 'i3py-sim'})

_FORMATTER = Formatter()


class NamedObject(object):
    """A class to construct named sentinels.

    """
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s>' % self.name

    __str__ = __repr__


if sys.version >= '3':
    def iter_bytes(data, mask, send_end):
        for d in data[:-1]:
            yield bytes([d & ~mask])

        if send_end:
            yield bytes([data[-1] | ~mask])
        else:
            yield bytes([data[-1] & ~mask])

    int_to_byte = lambda val: bytes([val])
    last_int = lambda val: val[-1]
else:
    def iter_bytes(data, mask, send_end):
        for d in data[:-1]:
            yield chr(ord(d) & ~mask)

        if send_end:
            yield chr(ord(data[-1]) | ~mask)
        else:
            yield chr(ord(data[-1]) & ~mask)

    int_to_byte = chr
    last_int = lambda val: ord(val[-1])


def build_matcher(query, optional=False):
    """Build a regular expression matching a query no matter the arguments.

    """
    matcher = StringIO()
    pattern = '\S*' if optional else '\S+'
    for literal, field, fmt, conv in _FORMATTER.parse(query):
        matcher.write(re.escape(literal))
        if field is not None:
            matcher.write(pattern)
    return matcher.getvalue()
