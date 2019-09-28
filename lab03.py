#Trabalho 03:
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
    def modVet2D(self):
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

class Vetor3D(Vetor2D):
    #constructor:
    def __init__(self,x=0,y=0,z=0):
        Vetor2D.__init__(self,x,y)
        self.z = z
    #getter:
    def getZ(self):
        return self.z
    #setter:
    def setZ(self,z):
        self.z = z
    #Módulo/Norma de um Vetor:
    def modVet3D(self):
        return ((self.x **2) + (self.y**2)+(self.z**2)) ** 0.5
    #Produto Vetorial:
    def prodVet(self,vetB):
        xLocal = self.getX();
        yLocal = self.getY();
        zLocal = self.getZ();
        self.x = (yLocal * vetB.getZ())-(zLocal * vetB.getY())
        self.y = (zLocal * vetB.getX())-(xLocal * vetB.getZ())
        self.z = (xLocal * vetB.getY())-(yLocal * vetB.getX())
    
a = Vetor3D(1,2,-2);
b = Vetor3D(3,0,1);

a.setX(1)
a.setY(2)
a.setZ(-2)

b.setX(3)
b.setY(0)
b.setZ(1)

print("VETOR A: x:"+str(a.getX())+"\ty:"+str(a.getY())+"\tz:"+str(a.getZ()))
print("VETOR B: x:"+str(b.getX())+"\ty:"+str(b.getY())+"\tz:"+str(b.getZ())+"\n")

print("Módulo de A: "+str(a.modVet3D()))
print("Módulo de B: "+str(b.modVet3D())+"\n")

a.prodVet(b)
print("Produto Vetorial de A com B")
print("X:"+str(a.getX())+"\tY:"+str(a.getY())+"\tZ:"+str(a.getZ()))