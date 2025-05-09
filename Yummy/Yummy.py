"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Yummy.pages.login import login
from Yummy.pages.signup import signup
from Yummy.pages.recipes import recipes
from Yummy.pages.single_recipe import single_recipe
from Yummy.pages.add_recipe import add_recipe
from Yummy.state.base import State
from Yummy.state.recipesState import RecipeSingleState, RecipesState, AddRecipe
from Yummy.styles.theme import theme



app = rx.App(
    theme=theme
)
app.add_page(login)
app.add_page(signup)
app.add_page(single_recipe, route="/recipes/[recipe_id]", on_load=RecipeSingleState.load_page)
app.add_page(add_recipe, route="/add_recipe", on_load=AddRecipe.load_page)
app.add_page(recipes, route="/", on_load=RecipesState.load_page)