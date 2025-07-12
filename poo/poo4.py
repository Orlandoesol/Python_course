#Metodos, son las acciones o tareas que puede realizar un objeto
#Atributos, son las caracteristicas de un objeto

class User:
    #def __init__(self, userName="", email="", password=""):
    def __init__(self, userName, password, email=None):
        self.userName = userName
        self.password = password        
        self.email = email

    def saludo(self):
        #print("Hola, soy el usuario", self.userName)
        print(f"Hola, usuario: {self.userName}; ha iniciado sesión..")

    def login(self, userName, password):
        if self.userName == userName and self.password == password:
            self.saludo()
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False
            

user1 = User(
    userName="JohnDoe",
    password="123456",
)

if user1.login("JohnDoe", "123456"):
    user1.saludo()