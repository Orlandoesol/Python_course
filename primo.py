def isPrime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True
    
"""     if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
num = int(input("Ingrese un numero: "))
print(isPrime(num)) """

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")

print()