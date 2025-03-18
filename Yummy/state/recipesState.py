import reflex as rx

from Yummy.state.base import State
from Yummy.db_model import User

class RecipesState(State):
    """Homepage state"""

    # recipe_id: int

    def get_recipe(self, id):
        # self.recipe_id = id
        return rx.redirect(f"/recipes/{id}")
    
    # @rx.var
    # def getUserPhoto(self) -> str | None:
    #     user_photo = None
    #     if self.logged_in:
    #         user_id = self.user.id
    #         if(user_id):
    #             with rx.session() as session:
    #                 user_photo = User.select().where(
    #                     User.id == user_id
    #                 )
    #     return user_photo                

