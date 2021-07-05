from tempo import Tempo
from random import randint
tempo = Tempo()
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome.title()
        self.idade = idade
        self.relacionamentoSocial = 0
        self.relacionamentoCasal = 0
        self.trabalho = 0
        self.faculdade = 0
        self.seguranca = 0
        self.saude = 100
    

    def situacaoUm(self):
        pass

    def trabalhar(self):
        pass

    def irFaculdade(self):
        pass

    def tomarBanho(self):
        pass

    def cuidarFilho(self):
        pass

    def dormir(self):
        pass

Maria = Pessoa('Maria',34)

Maria.situacaoUm()
# if escolha == 1:
#     Maria.trabalhar()
#     tempo.passarTempo(60*8)
# elif escolha == 2:
#     Maria.tomarBanho()
#     tempo.passarTempo(20)
# elif escolha == 3:
    
#     tempo.passarTempo(20)
# elif escolha == 4:
#     Maria.cuidarFilho()
#     tempo.passarTempo(20)
# elif escolha == 5:
#     Maria.trabalhar()
#     tempo.passarTempo(20)
# elif escolha == 6:
#     Maria.dormir()
#     tempo.passarTempo(20)

#     print(tempo.hora)