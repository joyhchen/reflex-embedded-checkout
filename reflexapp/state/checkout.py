import os
import reflex as rx
import stripe

stripe.api_key = os.environ["STRIPE_API_KEY"]

class CheckoutState(rx.State):
    """The checkout session state."""

    customer_id: str
    price_id: str
    checkout_session: str = ""

    def placeholder_action(self):
        print('hello world')

    def create_checkout_session(self):
        try:
            session = stripe.checkout.Session.create(
                ui_mode = 'embedded',
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': price_id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                return_url="https://stripe.com", # random placeholder
            )
        except Exception as e:
            return str(e)
