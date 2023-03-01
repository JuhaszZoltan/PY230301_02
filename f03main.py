from f03module import *

egitestek:list[Egitest] = []
file = open(file='egitestek.txt', mode='r', encoding='utf-8')
for s in file: egitestek.append(Egitest(s))

print(f'3.1. feladat: {len(egitestek)} égitest van az állományban.')

f32:int = 0
for e in egitestek:
    if e.hol_kering == 'Nap': f32 += 1
print(f'3.2. feladat: {f32} égitest kering a nap körül')

f33:int = 0
for i in range(len(egitestek)):
    if egitestek[i].tavolsag < egitestek[f33].tavolsag:
        f33 = i
print(f'3.3. feladat: a bolygójához legközelebb keringő égitest neve: {egitestek[f33].elnevezes}')

f34:list[str] = []
for e in egitestek:
    if not e.direktirany: f34.append(e.elnevezes)
print('3.4. feladat: ellentétes keringési irányú égitestek:')
for h in f34:
    print(f'\t- {h}')

f35:str = input('3.5. feladat: keresett égitest neve: ')
for e in egitestek:
    if e.elnevezes == f35:
        if e.felfedezo == '---' and e.felfedezes_eve == 0:
            print(f'\ta(z) {f35} szerepel az állományban,')
            print('\tde a felfedezéséről nincsenek adatok')
        else:
            print(f'\tfelfedező: {e.felfedezo}')
            print(f'\tfelfedezés éve: {e.felfedezes_eve}')
        break
else: print(f'\ta(z) {f35} égitest nem szerepel a listában')