import reflex as rx
import Yummy.styles.styles as styles
from Yummy.state.recipesState import RecipesState


def recipe_card(recipe: dict[str,str]):
    return rx.card(
        rx.hstack(
            rx.image(
                recipe["imagen"],
                width=styles.PercentSice.BIG, 
                height="auto"
                ),
            rx.vstack(
                rx.heading(recipe["nombre"]),
                rx.text(recipe["variante"]),
                rx.text(recipe["creador"]),
            ),
            spacing=styles.Size.DEFAULT.value,
        ),
        on_click=RecipesState.get_recipe(recipe["id"]),
        cursor = "pointer"
    ),

def recipes_list():
    return rx.flex(
        rx.foreach(RecipesState.recipesList, recipe_card),
        spacing=styles.Size.BIG.value,
        direction="column",
    )