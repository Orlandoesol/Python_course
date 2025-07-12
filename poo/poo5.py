#Herencia

class User:
    #def __init__(self, userName="", email="", password=""):
    def __init__(self, userName, password, email=None):
        self.userName = userName
        self.password = password        
        self.email = email

    def saludo(self):
        #print("Hola, soy el usuario", self.userName)
        print(f"Hola, usuario: {self.userName}; ha iniciado sesión!.")

    def login(self, userName, password):
        if self.userName == userName and self.password == password:
            self.saludo()
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
        
class Admin(User):
    def __init__(self, userName, password):
        super().__init__(userName, password)
        self.adminPrivileges = True

class manageUser(User):
    def __init__(self, userName, password):
        super().__init__(userName, password)
        self.managePrivileges = True

admin = Admin("AdminUser","AdminPassword")
manage = manageUser("ManageUser", "ManagePassword")

print("***** Admin ********")
print(f"Nombre de usuario: {admin.userName}")
print(f"Contraseña: {admin.password}")
print(f"Privilegios de administrador: {admin.adminPrivileges}")
print("\n***** Manage User ********")
print(f"Nombre de usuario: {manage.userName}")

print(f"Contraseña: {manage.password}")
print(f"Privilegios de gestión: {manage.managePrivileges}")
