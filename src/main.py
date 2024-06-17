import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../processors/')))

from processors.physical_product import PhysicalProductProcessor
from processors.book import BookProcessor
from processors.membership import MembershipProcessor
from processors.video import VideoProcessor

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/')))
from models import Order


def process_order(order_data):
    # Validate order data using pydantic
    try:
        order = Order(**order_data)
        print(f"Order validated: {order}")
    except Exception as e:
        print(f"Order validation error: {e}")
        return

    # Determine the appropriate processor based on product type
    if order.product_type == "physical_product":
        processor = PhysicalProductProcessor()
    elif order.product_type == "book":
        processor = BookProcessor()
    elif order.product_type == "membership":
        processor = MembershipProcessor()
    elif order.product_type == "video":
        processor = VideoProcessor()
    else:
        print("Unsupported product type")
        return

        # Process the order
    processor.process_order(order)


def main():
    # Example orders to process
    orders = [
        {"product_type": "physical_product"},
        {"product_type": "book"},
        {"product_type": "membership", "type": "new"},
        {"product_type": "membership", "type": "upgrade"},
        {"product_type": "video", "product_name": "Learning to Ski"},
    ]

    for order in orders:
        process_order(order)


if __name__ == "__main__":
    main()
