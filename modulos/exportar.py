import json
import csv
def exportar(rutaj, rutac):
    if not rutaj.exists() or rutaj.stat().st_size == 0:
        print('El archivo esta vacio o no existe!')
    else:
        if not rutac.exists():
            rutac.touch()
        else:
            rutac.unlink()
            rutac.touch()
    with open(rutac, mode = 'r') as stream:
        json_file = json.load(stream)
        for pintura in json_file:
            line = [pintura["codigo"],
                    pintura["nombre"],
                    pintura["tipo"],
                    pintura["valor"],
                    pintura["stock"]]
            with open(rutac, mode= 'a', newline= '') as stream:
                writer = csv.writer(stream)
                writer.writerow(line)

        