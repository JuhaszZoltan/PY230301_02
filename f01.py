from random import randint

print('1. feladat: ', end=' ')
for x in range(6):
    rnd:int = randint(3, 10)
    print(rnd * '*', end=' ')