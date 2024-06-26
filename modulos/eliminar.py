import json

def stl_code():
    code = input('Ingresa el codigo de la pintura a eliminar')
    if code.isnumeric():
        return int(code)
    

def borrar(dato, jsonf):
    if dato == None:
        print('La base de datos no existe!')
    else:
        with open(jsonf, mode= 'r') as stream:
            json_file = json.load(stream)
            for pintura in json_file:
                if pintura["codigo"] == dato:
                    json_file.remove(pintura)
                    print('Pintura borrada exitosamente')
            with open(jsonf, mode= 'w') as stream:
                json.dump(json_file, stream)