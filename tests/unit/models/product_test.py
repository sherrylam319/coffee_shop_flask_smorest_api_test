from models import ProductModel
from unittest import TestCase

class ProductTest(TestCase):
    def test_create_product(self):
        test_1 = ProductModel('coffee', 15.6, 3)

        self.assertEqual(test_1.name, "coffee")
        self.assertEqual(test_1.price, 15.6)
        self.assertEqual(test_1.store_id, 3)
        self.assertEqual(test_1.store, None)