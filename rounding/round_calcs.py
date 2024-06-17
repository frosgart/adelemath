import random
import math

def roundSum():
    randFloat = round(random.random(),3)
    randInteger = random.randint(100, 999)
    endNumber = randInteger + randFloat
    return endNumber

intList = list()
for i in range(0,9):
    iterationInteger = roundSum()
    intList.append(round(iterationInteger))
    print(iterationInteger)

print('####')
print(sum(intList))
