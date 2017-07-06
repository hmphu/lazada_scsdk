# -*- coding: utf-8 -*-
# @Author: Phu Hoang
# @Date:   2017-07-06 09:35:51
# @Last Modified by:   Phu Hoang
# @Last Modified time: 2017-07-06 09:39:33

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))

for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
    mod = __import__('.'.join([__name__, py]), fromlist=[py])
    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        setattr(sys.modules[__name__], cls.__name__, cls)
