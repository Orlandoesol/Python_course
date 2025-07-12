#import module
#print(module.counter)
from module import suml, prodl

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeros),"\n",prodl(ones))
