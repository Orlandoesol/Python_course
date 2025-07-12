""" 1 milla = 1609.344 metros.
1 galón = 3.785411784 litros. """
def l100kmtompg(liters):
    miles = 100 * 1000 / 1609.344
    gallon = liters / 3.785411784
    return miles / gallon

def mpgtol100km(miles):
    liters = 3.785411784
    kilometers = miles * 1609.344  / 1000
    km100 = kilometers / 100
    return liters / km100
#
# coloca tu código aqui
#

print(l100kmtompg(3.9))#60.31143162393162
print(l100kmtompg(7.5))#31.36194444444444
print(l100kmtompg(10.))#23.52145833333333
print(mpgtol100km(60.3))#3.9007393587617467
print(mpgtol100km(31.4))#7.490910297239916
print(mpgtol100km(23.5))#10.009131205673757