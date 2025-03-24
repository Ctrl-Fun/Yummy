import reflex as rx
from sqlmodel import select

from Yummy.state.base import State
from Yummy.db_model import User, Receta, Ingrediente_Receta, Pasos_Receta, Imagen_Receta

class RecipesState(State):
    """Homepage state"""

    def get_recipe(self, id):
        return rx.redirect(f"/recipes/{id}")
    

class RecipeSingleState(State):
    """Singlepage state"""
    recipe: Receta | None
    recipeIngredients: list[Ingrediente_Receta] | None
    recipeSteps: list[Pasos_Receta] | None
    recipeImages: list[Imagen_Receta] | None

    def load_page(self):

        if(not self.logged_in):
            return rx.redirect("/login")
        
        data = self.router.page.params
        recipe_id = data.get("recipe_id")

        with rx.session() as session:
            self.recipe = session.get(Receta,recipe_id)
            self.recipeIngredients = session.exec(
                select(Ingrediente_Receta).where(Ingrediente_Receta.id_receta==recipe_id)
            ).all()
            self.recipeSteps = session.exec(
                select(Pasos_Receta).where(Pasos_Receta.id_receta == recipe_id)
            ).all()
            self.recipeImages = session.exec(
                select(Imagen_Receta).where(Pasos_Receta.id_receta == recipe_id)
            ).all()

