'''
Funciones de aplicacion principal
'''
def construir_menu(lista):
    for ind, opt in enumerate(lista):
        print(f'{ind + 1}. {opt}')


def sol_ans():
    resp = input('¿Que quieres hacer?\n')
    return resp
