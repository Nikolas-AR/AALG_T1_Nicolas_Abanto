import random

class EquipoVoley:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partGanados = 0
        self.partPerdidos = 0
        self.setGanados = 0

def RegistraSet(ganador, equipo1, equipo2):
    if ganador == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partGanados += 1
            equipo2.partPerdidos += 1
            print(f"{equipo1.nombre} gana el partido\n")
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            return True 
    elif ganador == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partGanados += 1
            equipo1.partPerdidos += 1
            print(f"{equipo2.nombre} gana el partido\n")
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            return True 
    return False  

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    print(f"\nDamas y caballeros, aperturamos un nuevo partido entre {equipo1.nombre} y {equipo2.nombre}")
    
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()
        
        print("PUNTAJE ACTUAL:")
        print(f"Set: {equipo1.nombre} {puntos1} - {puntos2} {equipo2.nombre}")
        
        if puntos1 >= 25 or puntos2 >= 25:
            if puntos1 > puntos2 and puntos1 >= 25:
                if RegistraSet(1, equipo1, equipo2):
                    break  
            elif puntos2 > puntos1 and puntos2 >= 25:
                if RegistraSet(2, equipo1, equipo2):
                    break  
                
        else:
            while True:
                ptsExt1 = PuntosExtras()
                ptsExt2 = PuntosExtras()
                
                puntos1 += ptsExt1
                puntos2 += ptsExt2         
                
                print(f"Puntos extra: {equipo1.nombre} +{ptsExt1} -> {puntos1}, {equipo2.nombre} +{ptsExt2} -> {puntos2}")
                
                if puntos1 >= 25 and puntos1 > puntos2:
                    if RegistraSet(1, equipo1, equipo2):
                        break  
                elif puntos2 >= 25 and puntos2 > puntos1:
                    if RegistraSet(2, equipo1, equipo2):
                        break  

def ResultadoTorneo(equipo1, equipo2):
    print("\nRESULTADOS DEL TORNEO:")  
    print(f"{equipo1.nombre} - GANADOS: {equipo1.partGanados}, PERDIDOS: {equipo1.partPerdidos}")     
    print(f"{equipo2.nombre} - GANADOS: {equipo2.partGanados}, PERDIDOS: {equipo2.partPerdidos}")   

def Main():
    print("TORNEO DE VOLEY INTERNACIONAL")

    equipo1 = EquipoVoley("PER")
    equipo2 = EquipoVoley("BRA")
    
    cantPart = int(input("Ingrese cuántos partidos se deben jugar: "))
    for i in range(cantPart):
        print(f"\nPARTIDO {i+1}")
        JugarPartido(equipo1, equipo2)
        
    ResultadoTorneo(equipo1, equipo2)

Main()
