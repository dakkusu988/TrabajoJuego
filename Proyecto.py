import json

# Función para buscar logros por nombre
def buscar_por_nombre():
    busqueda = input("Ingrese el nombre o parte del nombre del logro: ")
    print(f"Logros que contienen '{busqueda}':")
    for logro in logros:
        if busqueda.lower() in logro['nombre'].lower():
            mostrar_logro(logro)

# Función para mostrar todos los logros
def mostrar_todos():
    print("Todos los logros:")
    print()
    print("LOGROS DESBLOQUEADOS:")
    print("----------------------")
    for logro in logros:
        if logro['desbloqueado']:
            mostrar_logro(logro)
    print()
    print("LOGROS BLOQUEADOS:")
    print("----------------------")
    for logro in logros:
        if not logro['desbloqueado']:
            mostrar_logro(logro, mostrar_fecha=False)

# Función para filtrar logros no desbloqueados por progreso (de mayor a menor)
def filtrar_por_progreso():
    print("Logros no desbloqueados con progreso de mayor a menor:")
    logros_no_desbloqueados = [logro for logro in logros if not logro['desbloqueado']]
    logros_no_desbloqueados.sort(key=lambda x: x['progreso'], reverse=True)
    for logro in logros_no_desbloqueados:
        mostrar_logro(logro)

# Función para mostrar un logro con todos sus detalles (incluyendo progreso y meta)
def mostrar_logro(logro, mostrar_fecha=True):
    print()
    print(f"Logro: {logro['nombre']}")
    print(f"Descripción: {logro['descripción']}")
    print(f"Progreso: {logro['progreso']}/{logro['meta']}")  # Mostrar progreso y meta
    print(f"Desbloqueado: {logro['desbloqueado']}")
    if mostrar_fecha and logro['desbloqueado'] and logro['fechaDesbloqueo']:
        print(f"Fecha de desbloqueo: {logro['fechaDesbloqueo']}")

# Abrir el archivo JSON "Logros.json" en modo lectura
with open('Logros.json', 'r') as archivo_json:
    # Cargar los datos desde el archivo JSON
    datos = json.load(archivo_json)

# Obtener la lista de logros
logros = datos["logros"]

while True:
    # Agregar una línea de separación
    print("=========================================")

    # Solicitar información al usuario
    print("Elija una opción:")
    print("1. Filtrar logros por nombre")
    print("2. Mostrar todos los logros")
    print("3. Filtrar logros no desbloqueados por progreso (de mayor a menor)")
    print("4. Salir")
    print()  # Agregar un espacio en blanco

    opcion = input("Ingrese el número de la opción deseada: ")
    print()  # Agregar un espacio en blanco

    # Diccionario de funciones para simular un switch
    opciones = {
        "1": buscar_por_nombre,
        "2": mostrar_todos,
        "3": filtrar_por_progreso,
        "4": lambda: exit(),
    }

    # Obtener la función correspondiente a la opción ingresada
    funcion = opciones.get(opcion, lambda: print("Opción no válida. Por favor, ingrese un número válido de 1 a 4."))
    print()  # Agregar un espacio en blanco

    # Ejecutar la función
    funcion()
    print()  # Agregar un espacio en blanco
