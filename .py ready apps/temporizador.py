import time
import os
import sys
import winsound
from _maxfont import maximiza
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
def clear(): return os.system('cls')


##########
clear()
print("Temporizador\n")
hini = int(input("Minuto inicial (59 a 0): "))
mini = int(input("Segundo inicial (59 a 0): "))
print('\n\n')

# Beep de inicio
winsound.Beep(500, 150)
time.sleep(0.7)

# Loops de contagem regressiva
for h in range(hini, -1, -1):
    for m in range(mini, -1, -1):
        string_vai = f' {h:02}:{m:02}'  # Formatação da string minuto e segundo

        # Envio da string formatada para a função maximiza, retorna caracteres
        hora_retorna = maximiza(string_vai)

        for i in range(len(hora_retorna)):
            col_var = 15 + (i * 7)
            gotoy = str(col_var) + 'H'

            for j in range(4):
                lin_var = 7 + j
                gotox = '['+str(lin_var)+';'
                print('\033' + gotox + gotoy + hora_retorna[i][j])

        time.sleep(1)

        if h == 0 and m == 1:
            winsound.Beep(500, 500)
    mini = 59
