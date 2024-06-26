import json

def ver_pintura(jsonf):
    with open(jsonf, mode= 'r') as stream:
        json_file = json.load(stream)
        for pintura in json_file:
            print(f'CODIGO: {pintura["codigo"]}')
            print(f'NOMBRE: {pintura["nombre"]}')
            print(f'TIPO: {pintura["tipo"]}')
            print(f'VALOR: {pintura["valor"]}')
            print(f'STOCK: {pintura["stock"]}')