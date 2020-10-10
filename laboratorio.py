#Hector Andres Alcala Gutierrez

from particula import Particula

class Laboratorio:
    
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, p: Particula):
        self.__particulas.append(p)

    def agregar_inicio(self, p: Particula):
        self.__particulas.insert(0, p)

    def mostrar(self):
        for p in self.__particulas:
            print(p)

#p1 = Particula(145, 0, 0, 8, 4, 300, 255, 255, 255)
#p2 = Particula(284, 10, 10, 0, 0, 50, 255, 0, 0)
#lab = Laboratorio()
#lab.agregar_final(p1)
#lab.agregar_inicio(p2)
#lab.agregar_inicio(p1)
#lab.mostrar()