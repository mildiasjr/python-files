def maximiza(string_hora):
    lista_hora = []
    lista_max = []
    x = 0

    for num in string_hora:
        lista_hora.append(num)
        if lista_hora[x] == '1':
            lista_max.append(['   ▄█  ',
                              '  ▀▀█  ',
                              '    █  ',
                              '  ▄▄█▄▄'])

        elif lista_hora[x] == '2':
            lista_max.append([' ▄▀▀▀▀▄',
                              '    ▄▄▀',
                              '  ▄▀   ',
                              ' █▄▄▄▄▄'])

        elif lista_hora[x] == '3':
            lista_max.append([' ▄▀▀▀▀▄',
                              '    ▄▄▀',
                              '      █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '4':
            lista_max.append([' █    █',
                              ' █▄▄▄▄█',
                              '      █',
                              '      █'])

        elif lista_hora[x] == '5':
            lista_max.append([' █▀▀▀▀▀',
                              ' █▄▄▄▄▄',
                              '      █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '6':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' █▄▄▄▄  ',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '7':
            lista_max.append([' ▀▀▀▀▀█',
                              '     █ ',
                              '    █  ',
                              '   █   '])

        elif lista_hora[x] == '8':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' ▀▄▄▄▄▀',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '9':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' ▀▄▄▄▄█',
                              '      █',
                              '  ▄▄▄▄▀'])

        elif lista_hora[x] == '0':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' █    █',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])
        elif lista_hora[x] == ':':
            lista_max.append(['       ',
                              '   ▀   ',
                              '   ▀   ',
                              '       '])
        x += 1
    return lista_max

def maximiza_t(string_hora):
    lista_hora = []
    lista_max = []
    x = 0

    for num in string_hora:
        lista_hora.append(num)
        if lista_hora[x] == '1':
            lista_max.append(['   ▄█  ',
                              '  ▀▀█  ',
                              '    █  ',
                              '  ▄▄█▄▄'])

        elif lista_hora[x] == '2':
            lista_max.append([' ▄▀▀▀▀▄',
                              '    ▄▄▀',
                              '  ▄▀   ',
                              ' █▄▄▄▄▄'])

        elif lista_hora[x] == '3':
            lista_max.append([' ▄▀▀▀▀▄',
                              '    ▄▄▀',
                              '      █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '4':
            lista_max.append([' █    █',
                              ' █▄▄▄▄█',
                              '      █',
                              '      █'])

        elif lista_hora[x] == '5':
            lista_max.append([' █▀▀▀▀▀',
                              ' █▄▄▄▄▄',
                              '      █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '6':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' █▄▄▄▄  ',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '7':
            lista_max.append([' ▀▀▀▀▀█',
                              '     █ ',
                              '    █  ',
                              '   █   '])

        elif lista_hora[x] == '8':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' ▀▄▄▄▄▀',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])

        elif lista_hora[x] == '9':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' ▀▄▄▄▄█',
                              '      █',
                              '  ▄▄▄▄▀'])

        elif lista_hora[x] == '0':
            lista_max.append([' ▄▀▀▀▀▄',
                              ' █    █',
                              ' █    █',
                              ' ▀▄▄▄▄▀'])
        elif lista_hora[x] == ':':
            lista_max.append(['       ',
                              '   ▀   ',
                              '   ▀   ',
                              '       '])
        x += 1
    return lista_max