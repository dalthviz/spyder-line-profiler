# -*- coding: utf-8 -*-
#
# Copyright © 2022-, Spyder Line Profiler contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""Spyder line-profiler default configuration."""

CONF_SECTION = 'spyder_line_profiler'

CONF_DEFAULTS = [
    (CONF_SECTION,
     {
      'use_colors': True,
     }
     ),
    ('shortcuts',
     {
       'spyder_line_profiler/run_profiler_action': 'Shift+F10',
     }
    )
]

# IMPORTANT NOTES:
# 1. If you want to *change* the default value of a current option, you need to
#    do a MINOR update in config version, e.g. from 1.0.0 to 1.1.0
# 2. If you want to *remove* options that are no longer needed in our codebase,
#    or if you want to *rename* options, then you need to do a MAJOR update in
#    version, e.g. from 1.0.0 to 2.0.0
# 3. You don't need to touch this value if you're just adding a new option
CONF_VERSION = '1.0.0'
