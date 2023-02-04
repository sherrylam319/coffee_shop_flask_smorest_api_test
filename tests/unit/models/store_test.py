

from models import StoreModel
from unittest import TestCase

class StoreTest(TestCase):
    def test_create_store(self):

        test_1 = StoreModel('fanling', 'store_1')

        self.assertEqual(test_1.location, 'fanling',
        "The location of the store after creation does not equal the constructor argument")
        
        self.assertEqual(test_1.product, [],
        "The store's products length was not 0 even though no items were added")

