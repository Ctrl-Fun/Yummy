import reflex as rx
from sqlmodel import select

from Yummy.state.base import State, User

class AuthState(State):
    """Login state"""
    username: str
    password: str

    def login(self):
        """Log in a user"""
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    User.username.contains(self.username)
                )
            ).first()
            if user and user.password == self.password:
                # print(type(user))
                self.user = user.id
                # print(user.id)
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password")