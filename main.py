from pessoa import Pessoa, humano
from tempo import Tempo
from time import sleep
from opcaos import *

import sys

# alteração do comentário
tempo = Tempo()


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.044)


while True:
    clean_screen()
    print_slow(
        f'''\n{humano.nome} tem {humano.idade}, é casada com Amando de 45 anos.\nJoão é o primeiro filho do casal que tem 6 anos de idade.\n{humano.nome} trabalha em período integral 8:00 – 18:00 em uma escola que fica \nlocalizada a 2 horas da sua casa. Ela está no penúltimo semestre da faculdade.\nO casal não possui casa própria, moram de aluguel. Amando está desempregado.\nAjude {humano.nome} a conseguir seus objetivos:\n''')
    sleep(2)

    # print_slow(opcao1())  # intro
    # abaixo temos algumas funções que foram importadas de um módulo e possuem
    # condições para adicionar ou não certos atributos.
        
    print(opcao1())
    sleep(4)
    print(opcao2())
    sleep(4)
    print(opcao3())
    sleep(4)
    print(opcao4())
    sleep(4)
    print(opcao5())
    sleep(4)
    print(opcao6())
    sleep(4)
    print(opcao7())
    sleep(4)
    print(opcao8())
    sleep(4)
    break
