import reflex as rx
from Yummy.components.navbar import navbar
from Yummy.components.footer import footer
from Yummy.styles import styles
from Yummy.state.recipesState import RecipeSingleState

# def render_ingredients(row):
    # rx.console_log(row)
    # pass
    # return rx.hstack(
    #     rx.foreach(
    #         row,
    #         lambda item: rx.box(
    #             item.nombre,
    #         ),
    #     ),
    # )

test = [1,2]

def single_recipe():
    # Welcome Page 
    print(RecipeSingleState.recipeIngredients)
    # for item in RecipeSingleState.recipeIngredients:
    #     print(item)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.text(RecipeSingleState.recipe.id),
                rx.text(RecipeSingleState.recipe.nombre),
                rx.text(RecipeSingleState.recipe.variante),
                rx.text(RecipeSingleState.recipe.creador),
                
                
                
                # rx.text(RecipeSingleState.recipeIngredients),


                rx.heading(f"Receta: {RecipeSingleState.recipe.nombre}"),
                # rx.foreach(RecipeSingleState.recipeIngredients, single_recipe),

                # rx.text(f"Recipe Ingredients: {[ingredient.nombre for ingredient in RecipeSingleState.recipeIngredients]}"),
                # rx.foreach(
                #     RecipeSingleState.recipeIngredients,
                #     lambda ingredient: rx.text(ingredient.nombre)  # Accediendo correctamente al atributo nombre
                # ),
                # rx.foreach(RecipeSingleState.recipeIngredients, render_ingredients),
                # rx.text(RecipeSingleState.recipeIngredients[0].nombre),
                # rx.foreach(
                #         RecipeSingleState.recipeIngredients,
                #         lambda ingredient: rx.text(
                #             f"{ingredient.nombre} ({ingredient.variante})" if ingredient.variante else ingredient.nombre
                #         )
                #     ),
                # rx.text("Ingredientes:"),
                
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
                            # rx.text(RecipeSingleState.recipeIngredients),
                            # rx.foreach(RecipeSingleState.recipeIngredients, lambda ingredient: rx.text(ingredient.nombre)),
                            
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