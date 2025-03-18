import reflex as rx
import Yummy.styles.styles as styles
from Yummy.styles.colors import Colors,TextColors
from rxconfig import config
from Yummy.elements.elements import RxLink, RxText

def social_link(icon: str, href: str) -> rx.Component:
    return RxLink(
        rx.icon(
            icon,
            style=styles.footer.social_icon_styles,
            color=TextColors.BODY,
        ),
        href=href,
    )


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", config.github),
        spacing=styles.Size.SMALL.value,
        justify="end",
        style=styles.footer.socials_def
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.flex(
                rx.hstack(
                    RxText(
                        "Powered by",
                        color = TextColors.BODY,
                        style=styles.footer.text,
                    ),
                    rx.image(   
                        src = "/img/reflex.svg",
                        style=styles.footer.image,
                    ),
                    spacing=styles.Size.SMALL.value,
                    align='center'
                ),
                socials(),
                style=styles.footer.flex_container,
                justify='between',
            ),
        ),
        style=styles.footer.vstack_container,
    )