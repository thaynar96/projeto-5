from pessoa import Pessoa,humano
from tempo import Tempo
from opcaos import *

tempo = Tempo()


play = True
while play == True:
    print (f'''
    Esse jogo aborda a realidade brasileira da sobrecarga de trabalho da mulher. 
    Reflita sobre cada escolha, para tomar uma decisão.  
    Use como norteador de objetivos da personagem a pirâmide de Maslow. 
''') #intro
    print (f'''
    
        {humano.nome} tem {humano.idade}, é casada com Amando 
        de 45 anos.João é o primeiro filho do casal
        que tem 6 anos de idade.{humano.nome} trabalha em período
        integral 8:00 – 18:00 em uma escola que fica localizada 
        a 2 horas da sua casa. Ela está no penúltimo semestre da 
        faculdade. O casal não possui casa própria, moram de 
        aluguel. Amando está desempregado. 
    
        Ajude a {humano.nome} conseguir seus objetivos:
        ''')
    
    opcao1()
    opcao2()
    opcao3()
    opcao4()
    opcao5()
    opcao6()
    opcao7()
    opcao8()
    break
 

