# Programado por Milton C Dias Junior. Ago-2022
import sys, os, time, winsound

from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
clear = lambda: os.system('cls')

def forca_joga(palavr_entra, palavr_chav, letras_list) :

    guess_palavra: list = []
    guess_letra: str = "1"
    enforcar: int = 0
    gotoxy: str = ''
    letra_found: bool = False
    letra_entrada: list = []
    jogado = False

    # Jogo
    clear()
    print('\033[5;25H' + '\033[47;30m' + " J O G O   D A   F O R C A " + '\033[0m\n')

    # Desenha os espaços das letras
    print('\033[8;25H', end='')
    for y in palavr_chav:              # Retirei o range(len()). A propria variavel é um iteravel.
        print('___ ', end='')          # não é preciso o inteiro da variavel retornardo por len()
                                       # pois faz o loop nos elementos da var, mas não a imprime

    # Imprime msg do total de letras da palavra a ser descoberta
    print(f": {len(palavr_chav)} letras")

    # Entrada da letra
    while enforcar < 7 and guess_palavra != palavr_chav :
        while True:
              guess_letra = input('\033[10;10H' + 'Adivinhe a letra: ')
           # Força a variavel possuir apenas um caracter, mesmo que o usuario digite mais
              guess_letra = guess_letra[0]

           # Apaga da tela os valores entrados
              print('\033[10;28H'+"                                                      ")

           # Controla se a entrada é um caracter alfabetico ou imprime msg erro
              if guess_letra.isalpha() == True:
                  if guess_letra not in letra_entrada:
                       letra_entrada.extend(guess_letra)         # Armazena e imprime a lista de letras entradas
                       print('\033[22;10H' + "Letras Usadas: ", letra_entrada)
                       break
                  else:
                      print('\033[12;10H' + "Letra já usada. Entre com outra letra")
                      winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                      print('\033[12;10H' + "                                      ")
                      continue
              else:
                  print('\033[12;10H'+"Entre apenas com letras de A a Z")
                  winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                  print('\033[12;10H'+"                                ")
                  continue


        # Compara se letra entrada é certa e imprime a letra no seu espaço correto.
        letra_found = False
        for i in range(len(letras_list)) :
            
            if letras_list[i] == guess_letra :
                gotoxy ='[8;' + str(26 + 4*i) +'H'
                print('\033' + gotoxy + guess_letra)
                guess_palavra.append(guess_letra)
                guess_palavra = sorted(guess_palavra)
                letra_found = True
                time.sleep(0.5)

        if letra_found == False :
            enforcar = enforcar + 1

            if enforcar == 1 :
                print('\033[18;75H' + '       /      \\')
                print('\033[19;75H' + ' _____/        \\_____')

            if enforcar == 2 :
                print('\033[14;75H' + '      ( ')
                print('\033[15;75H' + '      │ ')
                print('\033[16;75H' + '      │ ')
                print('\033[17;75H' + '     ()')

            if enforcar == 3 :
                print('\033[14;83H' + '|────┐       | | ')
                print('\033[15;83H' + '│    │       | | ')
                print('\033[16;83H' + '│    │       | |')
                print('\033[17;83H' + '└────|       |_|')

            if enforcar == 4 :
                print('\033[14;90H' + ')')
                print('\033[15;90H' + '│')
                print('\033[16;90H' + '│')
                print('\033[17;90H' + '()')

            if enforcar == 5 :
                print('\033[13;75H' + '          | |        | |')

            if enforcar == 6 :
                print('\033[08;75H' + '     ----------------|-|')
                print('\033[09;75H' + '     ----------------| |')
                print('\033[10;75H' + '     |   /   \       | |')
                print('\033[11;75H' + '     |  | O O |      | |')
                print('\033[12;75H' + '     |   \ - /       | |')

            if enforcar == 7 :
                print('\033[12;20H' + '\033[33;41m' + 'PERDEU!! GAME OVER' + '\033[0m')
                print('\033[13;20H' + '\033[33;42m' + 'A PALAVRA CORRETA ERA '+ str(palavr_entra) + '\033[0m')
                print('\033[10;75H' + '     |   /   \ ')
                print('\033[11;75H' + '     |  | x x |')
                print('\033[12;75H' + '     |   \   / ')
                print('\033[13;75H' + '     |----|-|--')



    if guess_palavra == palavr_chav :
      print('\033[12;20H' + '\033[32;40m' + 'VOCE GANHOU!! PARABÉNS' + '\033[0m')

      time.sleep(1)



jogar: bool = True

while jogar == True:

    jogado = False
    palavr_chav: list = []
    letras_list: list = []

    clear()
    print("Jogo da Forca \n")

    # Entrada da palavra a ser descoberta
    palavr_entra = input("Entre com a palavra-chave: ")

    # Insere espaço entre letras, separa as letras em lista, organiza alfabeticam// as letras
    palavr_entra = " ".join(palavr_entra)
    letras_list = palavr_entra.split()
    palavr_chav = sorted(letras_list)

    # Ordena letras em
    # lista de PALAVR_CHAV para comparação
    palavr_chav = sorted(letras_list)

    # Confirmação de inicio do jogo
    inicia = input("Inicia agora o jogo? (S/N)")
    if inicia.capitalize() == "S":
        forca_joga(palavr_entra, palavr_chav, letras_list)
        jogado = True
        reinicia = ""
        time.sleep(.5)
    else:
      break

    # Confirmação de novo jogo
    if jogado == True:
        while True:
              reinicia = input('\033[15;10H'+"Quer jogar novamente? (S/N)")
              reinicia = reinicia.capitalize()
              if reinicia == "S":
                  break
              elif reinicia == "N":
                  jogar = False
                  clear()
                  break
              else:
                  print('\033[16;10H'+"Entre com a letra S para SIM ou N para NAO")
                  winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                  print('\033[16;10H'+"                                          ")
                  continue