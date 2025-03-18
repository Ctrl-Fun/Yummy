import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.footer import footer
from Yummy.styles import styles
from Yummy.state.recipesState import RecipesState

def single_recipe():
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading("receta: macarrones con chorizo"),
                rx.text("Ingredientes:"),
                
                rx.hstack(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("Ingrediente"),
                                rx.table.column_header_cell("Tipo"),
                                rx.table.column_header_cell("Cantidad"),
                                rx.table.column_header_cell("unidad")
                            )
                        ),
                        rx.table.body(
                            rx.table.row(
                                rx.table.cell("Tomate"),
                                rx.table.cell("Rallado"),
                                rx.table.cell("500"),
                                rx.table.cell("gramos")
                            ),
                            rx.table.row(
                                rx.table.cell("Ajo"),
                                rx.table.cell("Diente"),
                                rx.table.cell("2"),
                                rx.table.cell("Ud.")
                            ),
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