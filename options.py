from random import randint
from pessoa import Pessoa
from time import sleep
from tempo import Tempo,tempo
import os
import sys

#função para validar a entrada da resposta de cada interação
def validation(a):
    while a not in 'AB':
        a = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    return a
#função para escrever textos letra a letra
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.044)
#função para limpar o terminar a cada interação
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#função para zerar o horário
def clean_time():
    tempo.hour = 5
    tempo.minute =0
#função que mostra quanto foi adicionado a cada atributo depois da interação
def show_scores(scores, labels):
    print()
    print('\033[1;93mPONTOS\033[m:')
    for i in range(0,7):
        if scores[i] != 0:
            print(f'\033[96m{labels[i]}\033[m:  \033[93m{scores[i]}\033[m \033[96mpontos\033[m')
    print()

#função com a primeira parte da história e que recebe o objeto como parametro.
def option1(human):
    clean_screen()
    print(Tempo())
    print_slow(f'{human.name} acorda cansada, não dormiu direito pois estava preocupada\ncomo iria honrar com as contas. João está chorando, com a fralda suja e\n{human.name} está atrasada para ir ao trabalho.')
    print(
    f'''


            A){human.name} vai cuidar do filho, toma um banho rápido
            ou prepara sua merenda e em seguida vai para o trabalho.

            B)Acorda Amando e pede que ele vá cuidar do filho e preparar
            a merenda do casal enquanto {human.name} vai tomar banho.        
    '''   )
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{human.name} tem grandes chances de chegar atrasada no trabalho e poderá ser advertida pelo seu superior.')

            fam = 10
            couple_relat = 0
            welfare = 0
            wrk = -10
            std = 0
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
        elif random_choice == 2:
            print(f'\n{human.name} cuida do filho e toma banho,mas está com fome por que não merendou')

            fam = 10
            couple_relat = 10
            welfare = 0
            wrk = 10
            std = 0
            saft = 0
            health = 20

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

            
    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nAmando cuida do filho e faz a merenda do casal. {human.name} chega à tempo no trabalho. ')

            fam = 10
            couple_relat = 10
            welfare = 0
            wrk = 10
            std = 0
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)

        elif random_choice == 2:
            print(
                f'\nAmando volta a dormir e não faz o que {human.name} pediu. ')

            fam = -10
            couple_relat = -10
            welfare = 0
            wrk = 10
            std = 0
            saft = 0
            health = -10
    
            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
def option2(human):
    clean_screen()
    tempo.pass_time(30)
    print(tempo)
    print_slow(f'{human.name} ao tentar sair com o carro elétrico, que foi emprestado\npor seu irmão Fabio, nota dois suspeitos na frente da casa.')
    print(f'''


            A){human.name} ignora os dois homens e abre o portão
            da garagem que não é automático.

            B){human.name} chama Amando, que a orienta a chamar a policia
            e aguardar até que os dois homens saiam da frente da garagem.         
    ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = 2
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{human.name} foi muito imprudente, colocou sua vida e da sua família em risco.')

            fam = 0
            couple_relat = 0
            welfare = 0
            wrk = 10
            std = 0
            saft = -10
            health = 0

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
        elif random_choice == 2:
            print(
                f'\nOs dois homens estavam hospedados na casa da frente, não ofereceram perigo. Eles esqueceram a chave e o celular dentro de casa . {human.name} ligou para um chaveiro 24h para ajudar os dois rapazes e em seguida foi para o trabalho. ')
            tempo.pass_time(20)
            fam = 0
            couple_relat = 10
            welfare = 0
            wrk = -10
            std = 0
            saft = 0
            health = 0

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)

    elif answer == 'B':
        if random_choice == 1:
            print(f'\n{human.name} segue o conselho do Amando, chama a polícia e espera até que os dois homens saiam da frente da garagem.')
            tempo.pass_time(20)
            fam = 0
            couple_relat = 10
            welfare = 5
            wrk = -10
            std = 0
            saft = 10
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
        elif random_choice == 2:
            print(f'\n{human.name} briga com Amando, diz que ele é muito medroso, mas espera os dois homens irem embora e aciona a polícia. ')
            tempo.pass_time(15)
            fam = 0
            couple_relat = -10
            welfare = 0
            wrk = -10
            std = 0
            saft = 10
            health = 5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
            

    #sleep(4)

def option3(human):
    clean_screen()
    tempo.pass_time(30)
    print(tempo)
    print_slow(f'{human.name} está no início do  percurso em direção ao seu trabalho,\ndentro do limite de velocidade permitido pela via. Ela tem duas rotas para escolha: ')
    print(f'''


            A){human.name} escolhe o caminho mais rápido.

            B){human.name} pega a rota normal.      
    ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nNo caminho mais rápido uma pessoa entra na frente do carro, mas ela não foi atropelada, não teve danos materiais, só o susto.')

            fam = 0
            couple_relat = 0
            welfare = 10
            wrk = 0
            std = 0
            saft = 10
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(
                f'\nNo caminho mais rápido uma pessoa entra na frente do carro. Ao jogar o carro para a calçada {human.name} bateu no meio fio e furou o pneu se atrasou. ')
            tempo.pass_time(30)
            fam = 0
            couple_relat = 0
            welfare = -5
            wrk = -10
            std = 0
            saft = -10
            health = -10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
    elif answer == 'B':
        if random_choice == 1:
            print(f'\nO trânsito esta normal, ela chega no trabalho cedo.')

            fam = 0
            couple_relat = 0
            welfare = 5
            wrk = 10
            std = 0
            saft = 0
            health = 5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
        elif random_choice == 2:
            print(
                f'\n{human.name} pega um engarrafamento devido um acidente e chega atrasada no trabalho.')

            fam = 0
            couple_relat = 0
            welfare = -5
            wrk = -10
            std = 0
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
    #sleep(4)

