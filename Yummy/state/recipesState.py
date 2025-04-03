import reflex as rx
from sqlmodel import select

from Yummy.state.base import State
from Yummy.db_model import User, Receta, Ingrediente_Receta, Pasos_Receta, Imagen_Receta, Ingrediente

class RecipesState(State):
    """Homepage state"""

    def get_recipe(self, id):
        return rx.redirect(f"/recipes/{id}")
    

class RecipeSingleState(State):
    """Singlepage state"""
    recipe: Receta | None
    recipeIngredients: list[Ingrediente] | None
    recipeSteps: list[Pasos_Receta] | None
    recipeImages: list[Imagen_Receta] | None

    def load_page(self):
        """Prepare recipe data and check the login user status"""
        if(not self.logged_in):
            return rx.redirect("/login")
        
        data = self.router.page.params
        recipe_id = data.get("recipe_id")
        ingredientRelation =[]

        with rx.session() as session:
            # recipe table data
            self.recipe = session.get(Receta,recipe_id)
            ingredientRelation = session.exec(
                select(Ingrediente_Receta).where(Ingrediente_Receta.id_receta==recipe_id)
            ).all()
            self.recipeSteps = session.exec(
                select(Pasos_Receta).where(Pasos_Receta.id_receta == recipe_id)
            ).all()
            self.recipeImages = session.exec(
                select(Imagen_Receta).where(Pasos_Receta.id_receta == recipe_id)
            ).all()

        ingredient_ids = []
        for relation in ingredientRelation:
            ingredient_ids.append(relation.id_ingrediente)
            
        with rx.session() as session:
            # ingredient table data
            self.recipeIngredients = session.exec(
                select(Ingrediente).where(Ingrediente.id.in_(ingredient_ids))
            ).all()
            
        print(self.recipeIngredients)
        print(self.recipe)