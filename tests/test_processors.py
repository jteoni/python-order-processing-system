import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.processors.physical_product import PhysicalProductProcessor
from src.processors.book import BookProcessor
from src.processors.membership import MembershipProcessor
from src.processors.video import VideoProcessor
from src.models import Order


class TestOrderProcessing(unittest.TestCase):
    def test_physical_product(self):
        # Test case for physical product processing
        order_data = {"product_type": "physical_product"}
        order = Order(**order_data)
        processor = PhysicalProductProcessor()
        processor.process_order(order)

        # Add assertions if needed to verify the processing outcome

    def test_book(self):
        order_data = {"product_type": "book"}
        order = Order(**order_data)

        # Capture stdout to verify printed messages
        from io import StringIO
        import sys
        stdout_orig = sys.stdout
        sys.stdout = StringIO()

        try:
            processor = BookProcessor()
            processor.process_order(order)

            # Check stdout for expected messages
            output = sys.stdout.getvalue().strip()
            self.assertIn("Processing book order:", output)
            self.assertIn("Generating duplicate packing slip for royalties", output)
            self.assertIn("Generating commission payment to agent", output)

            # Add more assertions if needed

        finally:
            sys.stdout = stdout_orig  # Restore original stdout

    def test_membership(self):
        # Test cases for membership processing (new and upgrade)
        order_data = {"product_type": "membership", "type": "new"}
        order = Order(**order_data)
        processor = MembershipProcessor()
        processor.process_order(order)

        # Add assertions if needed to verify the processing outcome

        order_data = {"product_type": "membership", "type": "upgrade"}
        order = Order(**order_data)
        processor.process_order(order)

        # Add assertions if needed to verify the processing outcome

    def test_video(self):
        # Test case for video processing
        order_data = {"product_type": "video", "product_name": "Learning to Ski"}
        order = Order(**order_data)
        processor = VideoProcessor()
        processor.process_order(order)

        # Add assertions if needed to verify the processing outcome


if __name__ == "__main__":
    unittest.main()
