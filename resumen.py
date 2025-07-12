print("Ejercicio 1")
for i in range(1,11):
    #imprime pares
    #if i % 2 == 0:
    #imprime impares
    if i % 2 == 1:
        print(i)
print("*************\nEjercicio 2\n*************")
x = 1
while x < 11:
    if x % 2 == 1:
        print(x)
    x += 1

print("*************\nEjercicio 3\n*************")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

print("\n*************\nEjercicio 4\n*************")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

print("\n*************\nEjercicio 5\n*************")
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

print("\n*************\nEjercicio 6\n*************")
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

print("\n*************\nEjercicio 7\n*************")
for i in range(0, 6, 3):
    print(i)
