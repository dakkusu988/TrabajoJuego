import json

# Abre el archivo JSON "Logros.json" en modo lectura
with open('Logros.json', 'r') as archivo_json:
    # Carga los datos desde el archivo JSON
    datos = json.load(archivo_json)

# Obtenemos la lista de logros
logros = datos["logros"]

# Itera a través de los logros e imprime sus detalles
for logro in logros:
    print(f"Logro: {logro['nombre']}")
    print(f"Descripción: {logro['descripción']}")
    print(f"Progreso: {logro['progreso']}")
    print(f"Desbloqueado: {logro['desbloqueado']}")
    
    if logro['fechaDesbloqueo']:
        print(f"Fecha de desbloqueo: {logro['fechaDesbloqueo']}")

    else:
        print("Fecha de desbloqueo: No disponible")
        
    print()  # Línea en blanco para separar los logros
