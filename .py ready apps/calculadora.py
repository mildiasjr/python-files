import PySimpleGUI as sg

sg.theme('Reddit')
teclado = [
    [sg.Button('C', size=(6, 2)), sg.Button(
        '/', size=(6, 2)), sg.Button('*', size=(6, 2))],
    [sg.Button('7', size=(6, 2)), sg.Button(
        '8', size=(6, 2)), sg.Button('9', size=(6, 2))],
    [sg.Button('4', size=(6, 2)), sg.Button(
        '5', size=(6, 2)), sg.Button('6', size=(6, 2))],
    [sg.Button('1', size=(6, 2)), sg.Button(
        '2', size=(6, 2)), sg.Button('3', size=(6, 2))],
    [sg.Button('0', size=(14, 2)), sg.Button(',', size=(6, 2))]]
lateral = [[sg.Button('-', size=(6, 2))], [sg.Button('+', size=(6, 4))],
           [sg.Button('=', size=(6, 6))]]

leiaute = [[sg.Output(size=(35, 3), key='saida', sbar_width=0, font='Consolas')],
           [sg.Column(teclado), sg.Column(lateral)]]

janela = sg.Window('Calculadora', size=(300, 320),
                   layout=leiaute, finalize=True)

calculo = []
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    # Todos os números 0-9 sesão inseridos no cálculo, poupou 20 linhas de codigo.
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
    elif event == 'C':
        calculo.clear()

    # Transforma a lista calculo em uma string visor, essa é desepejada no output
    visor = ''.join(calculo)
    janela['saida'].update(visor)

    # Tenta realizar a operação matemática expressa na string visor
    if event == '=':
        try:
            result = eval(visor)
        except:
            result = "Erro"
        finally:
            calculo.clear()
            janela['saida'].update(result)
