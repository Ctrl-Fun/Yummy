import reflex as rx
from sqlmodel import select

from Yummy.state.base import State, User, UPLOAD_FOLDER, ASSETS_FOLDER


class AuthState(State):
    """Login state"""
    username: str
    password: str
    confirm_password: str

    @rx.event
    async def signup(self, files: list[rx.UploadFile]):
        """Singup a user"""
        imagepath=None
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Las dos contraseñas no son iguales!")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("El usuario ya existe!")
            
            if(files[0]):
                upload_photo = await files[0].read()
                namephoto = files[0].name
                imagepath = ASSETS_FOLDER / UPLOAD_FOLDER / files[0].name

                with imagepath.open("wb") as file_object:
                    file_object.write(upload_photo)

            new_user = User(username=self.username,password=self.password,imagepath=str(imagepath))
            session.add(new_user)
            session.expire_on_commit = False
            session.commit()
            self.user = new_user.id
            self.userPhoto = "/img/uploads/"+str(namephoto)

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