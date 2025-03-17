"""Sign up page. Uses auth_layout to render UI shared with the login page."""

import reflex as rx
from Yummy.layout.auth import auth_layout
from Yummy.state.auth import AuthState


def signup():
    """The sign up page."""
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
                rx.input(
                    type="password",
                    placeholder="Confirm password",
                    on_blur=AuthState.set_confirm_password,
                    size="3",
                ),
                
                rx.hstack(
                    rx.upload(
                        accept={"image/png","image/jpeg"},
                        max_files=1,
                        multiple=False,
                        id="user_photo",                    
                    ),
                    rx.foreach(
                        rx.selected_files("user_photo"), rx.text
                    ),
                    rx.button(
                        "Clear",
                        on_click=rx.clear_selected_files("user_photo"),
                    ),
                ),
                rx.button(
                    "Sign up",
                    on_click=AuthState.signup(rx.upload_files(upload_id="user_photo")),
                    size="3",
                    width="6em",
                ),
                spacing="4",
            ),
            align_items="left",
            background="white",
            border="1px solid #eaeaea",
            padding="16px",
            width="400px",
            border_radius="8px",
        ),
        rx.text(
            "Already have an account? ",
            rx.link("Sign in here.", href="/"),
            color="gray",
        ),
    )
