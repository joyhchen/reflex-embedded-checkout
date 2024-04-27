import os
import reflex as rx
import stripe
import os

class CheckoutState(rx.State):
    customer_email: str
    client_secret: str
    publishable_key: str = os.environ.get('STRIPE_PUBLISHABLE_KEY')
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

    def create_checkout_session(self):
        session = stripe.checkout.Session.create(
            ui_mode = 'embedded',
            line_items=[
                {
                    'price': 'price_1ODMpEGC4ECGOX3CPP8F3fnl', # also hard coded this for demo...
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_email=self.customer_email,
            return_url="https://stripe.com", # random placeholder
        )
        self.client_secret = session.client_secret
