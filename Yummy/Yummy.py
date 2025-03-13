"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Yummy.pages.login import login
from Yummy.pages.signup import signup
from Yummy.pages.recipes import recipes
from Yummy.state.base import State



app = rx.App()
app.add_page(login)
app.add_page(signup)
app.add_page(recipes, route="/", on_load=State.check_login())