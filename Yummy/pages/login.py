"""Login page. Uses auth_layout to render UI shared with the sign up page."""

import reflex as rx

from Yummy.layout.auth import auth_layout
from Yummy.state.auth import AuthState


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Username",
                    on_blur=AuthState.set_username,
                    size="3",
                ),
                rx.input(
                    type="password",
                    placeholder="Password",
                    on_blur=AuthState.set_password,
                    size="3",
                ),
                rx.button("Log in", on_click=AuthState.login, size="3", width="5em"),
                spacing="4",
            ),
        ),
        rx.text(
            "No tienes cuenta aún? ",
            rx.link("Registrate aquí.", href="/signup"),
            color="gray",
        ),
    )
