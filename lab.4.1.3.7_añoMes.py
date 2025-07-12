""" Tu tarea es escribir y probar una función que toma 
dos argumentos (un año y un mes) y devuelve el número 
de días del mes/año dado 
(mientras que solo febrero es sensible al valor year, 
tu función debería ser universal). """
def isYearLeap(year):
    if year < 1582:
        print("EL añor ",year," esta fuera del periodo del calendario gregoriano.")
    elif year % 4 != 0:
        print("Es un año común")
        return False
    elif year % 100 != 0:
        print("Es un año Bisiesto")
        return True
    elif year % 400 !=0:
        print("Es un año común")
        return False
    else:
        print("Es bisiesto ")
        return True

#year = int(input("Ingrese el año: "))    		
#isYearLeap(year)  

def daysInMonth(year, month):
                #1 , 2, 3, 4, 5, 6, 7, 8, 9,10,11,12
    monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year) and month == 2:
        print("Los dias del mes",month,"son 29 dias.")
        return 29
    print("Los dias del mes",month,"son: ",monthDays[month - 1],"dias.")
    return monthDays[month - 1]


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
daysInMonth(year,month)