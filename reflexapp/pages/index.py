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

class CheckoutProvider(rx.Component):
    # TODO: implement this component
    # https://reflex.dev/docs/wrapping-react/overview/#wrapping-react-overview

    library = "@stripe/react-stripe-js"
    tag = "EmbeddedCheckoutProvider"
    # TODO: figure out how to initialize the stripe prop for EmbeddedCheckoutProvider
    # https://github.com/stripe/react-stripe-js/blob/master/src/components/EmbeddedCheckoutProvider.tsx#L46
    # stripe: rx.Var[]
    clientSecret: rx.Var[
        str
    ] = CheckoutState.client_secret
    is_default = False

    lib_dependencies: list[str] = ["@stripe/stripe-js"]

checkout_provider = CheckoutProvider.create

def checkout_builder() -> rx.Component:
    return rx.vstack(
        checkout_provider()
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
            checkout_builder(),
            align="center"
        )
    )
