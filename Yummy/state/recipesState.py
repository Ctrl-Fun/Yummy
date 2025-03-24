import reflex as rx

from Yummy.state.base import State
from Yummy.db_model import User
from Yummy.db_model import Receta

class RecipesState(State):
    """Homepage state"""

    def get_recipe(self, id):
        # self.recipe_id = id
        return rx.redirect(f"/recipes/{id}")
    

class RecipeSingleState(State):
    """Singlepage state"""
    recipe: Receta | None

    def load_page(self):

        if(not self.logged_in):
            return rx.redirect("/login")
        
        data = self.router.page.params
        recipe_id = data.get("recipe_id")

        with rx.session() as session:
            self.recipe = session.get(Receta,recipe_id)