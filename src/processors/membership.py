from .base import OrderProcessor


class MembershipProcessor(OrderProcessor):
    def process_order(self, order):
        # Specific rules for memberships
        print(f"Processing membership order: {order}")
        if order.type == "new":
            print("Activating new membership")
        elif order.type == "upgrade":
            print("Applying membership upgrade")
        print("Sending email to owner about activation/upgrade")
