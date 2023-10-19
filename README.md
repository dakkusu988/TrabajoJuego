#Guía del Código - Manejo de Logros en Python

Este código en Python utiliza la biblioteca requests para obtener datos desde una URL de internet, en este caso, un archivo JSON que contiene información sobre logros en un juego.
El programa permite realizar varias acciones relacionadas con estos logros, como buscar por nombre, mostrar todos los logros, filtrar por progreso y salir del programa.

#Instrucciones de Uso
#Requisitos

Asegúrate de tener instalada la biblioteca requests.
Puedes instalarla usando pip si aún no la tienes:
- pip install requests

#Ejecución

1. Abre un entorno de Python y copia el código proporcionado.
2. Ejecuta el programa.

#Uso

El programa proporciona una interfaz de línea de comandos para explorar y buscar logros en un juego desde un archivo JSON en línea.

A continuación, se explican las características y cómo utilizarlas:

#Características del Programa

1. Búsqueda de Logros por Nombre:

   Permite al usuario buscar logros por nombre o parte del nombre. Luego, muestra los logros que coinciden con la búsqueda.

2. Visualización de Todos los Logros:

   Muestra todos los logros en dos secciones: logros desbloqueados y logros bloqueados.

4. Filtrado de Logros por Progreso (No Desbloqueados):

   Filtra y muestra los logros no desbloqueados por progreso, ordenándolos de mayor a menor.

6. Salir del Programa:

   Permite al usuario salir del programa.

#Documentación de Dependencias

Este programa depende de la biblioteca requests para realizar solicitudes HTTP. 
Si la biblioteca no está instalada, se debe instalar utilizando el siguiente comando:
- pip install requests
  
#Gestión de Errores

El programa maneja errores relacionados con la obtención de datos desde la URL de Internet y la interacción del usuario.
En caso de errores, se mostrarán mensajes explicativos para guiar al usuario.

