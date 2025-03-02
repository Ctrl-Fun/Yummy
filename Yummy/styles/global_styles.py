import reflex as rx
from Yummy.styles.colors import Colors, TextColors
import Yummy.styles.fonts as fonts


BASE_STYLES = {
    "breakpoints": ["520px", "768px", "1024px", "1280px", "1640px"],
    "font_family": fonts.Type.DEFAULT,
    "font_weight": fonts.Weight.LIGHT,
    rx.button: {
        "color": TextColors.BODY.value,
        "cursor": "pointer"
    },
    rx.text: {
        "color": TextColors.BODY.value,
    },
    rx.select: {
        "color" : TextColors.BODY.value,
    },
    rx.link: {
        "color" : Colors.PRIMARY.value,
        "text_decoration" : "none",
        "_hover" : {}
    },
    # rx.heading: {
    #     "color" : TextColors.HEADER.value,
    #     "font_family": fonts.Type.DEFAULT,
    #     "font_weight": fonts.Weight.MEDIUM
    # },
    rx.grid: {
        "width" : "100%"
    }
}