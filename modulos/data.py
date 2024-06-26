from pathlib import Path

home = Path(__file__).parent.parent
ruta_j = Path(home/'base.json')
ruta_c = Path(home/'export.csv')
menup = ['Ver Listado de Pinturas',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas']