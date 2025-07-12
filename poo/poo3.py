'''
class <Nombre_clase>():
    def __init__(self, <parametros>):
        # Inicialización de atributos
        self.atributo1 = valor1
        self.atributo2 = valor2

        class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
'''

class User:
    def __init__(self, userName, password, email=None):
        self.userName = userName
        self.email = email
        self.password = password

user1 = User(
    userName="JohnDoe",
    password="123456",
)

user2 = User(
    userName="JaneFonda",
    password="Fj123456",
    email="fondajane@dominio.com"
)


print("***** Usuario 1********")
print(f"Nombre de usuario: {user1.userName}")
print(f"Email: {user1.email}")
print(f"Contraseña: {user1.password}")
