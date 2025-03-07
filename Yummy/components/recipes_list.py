import reflex as rx
import Yummy.styles.styles as styles


def recipes_list():
    return rx.flex(
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        rx.card(
            rx.hstack(
                rx.image("/img/lisa-feliz.jpg"),
                rx.vstack(
                    rx.heading("titulo de receta"),
                    rx.text("texto de receta"),
                ),
                spacing=styles.Size.DEFAULT.value,
            ),
        ),
        spacing=styles.Size.BIG.value,
        direction="column",
    )