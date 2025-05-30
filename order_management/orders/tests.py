from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):
    """
    Test case for the Order model.
    Ensures that the string representation (__str__) method works as expected.
    """

    def test_str_representation(self):
        # Create an Order instance with a sample title and description
        order = Order(title="Test Order", description="Desc")
        
        # Check that the string representation returns the order's title
        self.assertEqual(str(order), "Test Order")
