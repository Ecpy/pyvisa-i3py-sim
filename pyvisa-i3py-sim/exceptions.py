# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2016 by Pyvisa-I3py-sim Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Specific exceptions for simulated instruments.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)


class I3pyVisaSimException(Exception):
    """Base exceptions for all package specific exceptions.

    """
    pass
    # XXX need to define interface used by error handling mechanism
