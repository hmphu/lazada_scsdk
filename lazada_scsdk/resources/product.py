from .base import Resource
from lazada_scsdk.requests import ProductRequest


class Product(Resource):
    def __init__(self, client=None):
        self.client = client

    def fetch_all(self, **kwargs):
        """"
        Fetch all Product entities
        """
        # if 'Filter' not in kwargs:
        #     kwargs['Filter'] = 'live'

        response = self.get_url('GetProducts', **kwargs)
        if not response:
            return None

        products = response['SuccessResponse']['Body']['Products']
        if not products:
            return None
        return products

    def fetch(self, seller_sku, **kwargs):
        """"
        Fetch Product for given selelr sku
        """
        kwargs['SkuSellerList'] = '["' + seller_sku + '"]'
        products = self.fetch_all(**kwargs)
        if not products:
            return self.search_by_seller_sku(seller_sku)
        return products[0]

    def search_by_seller_sku(self, seller_sku, **kwargs):
        """"
        Searcg Product by given seller sku
        """
        kwargs['Search'] = self.no_accent_vietnamese(seller_sku)
        products = self.fetch_all(**kwargs)
        if not products:
            return None

        for product in products:
            if product['Skus']:
                for sku in product['Skus']:
                    if sku['SellerSku'].upper().strip() == seller_sku.upper().strip():
                        return product
            else:
                if product['SellerSku'].upper().strip() == seller_sku.upper().strip():
                    return product

        return None

    def create(self, data, **kwargs):
        """"
        Create Product from given dict

        Args:
            data : Dictionary having keys using which invoice have to be created

        Returns:
            Product Dict which was created
        """
        return self.post_url('CreateProduct', data, **kwargs)

    def update(self, data, **kwargs):
        """"
        Create Product from given dict

        Args:
            data : Dictionary having keys using which invoice have to be created

        Returns:
            Product Dict which was created
        """
        return self.post_url('UpdateProduct', data, **kwargs)

    def updatepricequantity(self, seller_sku, price=None, qty=None, **kwargs):
        productrequest = ProductRequest()
        sku_data = {}
        if price is not None:
            sku_data['SalePrice'] = price
        if qty is not None:
            sku_data['Quantity'] = qty

        if sku_data:
            productrequest.add_sku(seller_sku, **sku_data)
        else:
            productrequest.add_sku(seller_sku)

        return self.post_url('UpdatePriceQuantity', productrequest.tostring(), **kwargs)
