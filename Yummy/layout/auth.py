"""Shared auth layout."""

import reflex as rx
from Yummy.styles import styles

def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
            rx.center(
                rx.vstack(
                    rx.heading("Bienvenido a Yummy", size="8"),
                    rx.heading("Inicia sesión o registrate para comenzar", size="8"),
                    rx.text(
                        "Revisa el código de la aplicación ",
                        rx.link(
                            "aquí",
                            href="https://github.com/reflex-dev/reflex-examples/tree/main/twitter",
                        ),
                        ".",
                        color="gray",
                        font_weight="medium",
                    ),
                    *args,
                    style=styles.body_style,
                ),
                
                # border_top_radius="10px",
                # box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
                # display="flex",
                # flex_direction="column",
                # align_items="center",
                # padding_top="36px",
                # padding_bottom="24px",
                spacing=styles.Size.DEFAULT.value,
                style=styles.main_page_style
            )
        )
