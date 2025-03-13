import reflex as rx
from sqlmodel import select

from Yummy.state.base import State, User

class AuthState(State):
    """Login state"""
    username: str
    password: str
    confirm_password: str

    def signup(self):
        """Singup a user"""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Las dos contraseñas no son iguales!")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("El usuario ya existe!")
            new_user = User(username=self.username,password=self.password,imagepath=None)
            session.add(new_user)
            session.expire_on_commit = False
            session.commit()
            self.user = new_user.id
            return rx.redirect("/")
            

    def login(self):
        """Log in a user"""
        with rx.session() as session:
            user = session.exec(
                User.select().where(
                    User.username.contains(self.username)
                )
            ).first()
            if user and user.password == self.password:
                self.user = user.id
                self.get_user_photo(),
                # State.get_user_photo()
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password")