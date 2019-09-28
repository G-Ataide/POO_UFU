#Trabalho 01:
#Aluno: Gabriel Cardoso Mendes de Ataide
#Matricula: 11811ECP008
class Vetor2D:
    #constructor:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #getters
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    #setters
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    #Produto Escalar
    def prodEscalar(self,vetB):
        return (vetB.getX() * self.x)+(vetB.getY() * self.y)
    #Módulo/Norma de um Vetor
    def modVet(self):
        return ((self.x **2) + (self.y**2)) ** 0.5
    #Angulo entre 2 Vetores
    def angVet(self,vetB):
        return (self.prodEscalar(vetB)/(self.modVet() * vetB.modVet()))
    #Projeção de A em B
    def projVet(self,vetB):
        #(v1.v2/v2.v2) vezes vetor v2
        a = (self.x * vetB.getX()) + (self.y * vetB.getY())
        b = vetB.modVet()**2
        return b

a = Vetor2D(10,20)
b = Vetor2D(10,3)

print("Get X de A: "+str(a.getX()))
print("Get Y de A: "+str(a.getY()))
print("Get X de B: "+str(b.getX()))
print("Get Y de B: "+str(b.getY()))

print("Prod Escalar: "+str(a.prodEscalar(b)))

print("Mod A: "+str(a.modVet()))
print("Mod B: "+str(b.modVet()))

print("Angulo: "+str(a.angVet(b)))

print("Projeção: "+str(a.projVet(b)))