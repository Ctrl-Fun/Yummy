"""Backend main file"""

import reflex as rx
from Yummy.db_model import User

class State(rx.State):
    """Funcionamiento principal de la app (base state)"""

    user: int | None = None

    def logout(self):
        """Log out a user"""
        self.reset()
        return rx.redirect("/")
    
    def check_login(self):
        """Check if a user is logged in."""
        # print("executing...")
        if not self.logged_in:
            return rx.redirect("/login")
    
    @rx.var
    def logged_in(self) -> bool:
        """Check if a user is logged in."""
        return self.user is not None