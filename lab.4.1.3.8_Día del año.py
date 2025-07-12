def isYearLeap(year):
    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True

def daysInMonth(year, month):
                # 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

def dayOfYear(year, month, day):
    #validar las entradas
    if year < 1582:
        return None
    if month > 12 or month < 1:
        return None
    if day > 31 or day < 1:
        return None

    #Calcular los dias
    totalDays = day
    month = month - 1
    while month > 0:
        totalDays += daysInMonth(year,month)
        month -= 1

    return totalDays
year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
day = int(input("Ingrese el dia: "))

print(dayOfYear(year, month, day))
