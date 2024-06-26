import json
import os

def agregar(jsonf):
    if not jsonf.exists():
        jsonf.touch()
        print('La base de datos no existia, pero ahora ha sido creada')
    elif jsonf.stat().st_size == 0:
        json_file = []
        codp = 380560
    else:
        with open(jsonf, mode= 'r') as stream:
            json_file = json.load(stream)
            codp = []
            for pintura in json_file:
                codp.append(pintura["codigo"])
            codp = max(codp) + 1
    while True:
        print('Ingresa el nombre del color')
        nomp = input('Nombre: ').upper()
        ans = input(f'Nombre: {nomp}\n¿Es correcto?\n1. Si\2. No')
        if ans == '1':
            break
        else:
            os.system('cls')
    while True:
        print('Ingresa el tipo de la pintura (Acrilico o Latex)')
        tipo = input('Nombre: ').upper()
        ans = input(f'Nombre: {tipo}\n¿Es correcto?\n1. Si\2. No')
        if ans == '1':
            break
        else:
            os.system('cls')
    while True:
        print('Ingresa valor de la pintura')
        valor = input('Valor: ').upper()
        ans = input(f'Valor: {valor}\n¿Es correcto?\n1. Si\2. No')
        if ans == '1' and ans.isnumeric():
            ans = int(valor)
            break
        else:
            os.system('cls')
            print('Solo puedes ingresar numeros!')
    while True:
        print('Ingresa el stock de la pintura')
        stock = input('Stock: ').upper()
        ans = input(f'Stock: {stock}\n¿Es correcto?\n1. Si\2. No')
        if ans == '1' and ans.isnumeric():
            ans = int(stock)
            break
        else:
            os.system('cls')
            print('Solo puedes ingresar numeros!')
    data = {'codigo': codp,
            'nombre': nomp,
            'tipo': tipo,
            'valor': valor,
            'stock': stock}
    json_file.append(data)
    with open(jsonf, mode= 'w') as stream:
        json.dump(json_file, stream)
        print('Pintura agregada exitosamente!')