#Herencia multiple

class ClaseA:
    def say_hello(self):
        print("Hola, soy Clase A")

class ClaseB:
    def say_hello(self):
        print("Hola, soy Clase B")

    def say_goodbye(self):
        print("Adiós!!!")

class ClaseC(ClaseB, ClaseA):
    def say_hello(self):
        super().say_hello()
        print("Hola, soy Clase C")

c = ClaseC()
c.say_hello()
c.say_goodbye()