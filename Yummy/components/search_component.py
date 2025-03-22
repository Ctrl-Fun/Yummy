import reflex as rx
from Yummy.elements.elements import RxButton
import Yummy.styles.styles as styles


def search_component():
    return rx.box(
        rx.hstack(
            rx.input(
                placeholder="Buscar...",
                size=styles.BTN_SIZE,
                style=styles.search_component.input,
            ),
            RxButton(
                "Search",
            ),
            spacing=styles.Size.DEFAULT.value,
            width="100%",
            justify="center"
        ),
        style={
            "display": "flex",
            "justify_content": "center",
            "align_items": "center",
            "width": "100%",
            "max_width": "600px",
            "margin": "1em auto",
        },
    )