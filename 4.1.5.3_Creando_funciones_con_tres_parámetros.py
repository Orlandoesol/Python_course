def esUnTriangulo(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(esUnTriangulo (1, 1, 1))
print(esUnTriangulo (1, 1, 3))
print("-------------Version Mas compacta-----------")
def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(esUnTriangulo(1, 1, 1))
print(esUnTriangulo(1, 1, 3))
print("-------------Version Mas pidiendo los valores al usuario-----------")
def esUnTriangulo(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True
    
a = int(input("Ingrese el valor del primer lado: "))
b = int(input("Ingrese el valor del segundo lado: "))
c = int(input("Ingrese el valor del tercer lado: "))

print(esUnTriangulo(a, b, c))