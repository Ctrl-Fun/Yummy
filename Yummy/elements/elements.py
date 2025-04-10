import reflex as rx
import Yummy.styles.styles as styles
from Yummy.state.base import State

def RxGrid(data, columns: str = "3", spacing: str = styles.Size.DEFAULT.value, width: str = "100%", **kwargs) -> rx.Component:
    return rx.grid(
        data,
        columns = columns,
        spacing = spacing,
        width=width,
        **kwargs
    )

def RxLink(data, href: str, is_external: bool = True, **kwargs) -> rx.Component:
    return rx.link(
        data,
        href=href,
        is_external=is_external,
        **kwargs
    )

def RxButton(data, size: str = styles.BTN_SIZE, disabled: bool = False) -> rx.Component:
    return rx.button(
        data,
        size=size,
        background_color=styles.Colors.BUTTON_BACKGROUND,
        disabled=disabled,
        style=styles.button,
    )

def RxButtonHeader(data: str, href: str, size: str = styles.BTN_SIZE, disabled: bool = False) -> rx.Component:
    return rx.button(
        data,
        size=size,
        disabled=disabled,
        background_color=styles.Colors.BUTTON_BACKGROUND_HEADER,
        # on_click=State.set_active_navbar_button(data),
        style=rx.cond(
            State.router.page.path == href,
            styles.navbar_button_active,
            styles.navbar_button
        )
    )


def RxSelect(data, color_scheme: str = "brown", variant: str = "soft", size: str = styles.BTN_SIZE, placeholder: str = "Seleccione...", **kwargs) -> rx.Component:
    return rx.select(
        data,
        color_scheme=color_scheme,
        variant=variant,
        size="3",
        placeholder=placeholder,
        **kwargs
    )

def RxText(data, size: str = styles.TextSizes.DEFAULT.value, **kwargs) -> rx.Component:
    return rx.text(
        data,
        size=size,
        **kwargs
    )