class Egitest:
    def __init__(self, sor:str):
        v:list[str] = sor.split(';')
        self.hol_kering:str = v[0]
        self.elnevezes:str = v[1]
        self.tavolsag:int = int(v[2])
        self.direktirany:bool = v[3] == '1'
        self.atmero:int = int(v[4])
        self.felfedezo:str = v[5]
        self.felfedezes_eve:str = int(v[6])