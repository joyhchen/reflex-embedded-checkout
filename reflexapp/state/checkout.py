import os
import reflex as rx
import stripe

# sorry... I hardcoded api keys to prototype this faster locally
# add your own environment variables
stripe.api_key = 'sk_test_abc123'

class CheckoutState(rx.State):
    customer_email: str
    client_secret: str
    publishable_key: str = "pk_test_abc123"

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
        rx.call_script(
            f'async function initialize() {{ const stripe = Stripe("{self.publishable_key}"); const checkout = await stripe.initEmbeddedCheckout({{clientSecret: "{self.client_secret}"}}); checkout.mount("#checkout")}} initialize()',
        )
