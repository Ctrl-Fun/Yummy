"""Backend main file"""

import reflex as rx
from Yummy.db_model import User
import Yummy.styles.styles as styles
from pathlib import Path

ASSETS_FOLDER = Path("assets")
UPLOAD_FOLDER = Path("img/uploads")  # Define la carpeta de destino

class State(rx.State):
    """Funcionamiento principal de la app (base state)"""
    user: int | None = None
    userPhoto: str | None = None

    def logout(self):
        """Log out a user"""
        self.reset()
        return rx.redirect("/")
    
    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")
    
    def update_user_photo(self):
        if self.user:
            with rx.session() as session:
                user = session.exec(
                    User.select().where(
                        User.id == self.user
                    )
                ).first()
                self.userPhoto = user.imagepath

    @rx.var
    def logged_in(self) -> bool:
        """Check if a user is logged in."""
        return self.user is not None