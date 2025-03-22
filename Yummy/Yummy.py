"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Yummy.pages.login import login
from Yummy.pages.signup import signup
from Yummy.pages.recipes import recipes
from Yummy.pages.single_recipe import single_recipe
from Yummy.state.base import State
from Yummy.styles.theme import theme



app = rx.App(
    theme=theme
)
app.add_page(login)
app.add_page(signup)
app.add_page(single_recipe, route="/recipes/[recipe_id]", on_load=State.check_login())
app.add_page(recipes, route="/", on_load=State.check_login())