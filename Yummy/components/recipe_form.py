import reflex as rx
from Yummy.styles import styles
from Yummy.state.recipesState import AddRecipe
from Yummy.state.recipesState import RecipesState

def render_selected_ingredient(ingrediente):
    return rx.hstack(
        # rx.text(ingrediente),
        rx.text(ingrediente["nombre"]),
        rx.select(
            ingrediente["variantes"],
        ),
        # rx.button("Eliminar", on_click=lambda: AddRecipe.remove_item(ingrediente)),
    )

def recipe_form():
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Información de la Receta:"
                ),
                rx.input(
                    placeholder="Título de Receta",
                    size="3"
                ),
                rx.select(
                    ["Desayuno","Comida","Cena"],
                    placeholder="Variante",
                    size="3"
                ),
                spacing=styles.Size.DEFAULT.value
            ),
            rx.vstack(
                rx.heading(
                    "Ingredientes:"
                ),
                rx.select(
                    AddRecipe.ingredientes,
                    placeholder="Ingrediente",
                    value=AddRecipe.current_item,
                    on_change=AddRecipe.set_current_item
                ),
                rx.button("Agregar", on_click=AddRecipe.add_item),
                rx.foreach(
                    AddRecipe.items,
                    render_selected_ingredient
                ),
                spacing=styles.Size.DEFAULT.value
            ),
            



            spacing=styles.Size.DEFAULT.value,
        ),
    )