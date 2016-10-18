# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2016 by Pyvisa-I3py-sim Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Action-like method wrapper describing a dialog.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

import re
from string import Formatter
from io import StringIO

from stringparser import Parser
from i3py.core.actions import Action

from .component import NoResponse, NoMatch
from .exceptions import I3pyVisaSimException

_FORMATTER = Formatter()


class Dialog(Action):
    """Method decorator describing an instrument dialog.

    If parameters can be passed to the instrument formatted in the query,
    if will be extracted from the query and passed to the decorated function.
    The function should return a text message or None depending on whether the
    command should lead to an answer.

    Parameters
    ----------
    cmd : unicode or Parser, optional
        String or stringparser.Parser to use to extract the interesting value
        from the instrument answer.

    Other parameters are the ones of Action.

    """
    def __init__(self, cmd, answer_format=None, **kwargs):
        super(Dialog, self).__init__(**kwargs)
        # Passed command.
        self.cmd = cmd
        self.kwargs = {'cmd': cmd}

        # Parser used to extract the arguments of the command.
        self._parser = Parser(cmd)

        # Regular expression used to match the query so that an error in the
        # value does not prevent a match.
        matcher = StringIO()
        for literal, field, fmt, conv in _FORMATTER.parse(cmd):
            matcher.write(re.escape(literal))
            if field is not None:
                matcher.write('\S+')
        self._matcher = re.compile('^' + matcher.getvalue() + '$')


    def match(self, driver, query):
        """Try to match the query and extract the parameters.

        Parameters
        ----------
        query : unicode
            Query on which to try to match the dialog command.

        """
        if self._matcher.match(query):
            try:
                args = self._parser(query)
            except ValueError as e:
                driver.handle_error(e)

            if isinstance(args, list):
                args = args
                kwargs = {}
            elif isinstance(args, dict):
                args = ()
                kwargs = args
            else:
                args = (args,)
                kwargs = {}

            try:
                response = getattr(driver, self.name)(*args, **kwargs)
            except I3pyVisaSimException as e:
                driver.handle_error(e)

            return response or NoResponse
        else:
            return NoMatch

