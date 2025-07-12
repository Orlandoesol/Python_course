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

year = int(input("Ingrese el año: "))
    		
isYearLeap(year)   		

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"-> ",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
