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
    # TODO: figure out how to wrap react-stripe-js embedded checkout
    # https://reflex.dev/docs/wrapping-react/overview/#wrapping-react-overview
    return rx.center(
        rx.vstack(
            rx.text(CheckoutState.client_secret),
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
            checkout_container(),
            align="center"
        )
    )
