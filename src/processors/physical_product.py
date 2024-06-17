from .base import OrderProcessor


class PhysicalProductProcessor(OrderProcessor):
    def process_order(self, order):
        # Specific rules for physical products
        print(f"Processing physical product order: {order}")
        print("Generating packing slip for shipping")
        print("Generating commission payment to agent")
