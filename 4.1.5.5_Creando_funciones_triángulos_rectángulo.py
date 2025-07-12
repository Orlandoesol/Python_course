def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(a, b, c ** .5))
#print(campoTriangulo(1., 1., 2. ** .5))

