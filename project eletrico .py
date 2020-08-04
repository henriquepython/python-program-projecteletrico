#Olรก vamos fazer seu projeto!
#Quarto
print('Olá vamos fazer seu projeto elétrico!')
tensao = int(input('Informe sua tensão de operação!\n127 ou 220?\n'))
a = 0
#Quarto
while a == 0:

    qquarto = int(input('Informe a quantidade de quartos?\n1,2,3....\n'))

    if qquarto == 1:
        areaquarto1 = float(input('Informe a Área do quarto?\n'))
        perimetro1 = float(input('Informe o perímetro do quarto?\n'))

        tugquarto1 = perimetro1 // 5
        lumiquarto1 = areaquarto1 // 4
        potenciaquarto1 = ((tugquarto1 * 100) + (lumiquarto1 * 60))
        potenciatot1 = potenciaquarto1
        corrente1 = potenciaquarto1 / tensao
        print('quarto1\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciaquarto1,corrente1))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
    elif qquarto == 2:
        areaquarto1 = float(input('Informe a Área do quarto 1?\n'))
        perimetro1 = float(input('Informe o perímetro do quarto 1?\n'))
        areaquarto2 = float(input('Informe a Área do quarto 2?\n'))
        perimetro2 = float(input('Informe o perímetro do quarto 2?\n'))

        tugquarto1 = perimetro1 // 5
        lumiquarto1 = areaquarto1 // 4
        tugquarto2 = perimetro2 // 5
        lumiquarto2 = areaquarto2 // 4
        potenciaquarto1 = ((tugquarto1 * 100) + (lumiquarto1 * 60))
        potenciaquarto2 = ((tugquarto2 * 100) + (lumiquarto2 * 60))
        potenciatot1 = potenciaquarto2 + potenciaquarto1
        corrente1 = potenciaquarto1 / tensao
        corrente2 = potenciaquarto2 / tensao
        print('Quarto 1\nPotência:{:.2f}W\nCorrente:{:.2f}A\nQuarto 2\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciaquarto1,corrente1,potenciaquarto2,corrente2))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
a = 0
#Sala
while a == 0:
    qsala = int(input('Informe a quantidade de salas?\n1,2,3....\n'))

    if qsala == 1:
        areasala1 = float(input('Informe a Área da sala?\n'))
        perimetrosala1 = float(input('Informe o perímetro da sala?\n'))

        tugsala1 = perimetrosala1 // 5
        lumisala1 = areasala1 // 4
        potenciasala1 = ((tugsala1 * 100) + (lumisala1 * 60))
        potenciatot2 = potenciasala1
        correntesala1 = potenciasala1 / tensao
        print('Sala1\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciasala1, correntesala1))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
    elif qsala == 2:
        areasala1 = float(input('Informe a Área da sala 1?\n'))
        perimetrosala1 = float(input('Informe o perímetro da sala 1?\n'))
        areasala2 = float(input('Informe a Área da sala 2?\n'))
        perimetrosala2 = float(input('Informe o perímetro da sala 2?\n'))

        tugsala1 = perimetrosala1 // 5
        lumisala1 = areasala1 // 4
        tugsala2 = perimetrosala2 // 5
        lumisala2 = areasala2 // 4
        potenciasala1 = ((tugsala1 * 100) + (lumisala1 * 60))
        potenciasala2 = ((tugsala2 * 100) + (lumisala2 * 60))
        potenciatot2=potenciasala1+potenciasala2
        correntesala1 = potenciasala1 / tensao
        correntesala2 = potenciasala2 / tensao
        print('Sala 1\nPotência:{:.2f}W\nCorrente:{:.2f}A\nSala 2\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciasala1, correntesala1, potenciasala2, correntesala2))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
a = 0
#Cozinha
while a == 0:
    qcozinha = int(input('Informe a quantidade de cozinhas?\n1,2,3....\n'))

    if qcozinha == 1:
        areacozinha1 = float(input('Informe a Área da cozinha?\n'))
        perimetrocozinha1 = float(input('Informe o perímetro da cozinha?\n'))

        tugcozinha1 = perimetrocozinha1 // 3.5
        lumicozinha1 = areacozinha1 // 4
        potenciacozinha1 = ((tugcozinha1 * 100) + (lumicozinha1 * 60))
        potenciatot3 = potenciacozinha1
        correntecozinha1 = potenciacozinha1 / tensao
        print('Cozinha1\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciacozinha1, correntecozinha1))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
    elif qcozinha == 2:
        areacozinha1 = float(input('Informe a Área da cozinha 1?\n'))
        perimetrocozinha1 = float(input('Informe o perímetro da cozinha 1?\n'))
        areacozinha2 = float(input('Informe a Área da cozinha 2?\n'))
        perimetrocozinha2 = float(input('Informe o perímetro da cozinha 2?\n'))

        tugcozinha1 = perimetrocozinha1 // 3.5
        lumicozinha1 = areacozinha1 // 4
        tugcozinha2 = perimetrocozinha2 // 3.5
        lumicozinha2 = areacozinha2 // 4
        potenciacozinha1 = ((tugcozinha1 * 100) + (lumicozinha1 * 60))
        potenciacozinha2 = ((tugcozinha2 * 100) + (lumicozinha2 * 60))
        potenciatot3 = potenciacozinha1 + potenciacozinha2
        correntecozinha1 = potenciacozinha1 / tensao
        correntecozinha2 = potenciacozinha2 / tensao
        print('Cozinha 1\nPotência:{:.2f}W\nCorrente:{:.2f}A\nCozinha 2\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciacozinha1, correntecozinha1, potenciacozinha2, correntecozinha2))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
a = 0
#Banheiro
while a == 0:
    qbanheiro = int(input('Informe a quantidade de banheiro?\n1,2,3....\n'))

    if qbanheiro == 1:
        areabanheiro1 = float(input('Informe a Área da banheiro?\n'))
        perimetrobanheiro1 = float(input('Informe o perÍmetro da banheiro?\n'))

        tugbanheiro1 = perimetrobanheiro1 // 3.5
        lumibanheiro1 = areabanheiro1 // 4
        potenciabanheiro1 = ((tugbanheiro1 * 100) + (lumibanheiro1 * 60))
        potenciatot4 = potenciabanheiro1
        correntebanheiro1 = potenciabanheiro1 / tensao
        print('Banheiro1\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciabanheiro1, correntebanheiro1))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
    elif qbanheiro == 2:
        areabanheiro1 = float(input('Informe a Área da banheiro 1?\n'))
        perimetrobanheiro1 = float(input('Informe o perímetro da banheiro 1?\n'))
        areabanheiro2 = float(input('Informe a Área da banheiro 2?\n'))
        perimetrobanheiro2 = float(input('Informe o perímetro da banheiro 2?\n'))

        tugbanheiro1 = perimetrobanheiro1 // 3.5
        lumibanheiro1 = areabanheiro1 // 4
        tugbanheiro2 = perimetrobanheiro2 // 3.5
        lumibanheiro2 = areabanheiro2 // 4
        potenciabanheiro1 = ((tugbanheiro1 * 100) + (lumibanheiro1 * 60))
        potenciabanheiro2 = ((tugbanheiro2 * 100) + (lumibanheiro2 * 60))
        potenciatot4 = potenciabanheiro1+potenciabanheiro2
        correntebanheiro1 = potenciabanheiro1 / tensao
        correntebanheiro2 = potenciabanheiro2 / tensao
        print('Banheiro 1\nPotência:{:.2f}W\nCorrente:{:.2f}A\nBanheiro 2\nPotência:{:.2f}W\nCorrente:{:.2f}A'.format(potenciabanheiro1, correntebanheiro1, potenciabanheiro2, correntebanheiro2))
        a = int(input('aperte 0 para inserir os valores novamente\naperte 1 para continuar\n'))
#circuitos exclusivos
a = 0
ptue1=0
while a == 0:
    qtue = int(input('sua casa tera circuitos exclusivos para equipamentos de alta potência como chuveiro, arcoondicionados ou microondas?\n1 para sim e 0 para nรฃo\n'))
    if qtue == 0:
        a = 1
    elif qtue == 1:
        b = 0
        ptue1 = 0
        ptue2 = []
        while a == 0:
            ptue = float(input('informe a potência do equipamento\n'))
            ptue1 = ptue1 + ptue
            ptue2.append(ptue)
            qc = len(ptue2)
            print('A potência total dos circuitos exclusivos: {}W\n essas são as potências{}\n e você terá {} circuitos exclusivos'.format(ptue1,ptue2,qc))
            a = int(input('Se voce tiver mais circuitos exclusivos aperte o 0 senão 1 para continuar\n'))
#Padrão de entrada
#FINAL
potenciatotal = (potenciatot1+potenciatot2+potenciatot3+potenciatot4+ptue1)
correntedeprojeto = potenciatotal / tensao

a = 0

#PARTE WEB DOS MATERIAIS DO PADRÃO DE ENTRADA
import webbrowser
while a == 0:
    padrao = int(input('Informe o tipo do padrão\n1 para monofasico\n2 para bifásico\n3 para trifásico\n'))
    if padrao == 1:
        print('materiais para padrão de entrada monofásico:\n')
        webbrowser.open('http://servicos.coelba.com.br/comercial-industrial/Pages/Padr%C3%A3o%20de%20Entrada/monofasico.aspx')
        a = int(input('Pode continuar 1 para não 0 para sim\n'))
    elif padrao == 2:
        print('materiais para padrão de entrada bifásico:\n')
        webbrowser.open('http://servicos.coelba.com.br/comercial-industrial/Pages/Padr%C3%A3o%20de%20Entrada/bifasico.aspx')
        a = int(input('Pode continuar 1 para não 0 para sim\n'))

print('sua potência total: {:.2f}W\n, corrente de projeto : {:.2f}A\nPotência Sala: {:.2f}W\nPotência cozinha: {:.2f}W\nPotencia quartos: {:.2f}W\nPotência Banheiros: {:.2f}W\nPotência circuitos exclusivos{:.2f}W'.format(potenciatotal,correntedeprojeto,potenciatot2,potenciatot3,potenciatot1,potenciatot4,ptue1))