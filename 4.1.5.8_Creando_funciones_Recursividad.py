""" def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10):
    print(n, "->", fib(n))
 """

print("\n------otro ejemplo---------\n")
n1 = int(input("Ingrese un valor entero: "))
def factorialFun(n1):
    if n1 == 1:    # la condición de terminación
        return 1
    else:
        return n1 * factorialFun(n1 - 1)

print(factorialFun(n1)) # 4 * 3 * 2 * 1 = 24
    