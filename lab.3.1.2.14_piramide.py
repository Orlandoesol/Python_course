#Piramide de bloques
bloques = int(input("Ingrese el número de bloques:"))


#
# Escribe tu código aquí.
#
indice = 1
altura = 0
base = 0
while bloques > 0:
    if base >= 0:
        base = bloques - indice
        bloques = base
        indice += 1
        if bloques >= 0:
            altura += 1

print("La altura de la pirámide:", altura)
'''
blocks = int(input("Ingrese el número de bloques:"))
height = 0
while blocks > height:
    height = height + 1
    blocks = blocks - height
    
print("La altura de la pirámide:", height)
'''        
