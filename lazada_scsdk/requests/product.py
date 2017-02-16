# -*- coding: utf-8 -*-
# @Author: Phu Hoang
# @Date:   2017-02-17 19:28:13
# @Last Modified by:   Phu Hoang
# @Last Modified time: 2017-02-18 09:58:17

from .base import BaseRequest


class ProductRequest(BaseRequest):
    def _construct(self):
        _product = self._create_element('Product')
        self.root.append(_product)

    def add_sku(self, sellersku, **kwargs):
        _skus = self.root.find('.//Skus')
        if(_skus is None):
            _skus = self._create_element('Skus')
            self.root.find('.//Product').append(_skus)

        _sku = self._create_element('Sku')
        _sellersku = self._create_element('SellerSku')
        _sellersku.text = sellersku

        for key, value in kwargs.items():
            _key = self._create_element(key)
            _key.text = str(value)
            _sku.append(_key)

        _sku.append(_sellersku)
        _skus.append(_sku)
