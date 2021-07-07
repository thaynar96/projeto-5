from pessoa import Pessoa,humano
from tempo import Tempo
from opcaos import *
from time import sleep
import sys
tempo = Tempo()

while True:

    
    def print_slow(str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.044)

    print_slow(
        f'''{humano.nome} tem {humano.idade}, é casada com Amando de 45 anos.\nJoão é o primeiro filho do casal que tem 6 anos de idade.\n{humano.nome} trabalha em período integral 8:00 – 18:00 em uma escola que fica \nlocalizada a 2 horas da sua casa. Ela está no penúltimo semestre da faculdade.\nO casal não possui casa própria, moram de aluguel. Amando está desempregado.\nAjude {humano.nome} a conseguir seus objetivos:\n''')
    print_slow(opcao1())
    opcao2()
    opcao3()
    opcao4()
    opcao5()
    opcao6()
    opcao7()
    opcao8()

    terminar = input('Você quer jogar mais uma vez? [S/N]').upper()[0]
    while terminar not in 'SN':
        input('Não entendi. Você pode digitar novamente? [S/N]').upper()[0]
    if terminar == 'S':
        continue
    else:
        break
    # print(
    #         '[ 1 ] Trabalhar\n[ 2 ] Tomar Banho\n[ 3 ] Comer\n[ 4 ] Cuidar do filho\n[ 5 ] Trabalhar \n[ 6 ] Dormir')