def option4(human):
    clean_screen()
    tempo.pass_time(60*2)
    print(tempo)
    print_slow(f'O chefe de {human.name} pede que ela seja realocada de função durante 7\ndias, para uma função de gestão de planejamentos de dados da escola. Caso {human.name}\naceite essa pequena mudança ela terá que levar trabalho para casa e fazer pela\nmadrugada adentro, já que não dispõe de outro horário. ')
    print(f'''


            A){human.name} vê esse desafio como uma oportunidade de evolução
            pessoal e profissional mesmo que ela abdique de algumas horas do seu sono.

            B){human.name} recusa educadamente o pedido do chefe já que não tem tempo
            disponível. Mas fica triste em dar a recusa, pois o seu superior é muito
            compreensível com ela, até autorizou a sua saída uma hora mais cedo, 
            para que ela chegue a tempo na faculdade.        
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nDevido ao esforço de {human.name} ela é promovida a um cargo temporário de confiança que lhe permite ganhar mais, ela fica mais contente por dar mais conforto para sua família através do aumento que vai ter.')

            fam = 10
            couple_relat = 0
            welfare = 10
            wrk = 10
            std = 0
            saft = 10
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(f'\n{human.name} fica muito estressada e sobrecarregada com a quantidade de trabalho e o tempo disponível que tem. Acaba não dando atenção ao João e desconta seu estresse em Amando.')

            fam = 10
            couple_relat = -10
            welfare = -10
            wrk = 0
            std = 0
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    elif answer == 'B':
        if random_choice == 1:
            print(f'\nSeu chefe ficou chateado, já que ele sempre procura ajudar human de todas as formas possíveis.')

            fam = 0
            couple_relat = 0
            welfare = -10
            wrk = -10
            std = 0
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(
                f'\n{human.name} perdeu a oportunidade de ter um aumento. Ficou mais tempo com o seu filho.  ')

            fam = 10
            couple_relat = 0
            welfare = 0
            wrk = 0
            std = 0
            saft = 0
            health = 5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
    #sleep(4)


def option5(human):
    clean_screen()
    tempo.pass_time(60*3)
    print(tempo)
    print_slow(f'{human.name} está no seu horário de almoço e dispõe de 30 min para o\nalmoçar. Quando recebe uma ligação da escola do seu filho dizendo que o Amando não foi\nbuscar a criança.')
    print(f'''


            A){human.name} não almoça e vai pegar João na escola e traz ele 
            para o seu local de trabalho.

            B)Tenta ligar para o Armando e saber o que houve.        
            ''')
    
    choice = input('Digite uma opção do menu [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\n{human.name} brincou bastante de adivinhação com João no trajeto da escola para o seu trabalho. ')

            fam = 10
            couple_relat = -10
            welfare = 5
            wrk = 0
            std = 0
            saft = 0
            health = 0

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(
                f'\n{human.name} falou mal do pai na frente do João quando voltava da escola para o seu trabalho. ')

            fam = -10
            couple_relat = -10
            welfare = -5
            wrk = 0
            std = 0
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    elif answer == 'B':
        if random_choice == 1:
            print(f'\nDescobre que Armando se atrasou por que ele voltou para casa para fechar a panela de pressão que esqueceu ligada.  Amando estava preparando o prato favorito do filho.')

            fam = 10
            couple_relat = 10
            welfare = 0
            wrk = 0
            std = 0
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(f'\nDescobre que Amando não foi pegar o filho por que estava em um bar. ')

            fam = -10
            couple_relat = -10
            welfare = -5
            wrk = 0
            std = 0
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
    #sleep(4)

def option6(human):
    clean_screen()
    tempo.pass_time(60*7)
    print(tempo)
    print_slow(
        f'Durante o trajeto para a faculdade, o gps informa de um grande engarrafamento mais\nà frente. {human.name} tem um trabalho para apresentar em grupo:')
    print(f'''


            A)Pega um desvio mais longo que não tem engarrafamento.

            B)Fica na mesma via, supondo que o engarrafamento já terminou.        
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\nO desvio que {human.name} fez apesar de ser mais longo não houve engarrafamento durante o trajeto, {human.name} chegou na faculdade no horário correto.')

            fam = 0
            couple_relat = 0
            welfare = 5
            wrk = 0
            std = 10
            saft = 0
            health = 5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
        elif random_choice == 2:
            print(
                f'\nDurante o desvio houve engarrafamento e {human.name} chegou atrasada na faculdade.')

            fam = 0
            couple_relat = 0
            welfare = -5
            wrk = 0
            std = -10
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    elif answer == 'B':
        if random_choice == 1:
            print(f'\n{human.name} não seguiu o conselho de desvio do gps e chegou na faculdade adiantada, aproveitou para lanchar e ligar para o filho.')

            fam = 10
            couple_relat = 0
            welfare = 0
            wrk = 0
            std = 10
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(f'\n{human.name} ficou presa no engarrafamento, ficou estressada, chegou atrasada na faculdade, e levou uma advertência do professor. ')

            fam = 0
            couple_relat = 0
            welfare = -10
            wrk = 0
            std = -10
            saft = 0
            health = -10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)

    #sleep(4)

