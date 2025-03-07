import reflex as rx
import Yummy.styles.styles as styles
from Yummy.styles.colors import Colors, TextColors
from rxconfig import config
from Yummy.elements.elements import RxButton, RxLink


def navbar_link(text: str, url: str, disabled: bool = False) -> rx.Component:
    return RxLink(
        RxButton(
            text,
            variant="surface",
            disabled = disabled,
            style=styles.navbar.navbar_button,
        ),
        href=url,
        is_external=False
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/cooking.png",
                        style=styles.navbar.navbar_image_style
                    ),
                    rx.heading(
                        config.app_name,
                        style=styles.navbar.navbar_title_style
                    ),
                    align="center",
                ),
                rx.hstack(
                    navbar_link("Recetas", "/#", disabled=True),
                    navbar_link("Menu", "/#"),
                    navbar_link("Lista de la Compra", "/#"),

                    spacing=styles.Size.DEFAULT.value,
                    justify="center",
                    style=styles.navbar.vstack_links_style,
                ),
                align="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/cooking.png",
                        style=styles.navbar.navbar_image_style
                    ),
                    rx.heading(
                        config.app_name,
                        style=styles.navbar.navbar_title_style
                    ),
                    align="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Recetas"),
                        rx.menu.item("Menu"),
                        rx.menu.item("Lista de la Compra"),
                        color_scheme="brown",
                        variant="soft"
                    ),
                    justify="end",
                ),
                justify="between",
                align="center",
            ),
        ),
        style=styles.navbar.navbar_style,
    )