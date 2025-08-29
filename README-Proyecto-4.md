# Pokédex Interactiva con Python

Este es un proyecto de Pokédex interactiva desarrollada en Python. La aplicación se conecta a la PokeAPI, obtiene datos de un Pokémon específico y los muestra en una interfaz gráfica de usuario (GUI). Además, guarda la información consultada en un archivo JSON para futuras referencias.

Características
Consumo de API: Obtiene datos de Pokémon directamente de la PokeAPI.

Manejo de Errores: Gestiona los errores de conexión y las respuestas de la API (por ejemplo, cuando un Pokémon no se encuentra).

Interfaz Gráfica (GUI): Muestra la imagen y las estadísticas del Pokémon en una ventana limpia y organizada usando tkinter y Pillow.

Almacenamiento Local: Guarda los datos de cada Pokémon consultado en archivos .json dentro de una carpeta pokedex.

Navegación Interactiva: Permite al usuario buscar múltiples Pokémon en la misma sesión y salir del programa de forma controlada.

Requisitos
Para ejecutar este proyecto, necesitas tener Python 3.x y las siguientes bibliotecas instaladas. Puedes instalarlas usando pip:

Bash

pip install requests
pip install Pillow
tkinter generalmente viene preinstalado con Python, así que no es necesario instalarlo por separado.

Cómo Usar
Descarga el código: Clona el repositorio o descarga los archivos en tu computadora.

Instala las dependencias: Abre tu terminal y navega hasta la carpeta del proyecto. Ejecuta los comandos de instalación de requisitos mencionados anteriormente.

Ejecuta el programa: Desde la misma terminal, ejecuta el script principal:

Bash

python tu_script.py
Interactúa: Sigue las instrucciones en la terminal. Ingresa el nombre de un Pokémon para ver su información en la GUI. Para cerrar el programa, escribe salir en la terminal.

Estructura del Código
El proyecto está organizado en funciones modulares para una mejor legibilidad y mantenimiento:

get_image_from_url(url): Descarga una imagen desde una URL.

get_pokemon_data(pokemon_name): Se conecta a la API y obtiene los datos del Pokémon.

save_pokemon_data(pokemon_data): Guarda los datos procesados en un archivo JSON local.

show_pokemon_gui(pokemon_data, img_pil): Crea y muestra la ventana con la información del Pokémon.

main(): Orquesta el flujo del programa, incluyendo el bucle interactivo.

Autor
Proyecto creado por [tu_nombre].
