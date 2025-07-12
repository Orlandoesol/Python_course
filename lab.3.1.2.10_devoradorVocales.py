# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.

""" texto = input("Ingrese la palabra:").upper()

userWord=("A","E","I","O","U")

for letra in userWord:
    # Completa el cuerpo del ciclo for.
    texto = texto.replace(letra,"")
    
for letra in texto:
    print(letra) """

print("Lab.3.2.1.11")
palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord
userWord = input("Ingrese una palabra: ").upper()
vocal=("A","E","I","O","U")

for letra in userWord:
    if letra in vocal:
        continue
    else:
        print(letra+palabraSinVocal,end="\n")


	# Completa el cuerpo del ciclo.

# Imprimir la palabra asignada a palabraSinVocal.
