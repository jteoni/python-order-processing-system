from .base import OrderProcessor


class BookProcessor(OrderProcessor):
    def process_order(self, order):
        # Specific rules for books
        print(f"Processing book order: {order}")
        print("Generating duplicate packing slip for royalties")
        print("Generating commission payment to agent")
