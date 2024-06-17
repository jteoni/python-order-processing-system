from .base import OrderProcessor


class VideoProcessor(OrderProcessor):
    def process_order(self, order):
        # Specific rules for videos
        print(f"Processing video order: {order}")
        if order.product_name == "Learning to Ski":
            print("Adding free 'First Aid' video to packing slip")
