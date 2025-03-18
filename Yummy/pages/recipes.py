import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.search_component import search_component
from Yummy.components.recipes_list import recipes_list
from Yummy.components.footer import footer
from Yummy.styles import styles

def recipes():
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                search_component(),
                recipes_list(),
                style=styles.body_style,
                spacing=styles.Size.DEFAULT.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )