from pessoa import Pessoa, humano
from tempo import Tempo,tempo
from time import sleep
from options import *


# alteração do comentário

while True:
    clean_screen()
    print_slow(f'''\n{humano.name} tem {humano.age} anos, é casada com Amando de 45 anos.\nJoão é o primeiro filho do casal que tem 6 anos de idade.\n{humano.name} trabalha em período integral 8:00 – 18:00 em uma escola que fica \nlocalizada a 2 horas da sua casa. Ela está no penúltimo semestre da faculdade.\nO casal não possui casa própria, moram de aluguel. Amando está desempregado.\nAjude {humano.name} a conseguir seus objetivos:\n''')
    sleep(2)

        # print_slow(opcao1())  # intro
        # abaixo temos algumas funções que foram importadas de um módulo e possuem
        # condições para adicionar ou não certos atributos.
            
    print(option1())
    sleep(4)
    print(option2())
    sleep(4)
    print(option3())
    sleep(4)
    print(option4())
    sleep(4)
    print(option5())
    sleep(4)
    print(option6())
    sleep(4)
    print(option7())
    sleep(4)
    print(option8())
    sleep(4)
    terminar = input('Você quer tentar mais uma vez? (S/N)').upper()[0]
    while terminar not in 'SN':
        terminar = input('Você quer tentar mais uma vez? (S/N)').upper()[0]
    if terminar == 'S':
        continue
    else:
        print(humano)
        break

