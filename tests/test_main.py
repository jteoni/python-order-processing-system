import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.main import process_order  # Import process_order from the main module


class TestMainProcessOrder(unittest.TestCase):
    def test_process_order(self):
        orders = [
            {"product_type": "physical_product"},
            {"product_type": "book"},
            {"product_type": "membership", "type": "new"},
            {"product_type": "membership", "type": "upgrade"},
            {"product_type": "video", "product_name": "Learning to Ski"},
        ]

        for order_data in orders:
            process_order(order_data)


if __name__ == "__main__":
    unittest.main()
