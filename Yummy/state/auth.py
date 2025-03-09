import reflex as rx
from sqlmodel import select

from base import State, User

class AuthState(State):
    """Login state"""
    username: str
    email: str
    password: str

    def login(self):
        """Log in a user"""
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    User.username.contains(self.name)
                )
            ).first()
            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password")