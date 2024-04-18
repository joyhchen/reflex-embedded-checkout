"""The home page of the app."""

from reflexapp import styles
from reflexapp.templates import template
from reflexapp.state import CheckoutState

import reflex as rx

def input_ids() -> rx.Component:
    return rx.hstack(
        rx.input(
                placeholder="Customer ID",
                value=CheckoutState.customer_id,
                on_change=CheckoutState.set_customer_id,
            ),
            rx.input(
                placeholder="Price ID",
                value=CheckoutState.price_id,
                on_change=CheckoutState.set_price_id,
            ),
            rx.button(
                "Create session",
                on_click=CheckoutState.placeholder_action,
            ),
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
            rx.text('hi'),
            align="center"
        )
    )
