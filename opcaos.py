from random import randint
from pessoa import Pessoa,humano
def opcao1():
    print(f'{humano.nome} acorda cansada, não dormiu direito pois estava preocupada como iria honrar com as contas. João está chorando, com a fralda suja e {humano.nome} está atrasada para ir ao trabalho.')
    print(f'''
    A){humano.nome} vai cuidar do filho, toma um banho rápido ou prepara sua merenda e em seguida vai para o trabalho.
    B)Acorda Amando e pede que ele vá cuidar do filho e prepare a merenda do casal enquanto {humano.nome} vai tomar banho.        
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'{humano.nome} chega atrasada no seu trabalho e é advertida pelo seu superior.')
            humano.retirarSaude()
            # atributos
        elif aleatorio == 2:
            print(f'{humano.nome} cuida do filho e toma banho, não chega atrasada no trabalho.Mas está com fome por que não merendou')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'Amando cuida do filho e faz a merenda do casal. {humano.nome} chega atempo no trabalho. ')
        elif aleatorio == 2:
            print(f'Amando volta a dormir e não faz o que {humano.nome} pediu. ')

def opcao2():
    print(f'{humano.nome} ao tentar sair com o carro elétrico, que foi emprestado por seu irmão Fabio, nota que tem dois suspeitos na frente da casa.')
    print(f'''
    A){humano.nome} ignora os dois homens é abre o portão da garage que NÃO é automático.
    B){humano.nome} chama Amando, que a orienta a chamar a policia e aguardar até que os dois homens saião da frente da garagem..         
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'{humano.nome} foi muito imprudente, colocou sua vida em risco é da sua família .')
            # atributos
        elif aleatorio == 2:
            print(f'Os dois sujeitos estavam hospedados na casa de frente, não ofereceram perigo, os dois homens esqueceram a chave dentro de casa e o celular. {humano.nome} ligou para um chaveiro 24h para ajudar os dois rapazes e em seguida foi para o trabalho. ')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'{humano.nome} segue o conselho do Amando, chama a policia e espera até que os dois homens saiam da frente da garagem.')
        elif aleatorio == 2:
            print(f'{humano.nome} briga com amando, diz que ele é muito medroso, mas espera que os dois homens vão embora, aciona a polícia. ')

def opcao3():
    print(f'{humano.nome} está no início do  percurso em direção ao seu trabalho, dentro do limite de velocidade permitido pela via, ela tem duas rotas para escolha: ')
    print(f'''
    A)Ela escolhe o caminho mais rápido:
    B){humano.nome} pega a rota normal:       
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'{humano.nome} foi muito imprudente, colocou sua vida em risco é da sua família .')
            # atributos
        elif aleatorio == 2:
            print(f'No caminho mais rápido uma pessoa entra na frente do carro. Ao jogar o carro para a calçada {humano.nome} bateu no meio fio e furou o pneu se atrasou. ')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'O trânsito esta normal, ela chega no trabalho cedo.')
        elif aleatorio == 2:
            print(f'{humano.nome} pega um engarrafamento devido um acidente e chega atrasada no trabalho.')


def opcao4():
    print(f'O chefe de {humano.nome} pede que ela seja realocada de função durante 7 dias, para uma função de gestão de planejamentos de dados da escola. Caso humano aceite essa pequena mudança ela vai ter que levar trabalho para casa é fazer pela madrugada adentro, já que não dispõem de outro horário. ')
    print(f'''
    A){humano.nome} vê esse desafio como uma oportunidade de evolução pessoal e profissional mesmo que ela abdique de algumas horas do seu sono.
    B){humano.nome} recusa educadamente o pedido do chefe já que não tem tempo disponível. Mas fica triste em dar a recusa, pois o seu superior é muito compreensível com ela, até autorizou a sua saída uma hora mais cedo, para que ela chegue atempo na faculdade.        
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'Devido ao esforço de {humano.nome} ela é promovida a um cargo temporário de confiança que lhe permite ganhar mais, ela fica mais contente por dar mais conforto para sua família através do aumento que vai ter.')
            # atributos
        elif aleatorio == 2:
            print(f'{humano.nome} fica muito estressada e sobrecarregada com a quantidade de trabalho e o tempo disponível que tem. Acaba não dando atenção ao João e desconta seu estresse em Amando.')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'Seu chefe ficou chateado, já que ele sempre procura ajudar humano de todas as formas possíveis.')
        elif aleatorio == 2:
            print(f'{humano.nome} perdeu a oportunidade de ter um aumento. Ficou mais tempo com o seu filho.  ')


