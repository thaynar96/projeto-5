from pessoa import Pessoa
from tempo import Tempo,tempo
from time import sleep
from options import *


# alteração do comentário
human = Pessoa('Maria',42)

while True:
    clean_screen()
    print_slow(f'''\n{human.name} tem {human.age} anos, é casada com Amando de 45 anos.\nJoão é o primeiro filho do casal que tem 6 anos de idade.\n{human.name} trabalha em período integral 8:00 – 18:00 em uma escola que fica \nlocalizada a 2 horas da sua casa. Ela está no penúltimo semestre da faculdade.\nO casal não possui casa própria, moram de aluguel. Amando está desempregado.\nAjude {human.name} a conseguir seus objetivos:\n''')
    sleep(2)

        # print_slow(opcao1())  # intro
        # abaixo temos algumas funções que foram importadas de um módulo e possuem
        # condições para adicionar ou não certos atributos.
            
    option1(human)
    sleep(4)
    option2(human)
    sleep(4)
    option3(human)
    sleep(4)
    option4(human)
    sleep(4)
    option5(human)
    sleep(4)
    option6(human)
    sleep(4)
    option7(human)
    sleep(4)
    option8(human)
    sleep(4)
    end = input('Você quer tentar mais uma vez? (S/N)').upper()[0]
    while end not in 'SN':
        end = input('Você quer tentar mais uma vez? (S/N)').upper()[0]
    if end == 'S':
        continue
    else:
        print(human)
        break

