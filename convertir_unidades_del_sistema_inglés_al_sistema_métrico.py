def piespulgam(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254


def lbsakg(lb):
    return lb * 0.45359237

def imc(peso, altura):
    '''observa como el símbolo de diagonal invertida (\) es empleado. 
    Si se termina una línea de código con el, Python entenderá que 
    la línea continua en la siguiente.'''
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

#print(imc(352.5, 1.65))
print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))
