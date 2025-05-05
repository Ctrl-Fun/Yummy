import reflex as rx
from Yummy.styles import styles
from Yummy.state.recipesState import AddRecipe

def render_selected_ingredient(ingrediente, index:int):
    return rx.hstack(
        rx.text(ingrediente["nombre"]),
        rx.select(
            ingrediente["variantes"],
            placeholder="Variante",
            name=f"variante_ingrediente{index}"
        ),
        rx.input(
            placeholder="Cantidad",
            name=f"cantidad_ingrediente{index}"
        ),
        rx.input(
            placeholder="Unidad(es)",
            name=f"unidad_ingrediente{index}"
        ),
        rx.button("Eliminar", on_click=AddRecipe.remove_item(ingrediente), type="button"),
    )

def render_step(step: str, index:int):
    index = index+1
    return rx.hstack(
        rx.text(f"{index}. {step}"),
        rx.input(style={"display": "none"}, name=f"step{index}", value=step),
        rx.button("Eliminar",on_click=AddRecipe.remove_step(step), type="button")
    )

def render_photo_list(photo: list):
    return rx.hstack(
        rx.foreach(
            photo,
            rx.text
        ),
        rx.button(
            "Eliminar", 
            on_click=AddRecipe.delete_image_preview(photo),
            type="button"
        )
    )

def recipe_form():
    return rx.box(
            rx.form.root(
                 rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Información de la Receta:"
                        ),
                        rx.hstack(
                            rx.input(
                            name="recipe_name",
                            placeholder="Título de Receta",
                            # required=True,
                            size="3"
                            ),
                            rx.select(
                                ["Desayuno","Comida","Cena"],
                                name="recipe_variant",
                                placeholder="Variante",
                                # required=True,
                                size="3"
                            ),
                            spacing=styles.Size.DEFAULT.value
                        ),
                        spacing=styles.Size.DEFAULT.value
                    ),
                    rx.vstack(
                        rx.heading(
                            "Ingredientes:"
                        ),
                        rx.hstack(
                            rx.select(
                                AddRecipe.ingredientes,
                                placeholder="Ingrediente",
                                value=AddRecipe.current_item,
                                on_change=AddRecipe.set_current_item
                            ),
                            rx.button("Agregar", on_click=AddRecipe.add_item, type="button"),
                        ),
                        rx.foreach(
                            AddRecipe.items,
                            lambda ingrediente, index: render_selected_ingredient(ingrediente, index)
                        ),
                        spacing=styles.Size.DEFAULT.value
                    ),
                    rx.vstack(
                        rx.heading("Pasos:"),
                        rx.hstack(
                            rx.input(
                                placeholder="Introduce paso",
                                # name="step",
                                value=AddRecipe.current_step,  # Estado que refleja el valor actual
                                on_change=AddRecipe.set_current_step
                            ),
                            rx.button(
                                "Agregar",
                                on_click=AddRecipe.add_step,
                                type="button"
                            ),
                        ),
                        rx.foreach(
                            AddRecipe.steps,
                            lambda step, index: render_step(step, index),
                        ),
                        spacing=styles.Size.DEFAULT.value
                    ),
                    rx.vstack(
                        rx.heading("Fotos:"),
                        rx.vstack(
                            rx.hstack(
                                rx.upload(
                                    rx.text("Sube una o varias fotos A LA VEZ (INCOMPATIBILIDAD CON NO SIMULTANEIDAD DE REFLEX)"),
                                    accept={"image/png", "image/jpeg"},
                                    max_files=5,
                                    multiple=True,
                                    id="step_photo",
                                    # on
                                ),
                                rx.button(
                                    "Borrar",
                                    on_click=rx.clear_selected_files("step_photo"),
                                    type="button"
                                ),
                            ),
                            rx.foreach(
                                rx.selected_files("step_photo"), 
                                lambda filename: rx.hstack(
                                    rx.text(filename),
                                    rx.input(
                                        placeholder="Nombre",
                                        name="image_name",
                                    ),
                                    rx.select(
                                        AddRecipe.steps,
                                        placeholder="Paso",
                                        name="image_step",
                                    ),
                                )
                            ),
                            rx.text("Nota: posteriormente se puede editar la receta más en detalle")
                        ),
                    ),
                    rx.divider(),
                    rx.button(
                        "Subir",
                        type="submit",
                        # on_click=AddRecipe.handle_submit(rx.upload_files(upload_id="step_photo")),
                        # on_click=AddRecipe.handle_upload(rx.upload_files(upload_id="step_photo")),
                        # disabled=AddRecipe.disabled_upload_button
                    ),
                    spacing=styles.Size.DEFAULT.value,
                ),
                on_submit=AddRecipe.handle_submit(),
            ),
           
    )