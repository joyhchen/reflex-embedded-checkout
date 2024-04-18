from reflexapp import styles
from reflexapp.templates import template
from reflexapp.state import CheckoutState

import reflex as rx

def input_ids() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.input(
                placeholder="Customer email",
                value=CheckoutState.customer_email,
                on_change=CheckoutState.set_customer_email,
            ),
        ),
        # TODO: add an affirmation that the session was created
        # TODO: add python asyncio. ideally 1 button creates the session and loads checkout but this is hacked together :(
        rx.button(
            "Create session",
            on_click=CheckoutState.create_checkout_session,
        ),
    )

def checkout_container() -> rx.Component:
    return rx.vstack(
        rx.box(id="checkout"), # the container to load embedded checkout in
        rx.script(
            src="https://js.stripe.com/v3/", # load Stripe.js v3
        ),
        # button that reveals embedded checkout
        rx.button("Show checkout", on_click=rx.call_script(
            f'async function initialize() {{ const stripe = Stripe("{CheckoutState.publishable_key}"); const checkout = await stripe.initEmbeddedCheckout({{clientSecret: "{CheckoutState.client_secret}"}}); checkout.mount("#checkout")}} initialize()',
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
