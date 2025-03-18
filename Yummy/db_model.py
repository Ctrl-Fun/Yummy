import reflex as rx

class User(rx.Model, table=True):
    """Users table definition"""
    username: str
    password: str
    imagepath: str | None

class Receta(rx.Model, table=True):
    """Tabla de recetas"""
    nombre: str
    variante: str
    creador: str

class Ingrediente(rx.Model, table=True):
    """Tabla de ingredientes para las recetas"""
    nombre: str
    variante: str | None

class Ingrediente_Receta(rx.Model, table = True):
    """Relacion entre recetas e ingredientes"""
    id_receta: int
    id_ingrediente: int
    cantidad: int
    unidad: str

class Pasos_Receta(rx.Model, table=True):
    """Tabla de pasos para las recetas"""
    id_receta: int
    numero_paso: int
    descripcion: str

class Imagen_Receta(rx.Model, table=True):
    """Tabla de imagenes para las recetas"""
    id_receta: int
    id_paso: int
    image_path: str
    descripcion: str