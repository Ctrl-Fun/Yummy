import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.footer import footer
from Yummy.components.recipe_form import recipe_form
from Yummy.styles import styles

def add_recipe():
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                recipe_form(),
                style=styles.body_style,
                spacing=styles.Size.DEFAULT.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )