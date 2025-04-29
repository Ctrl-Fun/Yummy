import reflex as rx
from sqlmodel import select, desc

from Yummy.state.base import State
from Yummy.db_model import User, Receta, Ingrediente_Receta, Pasos_Receta, Imagen_Receta, Ingrediente
import sqlalchemy

class RecipesState(State):
    """Homepage state"""
    recipesList: list[dict[str,str]]
    allRecipes: list[Receta]

    def load_page(self):
        self.recipesList = []

        if(not self.logged_in):
            return rx.redirect("/login")
        
        with rx.session() as session:
            self.allRecipes = session.exec(select(Receta)).all()

        for i, recipe in enumerate(self.allRecipes):
            recipe_item = dict()

            with rx.session() as session:
                recipe_img = session.exec(
                    select(Imagen_Receta)
                    .where(Imagen_Receta.id_receta == recipe.id)
                    .order_by(desc(Imagen_Receta.id_paso))
                    .limit(1)
                ).first()

            recipe_item["id"] = recipe.id
            recipe_item["nombre"] = recipe.nombre
            recipe_item["variante"] = recipe.variante
            recipe_item["creador"] = recipe.creador
            if(recipe_img):
                recipe_item["imagen"] = recipe_img.image_path
            else:
                recipe_item["imagen"] = None
            self.recipesList.append(recipe_item)

    def get_recipe(self, id):
        return rx.redirect(f"/recipes/{id}")
    
    def add_recipe(self):
        return rx.redirect("/add_recipe")
    

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
                select(Imagen_Receta).where(Imagen_Receta.id_receta == recipe_id)
            ).all()

        for i, rel in enumerate(ingredientRelation):
            ingrediente_item = dict()

            ingrediente = session.get(Ingrediente,rel.id)
            ingrediente_item["nombre"] = ingrediente.nombre
            ingrediente_item["variante"] = ingrediente.variante
            ingrediente_item["cantidad"] = rel.cantidad
            ingrediente_item["unidad"] = rel.unidad
            self.ingredientsList.append(ingrediente_item)

        # print(self.ingredientsList)


class AddRecipe(State):
    # Lista de elementos seleccionados/agregados
    items: list[dict[str, list[str]]]  = []
    
    # Elemento actual seleccionado o escrito
    current_item: str = ""

    # ingredientes: list[dict[str,list]]
    ingredientes: list[str]

    def load_page(self):

        if(not self.logged_in):
            return rx.redirect("/login")
        
        with rx.session() as session:
            # recipe table data
            # result = session.exec(select(Ingrediente)).all()
            result = session.exec(
                sqlalchemy.text(
                    """
                        SELECT DISTINCT nombre
                        FROM ingrediente;

                    """
                )
            ).all()

        self.ingredientes = [item[0] for item in result]



    def add_item(self):
        # if self.current_item and self.current_item not in self.items:
        with rx.session() as session:
            result = session.exec(
                select(Ingrediente.variante).where(
                    Ingrediente.nombre.contains(self.current_item)
                )
            ).all()

        variantes = [item if item is not None else "-" for item in result]
        ingrediente = {
            "nombre": self.current_item,
            "variantes": variantes
        }

        self.items.append(ingrediente)
        print(self.items)
    
    def remove_item(self, item: str):
        self.items = [i for i in self.items if i != item]
