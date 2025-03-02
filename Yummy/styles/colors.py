from enum import Enum
import reflex as rx

class Colors(Enum):
    PRIMARY = "#F7EE7F"  # Rojo suave con un toque terroso
    SECONDARY = "#A54657"  # Granate suave, más equilibrado con el rojo
    BACKGROUND = "#582630"  # Amarillo más oscuro y menos saturado

    BUTTON_BACKGROUND = "#F4A259"  # Naranja más natural y menos saturado
    BUTTON_HOVER = "#E76F51"  # Rojo-anaranjado suave para un buen efecto hover


class TextColors(Enum):
    HEADER = "#F7EE7F"  # Un rojo oscuro para que resalte bien sobre el fondo claro
    BODY = "#F1A66A"  # Rojo oscuro con un tono cálido y suave
    # BLACK = "#2A0A0A"  # Negro con un leve tono rojizo para mantener coherencia