kilometros = 12.25
millas = 7.38
unidad_de_conversion = 1.61

millas_a_kilometros = millas * unidad_de_conversion
kilometros_a_millas = kilometros / unidad_de_conversion

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

#2.6.1.8 How to talk to a computer: string operators

print("--------Calcular la hipotenusa------")
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)