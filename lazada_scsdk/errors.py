# -*- coding: utf-8 -*-
# @Author: Phu Hoang
# @Date:   2017-02-17 14:43:56
# @Last Modified by:   Phu Hoang
# @Last Modified time: 2017-02-17 14:50:21


class BaseError(Exception):
    def __init__(self, code=None, message=None, *args, **kwargs):
        super(BaseError, self).__init__(message)
