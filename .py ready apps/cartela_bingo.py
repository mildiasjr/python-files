import random

# gerar cartelas do bingo
flag_rand = True
cartela = [['B', '', '', '', '', ''],      # Shape da Array (lista de listas) Cartela de Bingo
           ['I', '', '', '', '', ''],
           ['N', '', '', '', '', ''],
           ['G', '', '', '', '', ''],
           ['O', '', '', '', '', '']]

while True:
    print('*** GERADOR DE CARTELAS DE BINGO ***\n')
    vezes = int(input("Quantas cartelas você quer gerar: "))

    for y in range(0, vezes):           # Cria o for para fazer o loop e gerar cartelas quantas vezes o user escolher.

        for x in range(0, 5):           # loop para as linhas da array

            for n in range(1, 6):       # loop para as elementos da linha da array

                while flag_rand == True:  # Loop para gerar o número aleatório e guardar na array
                    if x == 0:
                        numer = str(random.randint(1, 19))      #gera o número de 1 a 19 para a coluna B
                    else:
                        numer = str(random.randint((x*20), 19+(x*20))) #gera o número de 20 a 39 etc para a coluna I,N,G,O
                    if numer in cartela[x]:                 #
                        pass                                # Primeiro compara se o número gerado já existe na array
                    else:                                   # Se existe, loop e gera de novo
                        flag_rand = False                   # Se não, guarda o número e quebra o loop
                        cartela[x][n] = numer               # 
                flag_rand = True               # Reseta a var_flag em True para poder rodar de novo o loop de geração de no.
        cartela[2][3] = "--"                   # Define o valor da linha 2 elemento 3 como vazio conforme a regra das cartelas
        for j in range(0,5):
            print(f"{cartela[j]}")    # imprime a cartela toda, linha a linha
        print('\n\n')                 # espaço entre cada impressão de cartelas

    # Controle de reinicializaçao
    cont = input('Deseja reexecutar? (S/N)')
    cont = cont.upper()
    if cont == "S":
        continue
    else:
        break
