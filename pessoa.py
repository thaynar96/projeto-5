from tempo import Tempo
from random import randint
tempo = Tempo()


class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome.title()
        self.__idade = idade

        self.__familya = 0
        self.__relacionamento_casal = 50
        self.__bemEstar = 50
        self.__trabalho = 100
        self.__estudo = 0
        self.__seguranca = 100
        self.__saude = 100

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade
    
    @property
    def saude(self):
        return self.__saude
    
    @property
    def familya(self):
        return self.__familya

    @property
    def relacionamento_casal(self):
        return self.__relacionamento_casal

    @property
    def bemEstar(self):
        return self.__bemEstar

    @property
    def trabalho(self):
        return self.__trabalho

    @property
    def estudo(self):
        return self.__estudo

    @property
    def seguranca(self):
        return self.__seguranca

    def acrescentarSaude(self):
        pass

    def retirarSaude(self):
        pass

    def __str__(self):
        return f'''\nPONTUAÇÃO:
            Família: {self.__familya}
            Relacionamento do Casal: {self.__relacionamento_casal}
            Bem Estar: {self.__bemEstar}
            Trabalho: {self.__trabalho}
            Estudo: {self.__estudo}
            Segurança: {self.__seguranca}
            Saúde: {self.__saude}'''

    def update_scores(self, fam, rel_casal, bem_est, trab, estd, segur, saude):
        param = [fam, rel_casal, bem_est, trab, estd, segur, saude]
        atrib = [self.__familya, self.__relacionamento_casal, self.__bemEstar,
                self.__trabalho, self.__estudo, self.__seguranca, self.__saude]
        for i in range(0, 7):
            if atrib[i] + param[i] >= 100:
                atrib[i] = 100
            elif atrib[i] + atrib[i] <= 0:
                atrib[i] = 0
            else:
                atrib[i] += param[i]

        self.__familya = atrib[0]
        self.__relacionamento_casal = atrib[1]
        self.__bemEstar = atrib[2]
        self.__trabalho = atrib[3]
        self.__estudo = atrib[4]
        self.__seguranca = atrib[5]
        self.__saude = atrib[6]


humano = Pessoa('Maria', 42)

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
