import reflex as rx
from enum import Enum
from .colors import Colors, TextColors
######## CONSTANTS
BTN_SIZE = "3"

class TextSizes(Enum):
    SMALL="1"
    DEFAULT="3"
    BIG="5"
    EXTRA_BIG="7"

class Size(Enum):
    NONE = "0"
    EXTRA_SMALL = "1"
    SMALL = "3"
    DEFAULT = "5"
    MEDIUM = "6"
    BIG = "7"

class EMSize(Enum):
    XS = "0.8em"
    S = "1em"
    L = "2em"
    XL= "4em"
    XXL="6em"
    Extra_4="10em"
    Extra_5="15em"

class PercentSice(Enum):
    SMALL = "30%"
    MEDIUM = "50%"
    BIG = "70%"
    EXTRA_BIG = "85%"

spacing_values = [4,8,12,16,24,32,40,48,64]

######## STYLES DESKTOP
## MAIN PAGE
body_style = dict(
    max_width="85%",
    align_items="center",
    margin_y=str(spacing_values[int(Size.DEFAULT.value)])+"px",
)

main_page_style = dict(
    padding_top="68px",
    backgroundColor = Colors.BACKGROUND.value,
    minHeight = "100vh",          # Asegura que el fondo cubra toda la pantalla
)

button = dict(
    color=Colors.PRIMARY.value,
    _disabled={
        "opacity": 0.6,  # Opcional, opacidad para indicar que está deshabilitado
    },
)

navbar_button = dict(
    color=Colors.PRIMARY.value,
    _disabled={
        "opacity": 0.6,  # Opcional, opacidad para indicar que está deshabilitado
    },
)

navbar_button_active = dict(
    color=Colors.PRIMARY.value,
    border= "1px solid",
    _disabled={
        "opacity": 0.6,  # Opcional, opacidad para indicar que está deshabilitado
    },
)

# NAVBAR
class navbar():
    navbar_style = dict(
        bg=Colors.SECONDARY.value,
        padding=EMSize.S,
        position="fixed",
        top="0px",
        z_index="999",
        width="100%",
        heigth=EMSize.XL
    )

    navbar_title_style = dict(
        size="7", 
        weight="bold",
        color=Colors.PRIMARY.value
    )

    navbar_image_style = dict(
        width=EMSize.L,
        height="auto",
    )

    vstack_links_style = dict(
        width="100%",
    )

# FOOTER
class footer():
    text = dict(
        white_space = "nowrap"
    )

    image = dict(
        width = EMSize.XXL.value,
        height = "auto",
    )

    flex_container = dict(
        width="100%",
    )

    vstack_container = dict(
        padding=EMSize.S.value,
    )

    socials_def = dict(
        width="100%",
    )

    social_icon_styles = dict(
        _hover = {
            "color" : Colors.PRIMARY.value
        }
    )

# SEARCH COMPONENT
class search_component():
    input = dict(
        # width=["100%", "80%", "60%"],  # Ancho adaptable
        width="100%"
    )

# HEADER
class header():
    avatar_style = dict(
        margin_left = EMSize.S,
    )



######## STYLES MOBILE