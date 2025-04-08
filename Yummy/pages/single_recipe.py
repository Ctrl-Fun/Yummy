import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.footer import footer
from Yummy.styles import styles
from Yummy.state.recipesState import RecipeSingleState

def render_ingredients(ingrediente: dict[str,str]):
    return rx.table.row(
                rx.table.cell(ingrediente["nombre"]),
                rx.table.cell(ingrediente["variante"]),
                rx.table.cell(ingrediente["cantidad"]),
                rx.table.cell(ingrediente["unidad"])
            ),

def single_recipe():
    # Welcome Page 
    print(RecipeSingleState.ingredientsList)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(f"Receta: {RecipeSingleState.recipe.nombre}"),

                rx.hstack(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Ingrediente"),
                                rx.table.column_header_cell("Variante/Tipo"),
                                rx.table.column_header_cell("Cantidad"),
                                rx.table.column_header_cell("Unidad Medida")
                            )
                        ),
                        rx.table.body(
                            rx.foreach(RecipeSingleState.ingredientsList, render_ingredients),
                        ),
                    ),
                    rx.hstack(
                        rx.button("+", color_scheme="green"),
                        rx.button("Nuevo Ingrediente", color_scheme="blue"),
                        spacing="1"
                    ),
                ),

                style=styles.body_style,
                spacing=styles.Size.BIG.value
            ),
        ),
        footer(),
        style=styles.main_page_style
    )