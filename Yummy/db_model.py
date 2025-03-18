import reflex as rx

class User(rx.Model, table=True):
    """Users table definition"""
    username: str
    password: str
    imagepath: str | None

class Ingrediente(rx.Model, table=True):
    """Tabla de ingredientes para las recetas"""
    nombre: str
    variante: str | None