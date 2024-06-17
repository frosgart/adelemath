import random
import math
from datetime import date

def roundSum():
    randFloat = round(random.random(),3)
    randInteger = random.randint(100, 999)
    endNumber = randInteger + randFloat
    return endNumber

intList = list()
print('Generated at', date.today())

for i in range(0,9):
    iterationInteger = roundSum()
    intList.append(round(iterationInteger))
    print(iterationInteger)

print(intList)
print('####')
print(sum(intList))
