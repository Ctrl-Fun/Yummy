import reflex as rx
import Yummy.styles.styles as styles
from Yummy.styles.colors import Colors, TextColors
from rxconfig import config
from Yummy.elements.elements import RxButton, RxSelect, RxText

def tv() -> rx.Component:
    return rx.box(
        rx.mobile_and_tablet(
            rx.vstack(
                rx.video(
                    url="/video/test.mp4",
                    width="100%",
                    height="auto",
                ),
                RxText(
                    "Puedes seleccionar otro capítulo para reproducir:",
                    color=TextColors.HEADER.value,
                    weight="medium",
                    size=styles.Size.DEFAULT.value,
                ),
                RxText("Descripcion del capítulo..."),
                rx.flex(
                    RxSelect(["Temporada 1", "Temporada 2", "Temporada 3", "Temporada 4", "Temporada 5"],
                        placeholder="Temporada"
                    ),
                    RxSelect(["Episodio 1", "Episodio 2", "Episodio 3", "Episodio 4", "Episodio 5"],
                        placeholder="Capitulo"
                    ),
                    RxButton(
                        "Reproducir",
                    ),
                    spacing=styles.Size.SMALL.value,
                    style=styles.tv.flex,
                ),
                spacing=styles.Size.SMALL.value,
                style=styles.tv.vstack_style
            )

        ),
        rx.desktop_only(
            rx.hstack(
                rx.video(
                    url="/video/test.mp4",
                ),
                rx.vstack(
                    RxText(
                        "Puedes seleccionar otro capítulo para reproducir:",
                        color=TextColors.HEADER.value,
                        weight="medium",
                        size=styles.Size.DEFAULT.value,
                    ),
                    rx.hstack(
                        RxSelect(["Temporada 1", "Temporada 2", "Temporada 3", "Temporada 4", "Temporada 5"],
                            placeholder="Temporada"
                        ),
                        RxSelect(["Episodio 1", "Episodio 2", "Episodio 3", "Episodio 4", "Episodio 5"],
                            placeholder="Capitulo"
                        ),
                        RxButton(
                            "Reproducir",
                        ),
                        align="center"
                    ),
                    RxText("Descripcion del capítulo..."),
                    spacing=styles.Size.SMALL.value,
                    style=styles.tv.vstack_style
                ),  
                style=styles.tv.hstack_container_style
            ),
        ),      
    )