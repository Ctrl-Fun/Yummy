import reflex as rx
import Yummy.styles.styles as styles
from Yummy.elements.elements import RxGrid, RxText

def episode_view()->rx.Component:
    return rx.box(
        rx.mobile_only(
            RxGrid(
                rx.foreach(
                    rx.Var.range(6),
                    lambda i: rx.card(
                        rx.vstack(
                            rx.image(
                                src="/img/lisa-feliz.jpg", 
                                style=styles.episode_view.header_image_style
                            ),
                            rx.vstack(
                                rx.heading(
                                    f"Chapter {i + 1}",
                                    size=styles.TextSizes.BIG.value
                                ),
                                RxText(
                                    "En este capítulo, exploraremos los fundamentos de la programación, incluyendo los conceptos básicos de variables, estructuras de control y tipos de datos. Al finalizar, estarás listo para escribir tus primeros programas en Python.",
                                    max_width = styles.EMSize.Extra_5.value,
                                    )
                            ),
                        )
                    ),
                ),
                spacing=styles.Size.MEDIUM.value,
                columns="1"
            ),           
        ),
        rx.tablet_and_desktop(
            rx.flex(
                rx.foreach(
                    rx.Var.range(6),
                    lambda i: rx.card(
                        rx.hstack(
                            rx.image(
                                src="/img/lisa-feliz.jpg", 
                                style=styles.episode_view.header_image_style
                            ),
                            rx.vstack(
                                rx.heading(
                                    f"Chapter {i + 1}",
                                    size=styles.TextSizes.BIG.value
                                ),
                                RxText(
                                    "En este capítulo, exploraremos los fundamentos de la programación, incluyendo los conceptos básicos de variables, estructuras de control y tipos de datos. Al finalizar, estarás listo para escribir tus primeros programas en Python.",
                                    max_width = styles.EMSize.Extra_5.value,
                                    )
                            )
                            
                        )
                    ),
                ),
                spacing=styles.Size.MEDIUM.value,
                style=styles.episode_view.flex,
            ),
        )
        
    )