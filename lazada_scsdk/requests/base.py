# -*- coding: utf-8 -*-
# @Author: Phu Hoang
# @Date:   2017-02-17 19:29:40
# @Last Modified by:   Phu Hoang
# @Last Modified time: 2017-02-18 09:35:08

from lxml import etree
from lxml.builder import E


class BaseRequest(object):
    def __init__(self):
        self.root = E.Request()
        self._construct()

    def _construct(self):
        pass

    def _create_element(self, tag, **kwargs):
        return etree.Element(tag, **kwargs)

    def tostring(self):
        return etree.tostring(self.root)
