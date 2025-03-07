"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import Yummy.styles.styles as styles
from Yummy.styles.global_styles import BASE_STYLES
from Yummy.components.navbar import navbar
from Yummy.components.header import header
from Yummy.components.tv import tv
from Yummy.components.footer import footer
from Yummy.components.season_menu import season_menu
from Yummy.components.episode_view import episode_view
from Yummy.components.recipes_list import recipes_list
import Yummy.styles.fonts as fonts


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                # header(),
                # tv(),
                recipes_list(),
                style=styles.body_style,
                spacing=styles.Size.BIG.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )


app = rx.App()
app.add_page(index)
