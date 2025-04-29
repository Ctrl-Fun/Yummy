import reflex as rx
from Yummy.elements.elements import RxButton
import Yummy.styles.styles as styles
from Yummy.state.recipesState import RecipesState

def search_component():
    return rx.box(
        rx.hstack(
            rx.input(
                placeholder="Buscar...",
                size=styles.BTN_SIZE,
                style=styles.search_component.input,
            ),
            RxButton(
                "Buscar",
            ),
            RxButton(
                "Añadir Receta",
                on_click=RecipesState.add_recipe
            ),
            spacing=styles.Size.DEFAULT.value,
            width="100%",
            justify="center"
        ),
    )