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
    ingredientsList: list[dict[str,str]]
    recipeSteps: list[Pasos_Receta]
    recipeImages: list[Imagen_Receta]

    def load_page(self):
        """Prepare recipe data and check the login user status"""
        self.ingredientsList = []
        ingredientRelation =[]

        if(not self.logged_in):
            return rx.redirect("/login")
        
        data = self.router.page.params
        recipe_id = data.get("recipe_id")

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

        for i, rel in enumerate(ingredientRelation):
            ingrediente_item = dict()

            ingrediente = session.get(Ingrediente,rel.id)
            ingrediente_item["nombre"] = ingrediente.nombre
            ingrediente_item["variante"] = ingrediente.variante
            ingrediente_item["cantidad"] = rel.cantidad
            ingrediente_item["unidad"] = rel.unidad
            self.ingredientsList.append(ingrediente_item)