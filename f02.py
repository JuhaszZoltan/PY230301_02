print('2. feladat:')
szoveg:str = input('írja be a szöveget: ').lower()

ek:str = 'áéíóöőúüű'
em:str = 'aeiooouuu'

for i in range(len(ek)):
    szoveg = szoveg.replace(ek[i], em[i])

spec:str = ',;:.!?'
for sk in spec:
    szoveg = szoveg.replace(sk, '\0')

szavak:list[str] = szoveg.split()

szoveg = szavak[0]
for szo in szavak[1:]:
    szoveg += szo.title()

print(f'camelCase változat: {szoveg}')