from tempo import Tempo
from random import randint
tempo = Tempo()


class Pessoa:
    def __init__(self, name, age):
        self.__name = name.title()
        self.__age = age

        self.__family = 0
        self.__couple_relationship = 50
        self.__well_being = 50
        self.__work = 100
        self.__study = 0
        self.__security = 100
        self.__health = 100

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @property
    def health(self):
        return self.__health
    
    @property
    def familya(self):
        return self.__family

    @property
    def couple_relationship(self):
        return self.__couple_relationship

    @property
    def well_being(self):
        return self.__well_being

    @property
    def work(self):
        return self.__work

    @property
    def study(self):
        return self.__study

    @property
    def security(self):
        return self.__security

    def acrescentarhealth(self):
        pass

    def retirarhealth(self):
        pass

    def __str__(self):
        return f'''\nPONTUAÇÃO:
            Família: {self.__family}
            Relacionamento do Casal: {self.__couple_relationship}
            Bem Estar: {self.__well_being}
            work: {self.__work}
            study: {self.__study}
            Segurança: {self.__security}
            Saúde: {self.__health}'''

    def update_scores(self, fam, rel_casal, bem_est, trab, estd, segur, health):
        param = [fam, rel_casal, bem_est, trab, estd, segur, health]
        atrib = [self.__family, self.__couple_relationship, self.__well_being,
                self.__work, self.__study, self.__security, self.__health]
        for i in range(0, 7):
            if atrib[i] + param[i] >= 100:
                atrib[i] = 100
            elif atrib[i] + atrib[i] <= 0:
                atrib[i] = 0
            else:
                atrib[i] += param[i]

        self.__family = atrib[0]
        self.__couple_relationship = atrib[1]
        self.__well_being = atrib[2]
        self.__work = atrib[3]
        self.__study = atrib[4]
        self.__security = atrib[5]
        self.__health = atrib[6]


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
