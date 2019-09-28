#Trabalho 02:
#Aluno: Gabriel Cardoso Mendes de Ataide
#Matricula: 11811ECP008
class Tempo:
    #constructor
    def __init__(self,hr=0,minu=0,seg=0):
        self.hr = hr
        self.minu = minu
        self.seg = seg
    #solicitar hora,min e seg:
    def solicita(self):
        self.hr = input("Digite a(s) Hora(s): ")
        self.minu = input("Digite o(s) Minuto(s): ")
        self.seg = input("Digite o(s) Segundo(s): ")
    #geters:
    def get_hr(self):
        return self.hr
    def get_minu(self):
        return self.minu
    def get_seg(self):
        return self.seg
    #seters:
    def set_hr(self,hr):
        self.hr = hr
    def set_minu(self,minu):
        self.minu = minu
    def set_seg(self,seg):
        self.seg = seg
    #retorna tempo:
    def retorna_tempo(self):
        return str(self.hr)+':'+str(self.minu)+':'+str(self.seg)
    #converte
    def converte_tempo(self):
        while(self.seg >= 60):
            self.seg-=60
            self.minu+=1
        while(self.minu >= 60):
            self.minu-=60
            self.hr+=1
        return self
    #adiciona
    def adiciona_tempo(self,t2):
        self.hr+=t2.hr
        self.minu+=t2.minu
        self.seg+=t2.seg
        return self.converte_tempo()
    #remove    
    def remove_tempo(self,t2):
        self.hr = abs(self.hr-t2.hr)
        self.minu = abs(self.minu-t2.minu)
        self.seg = abs(self.seg-t2.seg)
        return self.converte_tempo()

class Estacionamento:
    #constructor
    def __init__(self,placa='',marca='',tempo_entrada=Tempo(),tempo_saida=Tempo()):
        self.placa = placa
        self.marca = marca
        self.tempo_entrada = tempo_entrada
        self.tempo_saida = tempo_saida
    #solicita dados
    def solicita_dados(self):
        self.placa = input("Digite a Placa do Veículo: ")
        self.marca = input("Digite a Marca do Veículo: ")
        self.tempo_entrada = Tempo(input("Hr Entrada: "),input("Min. Entrada: "),input("Seg. Entrada: "))
        self.tempo_saida = Tempo(input("Hr Saida: "),input("Min. Saida: "),input("Seg. Saida: "))
    #imprime dados
    def imprime_dados(self):
        print("Placa: "+str(self.placa))
        print("Marca: "+str(self.marca))
        print("Entrada: "+str(self.tempo_entrada.retorna_tempo()))
        print("Saida: "+str(self.tempo_saida.retorna_tempo()))
    #valor cobrado
    def valor_cobrado(self):
        self.tempo_entrada.hr = int(self.tempo_entrada.hr)
        self.tempo_entrada.minu = int(self.tempo_entrada.minu)
        self.tempo_entrada.seg = int(self.tempo_entrada.seg)
        self.tempo_saida.hr = int(self.tempo_saida.hr)
        self.tempo_saida.minu = int(self.tempo_saida.minu)
        self.tempo_saida.seg = int(self.tempo_saida.seg)
        return 7 * (self.tempo_entrada.remove_tempo(self.tempo_saida).hr)


#tempo = Tempo()
#print("Hr:\t"+str(tempo.get_hr())+"\tMin:\t"+str(tempo.get_minu())+"\tSeg:\t"+str(tempo.get_seg()))
#tempo.set_hr(20)
#tempo.set_minu(39)
#tempo.set_seg(45)
#print("Hr:\t"+str(tempo.get_hr())+"\tMin:\t"+str(tempo.get_minu())+"\tSeg:\t"+str(tempo.get_seg()))
#print(tempo.retorna_tempo())
#tempo.solicita()
#print(tempo.retorna_tempo())
#t2 = Tempo(10,30,60)
#t1 = Tempo(10,30,60)
#print(t1.remove_tempo(t2).retorna_tempo())
#print(t1.adiciona_tempo(t2).retorna_tempo())

#carro = Estacionamento()
#carro.solicita_dados()
#print('R$: '+str(carro.valor_cobrado()))
lista = []
for i in range(0,5,1):
    lista.append(Estacionamento())
    print("Carro["+str(i+1)+"]:")
    lista[i].solicita_dados()

print("---------------------------------------")
print("\tRelatório de Veículos:")
print("---------------------------------------")
for j in range(0,5,1):
    print("Carro["+str(j+1)+"]:")
    print(lista[j].imprime_dados())
    print("Valor Cobrado: R$ "+str(lista[j].valor_cobrado())+",00")
    print("---------------------------------------")
