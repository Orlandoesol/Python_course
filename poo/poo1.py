'''
Etructura de una clase en Python
=====================================

class <Nombre_clase>():

<variable> = <Nombre_clase>()

'''

class User():
    userName = ""
    email = ""
    password = ""

user1 = User()
user1.userName = "JohnDoe"
user1.email = "jhondoe@dominio.com"
user1.password = "123456"

print(f"Nombre de usuario: {user1.userName}")
print(f"Email: {user1.email}")
print(f"Contraseña: {user1.password}")


