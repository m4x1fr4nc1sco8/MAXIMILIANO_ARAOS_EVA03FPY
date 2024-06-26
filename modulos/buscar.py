import json

def buscar(dato, jsonf):
    if not jsonf.exists():
        print('La base de datos no existe!')
    elif jsonf.stat().st_size == 0:
        print('La base de datos esta vacia!')
    else:
        with open(jsonf, mode= 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                if str(pintura["codigo"]) == dato or dato.upper() in pintura["nombre"]:
                    print(f'CODIGO: {pintura["codigo"]}')
                    print(f'NOMBRE: {pintura["nombre"]}')
                    print(f'TIPO: {pintura["tipo"]}')
                    print(f'VALOR: {pintura["valor"]}')
                    print(f'STOCK: {pintura["stock"]}')
    
def stl_codigo():
    resp = input('Ingresa el codigo o nombre de la pintura a buscar')
    return resp
                
