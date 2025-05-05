import reflex as rx
from Yummy.styles import styles
from Yummy.state.recipesState import AddRecipe

def render_selected_ingredient(ingrediente):
    return rx.hstack(
        rx.text(ingrediente["nombre"]),
        rx.select(
            ingrediente["variantes"],
            placeholder="Variante",
        ),
        rx.input(
            placeholder="Cantidad",
        ),
        rx.input(
            placeholder="Unidad(es)"
        ),
        rx.button("Eliminar", on_click=AddRecipe.remove_item(ingrediente)),
    )

def render_step(step: str, index:int):
    index = index+1
    return rx.hstack(
        rx.text(f"{index}. {step}"),
        rx.button("Eliminar",on_click=AddRecipe.remove_step(step))
    )

def render_photo_list(photo: list):
    return rx.hstack(
        rx.foreach(
            photo,
            rx.text
        ),
        rx.button(
            "Eliminar", 
            on_click=AddRecipe.delete_image_preview(photo)
        )
    )

def recipe_form():
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    "Información de la Receta:"
                ),
                rx.hstack(
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
                    rx.button("Agregar", on_click=AddRecipe.add_item),
                ),
                rx.foreach(
                    AddRecipe.items,
                    render_selected_ingredient
                ),
                spacing=styles.Size.DEFAULT.value
            ),
            rx.vstack(
                rx.heading("Pasos:"),
                rx.hstack(
                    rx.input(
                        placeholder="Introduce paso",
                        value=AddRecipe.current_step,  # Estado que refleja el valor actual
                        on_change=AddRecipe.set_current_step
                    ),
                    rx.button(
                        "Agregar",
                        on_click=AddRecipe.add_step
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
                rx.hstack(
                    # rx.cond(

                        # AddRecipe.show_upload,
                rx.upload(
                    rx.text("Sube una foto"),
                    accept={"image/png", "image/jpeg"},
                    max_files=5,
                    multiple=True,
                    id="step_photo",
                ),
                        # rx.box()  # Elemento vacío si está oculto
                    # ),
                    rx.vstack(
                        # rx.hstack(
                        #     rx.select(
                        #         AddRecipe.steps,
                        #         placeholder="Paso",
                        #         value=AddRecipe.current_photo_step,
                        #         on_change=AddRecipe.set_current_photo_step,
                        #     ),
                        #     rx.input(
                        #         placeholder="Nombre",
                        #         value=AddRecipe.current_photo_name,  # Estado que refleja el valor actual
                        #         on_change=AddRecipe.set_current_photo_name
                        #     ),
                        #     rx.button(
                        #         "Agregar",
                        #         on_click=AddRecipe.step_image_preview(rx.selected_files("step_photo")),
                        #     ),
                        # ),
                        # rx.vstack(
                        #     rx.foreach(
                        #         AddRecipe.photos, render_photo_list
                        #     )
                        # ),
                        rx.vstack(
                            rx.foreach(
                                rx.selected_files("step_photo"), 
                                lambda filename: rx.hstack(
                                    rx.text(filename),
                                    # rx.text(AddRecipe.photo_step),
                                    # rx.text(AddRecipe.photo_name),
                                    rx.input(placeholder="Nombre"),
                                    rx.select(
                                        AddRecipe.steps,
                                        placeholder="Paso",
                                        # value=AddRecipe.current_photo_step,
                                        # on_change=AddRecipe.set_current_photo_step,
                                    ),
                                    rx.button("Borrar"),
                                    # rx.call(AddRecipe.hide_upload),
                                    # AddRecipe.show_upload = False
                                )
                            )
                        ),
                    ),
                   
                ),
            ),
            rx.button(
                "Upload",
                on_click=AddRecipe.handle_upload(rx.upload_files(upload_id="step_photo")),
                disabled=AddRecipe.disabled_upload_button
            ),
            rx.foreach(
                AddRecipe.img,
                lambda img: rx.hstack(
                    rx.image(
                        src=rx.get_upload_url(img)
                    ),
                    rx.button("delete"),
                ),
            ),
            spacing=styles.Size.DEFAULT.value,
        ),
    )