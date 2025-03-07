import reflex as rx
from Yummy.elements.elements import RxButton
import Yummy.styles.styles as styles


def search_component():
    return rx.box(
        rx.hstack(
            rx.input(
                placeholder="Buscar...",
                size=styles.BTN_SIZE,
                style={
                    "width": ["100%", "80%", "60%"],  # Se ajusta en móviles, tablets y escritorio
                    # "padding": "0.5em",
                    # "border": "1px solid #ccc",
                    # "border_radius": "8px",
                    # "outline": "none",
                },
            ),
            RxButton(
                "Search",
                # variant="surface",
                style=styles.navbar.navbar_button,
            ),
            spacing=styles.Size.DEFAULT.value,
            width="100%",
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