def option7(human):
    clean_screen()
    print_slow(
        f'Ao ir em direção a vaga de estacionamento, {human.name} aguarda o carro sair da\n vaga para poder estacionar, quando de repente um motorista\nentra de uma vez e pega a vaga. ')
    print(f'''


            A)Procura por outra vaga

            B)Tenta dialogar com o motorista para que ele dê a vaga para ela,
            já que ela estava esperando o motorista da vaga sair para ela poder entrar
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(f'\nEncontra uma vaga e consegue chegar à tempo na faculdade ')

            fam = 0
            couple_relat = 0
            welfare = -5
            wrk = 0
            std = 10
            saft = 0
            health = 5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(f'\nChega atrasada na classe de aula')
            tempo.pass_time(15)
            fam = 0
            couple_relat = 0
            welfare = -5
            wrk = 0
            std = -10
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nO motorista que furou a frente da {human.name} pede desculpas e tira o\ncarro da vaga. {human.name} chega no horário na sala de aula.')

            fam = 0
            couple_relat = 0
            welfare = 10
            wrk = 0
            std = 10
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

        elif random_choice == 2:
            print(f'\nO motorista não tira o carro da vaga, {human.name} xinga o motorista\né chega atrasada na sala de aula.  ')

            fam = 0
            couple_relat = 0
            welfare = -10
            wrk = 0
            std = -5
            saft = 0
            health = -5

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    #sleep(4)

def option8(human):
    clean_screen()
    tempo.pass_time(60*4)
    print(tempo)
    print_slow(
        f'Ao chegar em casa, {human.name} descobre que Amando estava bêbado e não cuidou do filho. João estava sujo, com fome e chorando. ')
    print(f'''


            A){human.name} vai cuidar de João, toma banho e vai jantar e vai dormir.

            B){human.name} vai cuidar do filho e do marido. Toma banho, vai jantar
            e depois faz os trabalhos da faculdade e da escola onde ensina.
    ''')
    
    choice = input('Digite uma opção do menu  [A / B]:  ')[0].upper()
    answer = validation(choice)
    random_choice = randint(1, 2)
    
    if answer == 'A':
        if random_choice == 1:
            print(
                f'\nMesmo estando exausta de uma longa jornada de trabalho, {human.name} cuida do filho, prepara a sua janta, toma banho e vai dormir.')

            fam = 10
            couple_relat = -10
            welfare = 5
            wrk = 0
            std = 0
            saft = 0
            health = 0

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            


        elif random_choice == 2:
            print(f'\n{human.name} cuida do filho e depois cai na cama de tanto cansaço. O sono foi mais forte que a fome e banho.')

            fam = 5
            couple_relat = -10
            welfare = -5
            wrk = 0
            std = 0
            saft = 0
            health = -10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    elif answer == 'B':
        if random_choice == 1:
            print(
                f'\nApesar do problema de alcoolismo do Marido, {human.name} acredita que Amando vai superar essa fase. Ela priorizou o cuidado de todos os integrantes da família.')

            fam = 10
            couple_relat = 10
            welfare = 10
            wrk = 10
            std = 10
            saft = 0
            health = 20

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            
        elif random_choice == 2:
            print(f'\n{human.name} está pensando em se divorciar, mas apesar dos problemas que ela tem com o marido, João é muito apegado com o pai, ela teme que o João fique muito triste com a separação dos pais. {human.name} vai dormir com uma forte dor de cabeça. ')

            fam = 0
            couple_relat = -5
            welfare = 10
            wrk = 10
            std = 10
            saft = 0
            health = 10

            human.scores = [fam, couple_relat, welfare, wrk, std, saft, health]
            human.update_scores(human.scores)            
            show_scores(human.scores, human.labels)
            

    #sleep(4)

def conclusao(human):
    clean_screen()
    if human.health >= 90:
        print_slow(f'\nParabéns,a {human.name} conseguiu alcançar seus objetivos!\n\n\n\nDe acordo com o estudo feito pelo Instituto de Pesquisa Econômica Aplicada,as\nmulheres trabalham cerca de 7,5 horas a mais do que os homens.O percentual de\ndomicílios brasileiros comandados por mulheres saltou de 25%, em 1995, para 45%\n em 2018. 43% das mulheres que são chefes de domicílio no Brasil vive em casal\n – sendo que 30% têm filhos e 13% não. Já o restante das 34,4 milhões das\nreponsáveis pelo lar se dividem entre mulheres solteiras com filho (32%),\nmulheres que vivem sozinhas (18%) e mulheres que dividem a casa com amigos ou parentes (7%).')
    else:
        print_slow(f'Infelizmente, a {human.name} não conseguiu alcançar seus objetivos.\n\n\nDe acordo com o estudo feito pelo Instituto de Pesquisa Econômica Aplicada, as\nmulheres trabalham cerca de 7,5 horas a mais do que os homens.O percentual de domicílios\n brasileiros comandados por mulheres saltou de 25%, em 1995, para 45% em 2018.\n43% das mulheres que são chefes de domicílio no Brasil vive em casal – sendo que\n30% têm filhos e 13% não. Já o restante das 34,4 milhões das responsáveis pelo lar \nse dividem entre mulheres solteiras com filho (32%), mulheres que vivem \nsozinhas (18%) e mulheres que dividem a casa com amigos ou parentes (7%).')
