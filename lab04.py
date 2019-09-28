#Trabalho 04:
#Aluno: Gabriel Cardoso Mendes de Ataide
#Matricula: 11811ECP008
from random import randint

class Funcionario():
    #constructor:
    def __init__(self,_nome='',_codigo=''):
        self.nome = _nome
        self.codigo = _codigo
        self.salario = 1000.00
    #getters
    def getSalario():
        pass
    def getEscolaridade():
        pass

class SemEscolaridade(Funcionario):
    #constructor:
    def __init__(self,_nome='',_codigo=''):
        Funcionario.__init__(self,_nome,_codigo)
    #getters:
    def getSalario(self):
        return self.salario

class EnsinoBasico(Funcionario):
    #constructor:
    def __init__(self,_nome='',_codigo='', _escola=''):
        Funcionario.__init__(self,_nome,_codigo)
        self.escola = _escola
    #getters:
    def getSalario(self):
        return self.salario + (0.1*self.salario)

class EnsinoMedio(Funcionario):
    #constructor:
    def __init__(self,_nome='',_codigo='',_escola=''):
        Funcionario.__init__(self,_nome,_codigo)
        self.escola = _escola
    #getters:
    def getSalario(self):
        return self.salario + (0.5*self.salario)

class Graduacao(Funcionario):
    #constructor:
    def __init__(self,_nome='',_codigo='',_universidade='',_curso=''):
        Funcionario.__init__(self,_nome,_codigo)
        self.universidade = _universidade
        self.curso = _curso
    #getters:
    def getSalario(self):
        return 2*self.salario

lista = []
salario_total = 0
salario_escolaridade = {
    "SemEscolaridade":0.00,
    "EnsinoBasico":0.00,
    "EnsinoMedio":0.00,
    "Graduacao":0.00,
}

for i in range(0,10,1):
    aleatorio = randint(1,4)
    
    if aleatorio == 1:
        obj = SemEscolaridade('João','789521')
        salario_escolaridade["SemEscolaridade"]+=obj.getSalario()
        
    elif aleatorio == 2:
        obj = EnsinoBasico('Henrique','7419635','Escola Araguari')
        salario_escolaridade["EnsinoBasico"]+=obj.getSalario()
        
    elif aleatorio == 3:
        obj = EnsinoMedio('Lucas','74123','Escola Resende')
        salario_escolaridade["EnsinoMedio"]+=obj.getSalario()
        
    elif aleatorio == 4:
        obj = Graduacao('Gabriel','11811ECP008','UFU','Eng. de Computação')
        salario_escolaridade["Graduacao"]+=obj.getSalario()
            
    lista.append(obj)
    salario_total+=lista[i].getSalario()

print("----------------------------------------------------")
print("\tRelatório de Salários:")
print("----------------------------------------------------")
print("Ensino Básico: \t\tR$:",salario_escolaridade["EnsinoBasico"])
print("Sem Escolaridade: \tR$:",salario_escolaridade["SemEscolaridade"])
print("Ensino Médio: \t\tR$:",salario_escolaridade["EnsinoMedio"])
print("Graduação: \t\tR$:",salario_escolaridade["Graduacao"])
print("----------------------------------------------------")
print("TOTAL: \t\t\tR$:",salario_total)
