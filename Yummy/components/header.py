import reflex as rx
import Yummy.styles.styles as styles
from Yummy.styles.colors import Colors, TextColors
from rxconfig import config
from Yummy.elements.elements import RxText


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src="/img/lisa-feliz.jpg",
                size="8",
                radius="full",
                style=styles.header.avatar_style,
            ),
            rx.vstack(
                rx.heading(
                    "Bienvenido a Yummy",
                    size=styles.Size.BIG.value,
                    color=styles.TextColors.HEADER
                ),
                rx.text(
                    "Aquí podrás ver todas tus recetas",
                    color = styles.TextColors.BODY
                ),
                # RxText(
                #     "No has fantaseado con poder ver Los Simpsons 24/7?",
                # ),
                spacing=styles.Size.EXTRA_SMALL.value
            ),
            spacing=styles.Size.DEFAULT.value,
            align="center"
        )    
    )
    