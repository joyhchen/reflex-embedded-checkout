"""The home page of the app."""

from reflexapp import styles
from reflexapp.templates import template
from reflexapp.state import CheckoutState

import reflex as rx

def input_ids() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Price ID",
            value=CheckoutState.price_id,
            on_change=CheckoutState.set_price_id,
        ),
        rx.button(
            "Create session",
            on_click=CheckoutState.create_checkout_session,
        ),
    )

def checkout_container() -> rx.Component:
    return rx.vstack(
        rx.box(id="checkout"),
        rx.script(
            src="https://js.stripe.com/v3/",
        ),
        rx.button("Show checkout", on_click=rx.call_script(
            # TODO: this doesn't work because I haven't figured out async/await in the call_script block.
            # but calling checkout.mount doesn't work until the promise is fulfilled
            f'const stripe = Stripe("{CheckoutState.publishable_key}"); const checkout = stripe.initEmbeddedCheckout({{clientSecret: "{CheckoutState.client_secret}"}});'
        )
        )
    )

@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    return rx.center(
        rx.vstack(
            input_ids(),
            checkout_container(),
            align="center"
        )
    )
