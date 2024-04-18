import os
import reflex as rx
import stripe

stripe.api_key = os.environ["STRIPE_API_KEY"]

class CheckoutState(rx.State):
    """The checkout session state."""

    price_id: str
    client_secret: str = ""

    def create_checkout_session(self):
        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': self.price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            return_url="https://stripe.com", # random placeholder
        )
        self.client_secret = session.client_secret