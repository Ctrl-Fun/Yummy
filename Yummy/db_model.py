import reflex as rx

class User(rx.Model, table=True):
    """Users table definition"""
    username: str
    email: str
    password: str