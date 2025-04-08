import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.footer import footer
from Yummy.styles import styles
from Yummy.state.recipesState import RecipeSingleState

def safe_cell(value: str, fallback: str = "-"):
    return rx.cond(value, rx.table.cell(value), rx.table.cell(fallback))


def render_ingredients(ingrediente: dict[str,str]):
    return rx.table.row(
        safe_cell(ingrediente["nombre"]),
        safe_cell(ingrediente["variante"]),
        safe_cell(ingrediente["cantidad"]),
        safe_cell(ingrediente["unidad"]),
    )


def single_recipe():
    # Welcome Page 
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(RecipeSingleState.recipe.nombre),

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