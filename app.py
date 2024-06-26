from modulos.construccion import construir_menu, sol_ans
from modulos.data import menup, ruta_j, ruta_c
from modulos.agregar import agregar
from modulos.ver_listado import ver_pintura
from modulos.buscar import buscar, stl_codigo
from modulos.eliminar import stl_code, borrar
from modulos.exportar import exportar
import os

while True:
    construir_menu(menup)
    ans = sol_ans()
    os.system('cls')
    if ans == '1':
        ver_pintura(ruta_j)
    elif ans == '2':
        buscar(stl_codigo(), ruta_j)
    elif ans == '3':
        agregar(ruta_j)
    elif ans == '4':
        borrar(stl_code(), ruta_j)
    elif ans == '5':
        exportar(ruta_j, ruta_c)
    else:
        print('Error: Opcion no valida')