# def opcao2():
#     print('')
def opcao5():
    print(f'{humano.nome} está no seu horário de almoço e dispõe de 30 min para o almoçar. Quando recebe uma ligação da escola do seu filho dizendo que o Amando não foi buscar a criança.')
    print(f'''
    A){humano.nome} não almoça e vai pegar João na escola e traz ele para o seu local de trabalho.
    B)Tenta ligar para o Armando e saber o que houve.        
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'{humano.nome} brincou bastante de adivinhação com João no trajeto da escola para o seu trabalho. ')
            # atributos
        elif aleatorio == 2:
            print(f'{humano.nome} falou mal do pai na frente do João quando voltava da escola para o seu trabalho. ')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'Descobre que Armando se atrasou por que ele voltou para casa para fechar a panela de pressão que esqueceu ligada.  Amando estava preparando o prato favorito do filho.')
        elif aleatorio == 2:
            print(f'Descobre que Amando não foi pegar o filho por que estava em um bar. ')

def opcao6():
    print(f'Durante o trajeto para a faculdade, o gps informa de um grande engarrafamento mais afrente. {humano.nome} tem um trabalho para apresentar em grupo:')
    print(f'''
    A)Pega um desvio mais longo que não tem engarrafamento.
    B)Fica na mesma via, supondo que o engarrafamento já terminou.        
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'O desvio que {humano.nome} fez apesar de ser mais longo não houve engarrafamento durante o trajeto, {humano.nome} chegou na faculdade no horário correto.')
            # atributos
        elif aleatorio == 2:
            print(f'Durante o desvio houve engarrafamento e {humano.nome} chegou atrasada na faculdade.')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'{humano.nome} não seguiu o conselho de desvio do gps e chegou na faculdade adiantada, aproveitou para lanchar e ligar para o filho.')
        elif aleatorio == 2:
            print(f'{humano.nome} ficou presa no engarrafamento, ficou estressada, chegou atrasada na faculdade, e levou uma advertência do professor. ')


def opcao7():
    print(f'Ao ir em direção a vaga de estacionamento, {humano.nome} aguarda o carro sair da vaga para poder estacionar, quando de repente um motorista entra de uma vez e pega a vaga. ')
    print(f'''
    A)Procura por outra vaga
    B)Tenta dialogar com o motorista para que ele dê a vaga para ela, já que ela estava esperando o motorista da vaga sair para ela poder entrar
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'Encontra uma vaga e consegue chegar atempo no trabalho ')
            # atributos
        elif aleatorio == 2:
            print(f'Chega atrasada na classe de aula')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'O motorista que furou a frente da {humano.nome} pede desculpas e tira o carro da vaga. {humano.nome} chega no horário na sala de aula.')
        elif aleatorio == 2:
            print(f'O motorista não tira o carro da vaga, humano xinga o motorista é chega atrasada na sala de aula.  ')

def opcao8():
    print(f'Ao chegar em casa, {humano.nome} descobre que Amando estava bêbado e não cuidou do filho. João estava sujo, com fome e chorando. ')
    print(f'''
    A){humano.nome} vai cuidar de João, toma banho, vai jantar e vai dormir.
    B){humano.nome} vai cuidar do filho e do marido. Tomar banho, vai jantar e depois faz os trabalhos da faculdade e da escola onde ensina.
    ''')
    escolha = input('Digite uma opção do menu:')[0].upper()
    aleatorio = randint(1,2)
    if escolha == 'A':
        if aleatorio == 1:
            print(f'Mesmo estando exausta de uma longa jornada de trabalho, {humano.nome} cuida do filho, prepara a sua janta, toma banho e vai dormir.')
            # atributos
        elif aleatorio == 2:
            print(f'{humano.nome} cuida do filho e depois cai na cama de tanto cansaço. O sono foi mais forte que a fome e banho.')
    elif escolha == 'B':
        if aleatorio == 1:
            print(f'Apesar do problema de alcoolismo do Marido, {humano.nome} acredita que Amando vai superar essa fase. Ela priorizou o cuidado de todos os integrantes da família.')
        elif aleatorio == 2:
            print(f'{humano.nome} está pensando em se divorciar, mas apesar dos problemas que ela tem com o marido, João é muito apegado com o pai, ela teme que o João fique muito triste com a separação dos pais. {humano.nome} vai dormir com uma forte dor de cabeça. ')