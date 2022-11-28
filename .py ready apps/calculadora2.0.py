import PySimpleGUI as sg
import math

sg.theme('Reddit')
teclado = [[sg.Button('C', size=(6, 2), font='Consolas'), sg.Button(
    '√', size=(6, 2), font='Consolas'), sg.Button('^', size=(6, 2), font='Consolas')],
    [sg.Button('%', size=(6, 2), font='Consolas'), sg.Button(
        '/', size=(6, 2), font='Consolas'), sg.Button('*', size=(6, 2), font='Consolas')],
    [sg.Button('7', size=(6, 2), font='Consolas'), sg.Button(
        '8', size=(6, 2), font='Consolas'), sg.Button('9', size=(6, 2), font='Consolas')],
    [sg.Button('4', size=(6, 2), font='Consolas'), sg.Button(
        '5', size=(6, 2), font='Consolas'), sg.Button('6', size=(6, 2), font='Consolas')],
    [sg.Button('1', size=(6, 2), font='Consolas'), sg.Button(
        '2', size=(6, 2), font='Consolas'), sg.Button('3', size=(6, 2), font='Consolas')],
    [sg.Button('0', size=(14, 2), font='Consolas'), sg.Button(',', size=(6, 2), font='Consolas')]]

lateral = [[sg.Button('←', size=(6, 2), font='Consolas')], [sg.Button('-', size=(6, 2), font='Consolas')], [sg.Button('+', size=(6, 4), font='Consolas')],
           [sg.Button('=', size=(6, 6), font='Consolas')]]

leiaute = [[sg.Output(size=(35, 3), key='saida', sbar_width=0, font='Consolas')],
           [sg.Column(teclado), sg.Column(lateral, pad=1)]]

janela = sg.Window('Calculadora', size=(315, 420),
                   layout=leiaute, finalize=True)

calculo = []
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    # Todos os números 0-9 ssão inseridos no cálculo, poupou 20 linhas de codigo.
    elif event.isdigit() == True:
        calculo.append(event)
    # Inserção no cálculo dos demais eventos
    elif event == ',':
        calculo.append('.')
    elif event == '/':
        calculo.append('/')
    elif event == '*':
        calculo.append('*')
    elif event == '-':
        calculo.append('-')
    elif event == '+':
        calculo.append('+')
    elif event == '%':
        calculo.append('*0.01')
    elif event == '^':
        calculo.append('**')

    elif event == 'C':
        calculo.clear()
    elif event == '←':
        calculo.pop()

    # Transforma a lista calculo em uma string visor, essa é desepejada no output
    visor = ''.join(calculo)
    janela['saida'].update(visor)

    if event == '√':
        try:
            radic = int(visor)
            result = math.sqrt(radic)
        except:
            result = "Erro"
        finally:
            calculo.clear()
            janela['saida'].update(result)

    # Tenta realizar a operação matemática expressa na string visor
    if event == '=':
        try:
            result = eval(visor)
        except:
            result = "Erro"
        finally:
            calculo.clear()
            janela['saida'].update(result)
