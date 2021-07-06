from tempo import Tempo
from random import randint
tempo = Tempo()
class Pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome.title()
        self.__idade = idade
        self.__relacionamento = 0
        # self.relacionamentoCasal = 0
        self.__trabalho = 0
        self.__faculdade = 0
        self.__seguranca = 0
        self.__saude = 100
    


    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome


    def acrescentarSaude(self):
        pass

    def retirarSaude(self):
        pass

humano = Pessoa('Maria',42)

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