import requests  # Para hacer solicitudes HTTP a la API
import json      # Para manejar datos JSON y guardarlos en archivos
import os        # Para manejar archivos y directorios en el sistema
import tkinter as tk  # Para la interfaz gráfica de usuario
from PIL import Image, ImageTk  # Para manejar imágenes en Tkinter
import webbrowser  # Para abrir URLs en el navegador predeterminado

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Función para descargar y abrir una imagen desde una URL usando requests y PIL
def get_image_from_url(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Lanza un error para códigos de estado incorrectos
        
        # Abre la imagen desde el contenido de la respuesta usando PIL
        img = Image.open(response.raw) 
        return img
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return None
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Función para obtener datos del Pokémon desde la API
def get_pokemon_data(pokemon_name):
    # Convertimos a minúsculas para evitar errores
    pokemon_name = pokemon_name.lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}" # URL de la API
    
    try:
        response = requests.get(url)
        # Verificamos si la solicitud fue exitosa (código 200)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: No se encontró el Pokémon '{pokemon_name}'.")
            return None
        else:
            print(f"Error al conectar con la API: Código de estado {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Función para guardar los datos en un archivo JSON
def save_pokemon_data(pokemon_data):
    if not pokemon_data:
        return

    # Crear la carpeta 'pokedex' si no existe
    pokedex_folder = "pokedex"
    if not os.path.exists(pokedex_folder):
        os.makedirs(pokedex_folder)
        
    # Crear el nombre del archivo JSON
    file_name = f"{pokemon_data['name'].lower()}.json"
    file_path = os.path.join(pokedex_folder, file_name)
    
    # Guardar los datos en el archivo
    with open(file_path, "w") as f:
        json.dump(pokemon_data, f, indent=4)
        
    print(f"\n¡Información de {pokemon_data['name']} guardada en '{file_path}' exitosamente!")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# función para mostrar la imagen y los datos del Pokémon en una ventana de Tkinter
def show_pokemon_gui(pokemon_data, img_pil):
    if not pokemon_data:
        return

    window = tk.Tk()
    window.title(f"Pokédex: {pokemon_data['name']}")

    # --- Frame para la Imagen ---
    image_frame = tk.Frame(window, bd=2, relief="groove")
    image_frame.pack(pady=10)

    if img_pil:
        # Redimensionar la imagen si es muy grande para la ventana
        img_pil.thumbnail((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_pil)
        
        image_label = tk.Label(image_frame, image=img_tk)
        image_label.pack()
        image_label.image = img_tk  # Guardar referencia para evitar que sea eliminada
    else:
        no_image_label = tk.Label(image_frame, text="No se pudo cargar la imagen", fg="red")
        no_image_label.pack()
    
    # --- Frame para las Estadísticas ---
    stats_frame = tk.Frame(window, bd=2, relief="groove", padx=10, pady=10)
    stats_frame.pack(pady=10, fill="x")

    # Título del Pokémon
    name_label = tk.Label(stats_frame, text=f"{pokemon_data['name']}", font=("Arial", 24, "bold"), fg="blue")
    name_label.pack(pady=5)

    # Separador
    tk.Frame(stats_frame, height=2, bd=1, relief="sunken").pack(fill="x", padx=5, pady=5)

    # Detalles del Pokémon
    details = [
        f"Peso: {pokemon_data['weight']} kg",
        f"Tamaño: {pokemon_data['height']} m",
        f"Tipos: {', '.join(pokemon_data['types']).capitalize()}",
        f"Habilidades: {', '.join(pokemon_data['abilities']).capitalize()}",
        f"Algunos Movimientos: {', '.join(pokemon_data['moves']).capitalize()}"
    ]

    for detail in details:
        label = tk.Label(stats_frame, text=detail, font=("Arial", 12), anchor="w")
        label.pack(fill="x", padx=10)

    # URL de la Pokédex oficial como un enlace
    pokedex_url = f"https://www.pokemon.com/el/pokedex/{pokemon_data['name'].lower()}"
    url_label = tk.Label(stats_frame, text="Ver en la Pokédex oficial", 
                         font=("Arial", 9, "underline"), fg="blue", cursor="hand2")
    url_label.pack(fill="x", padx=10, pady=5)
    url_label.bind("<Button-1>", lambda e: webbrowser.open_new(pokedex_url))

    window.mainloop()
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Función principal (main) que orquesta todo el programa
def main():
    print("--- ¡Bienvenido a la Pokédex! ---")
    while True:
        pokemon_name = input("Ingresa el nombre de un Pokémon (o escribe 'salir' para terminar): ")

        if pokemon_name.lower() == 'salir':
            print("¡Hasta la próxima!")
            break  # Esto rompe el bucle y termina el programa

        # Obtiene los datos crudos del Pokémon
        pokemon_data_raw = get_pokemon_data(pokemon_name)

        if pokemon_data_raw:
            # Procesa los datos para que sean más fáciles de usar
            processed_data = {
                "name": pokemon_data_raw['name'].capitalize(),
                "weight": pokemon_data_raw['weight'] / 10,
                "height": pokemon_data_raw['height'] / 10,
                "types": [poke_type['type']['name'] for poke_type in pokemon_data_raw['types']],
                "abilities": [ability['ability']['name'] for ability in pokemon_data_raw['abilities']],
                "moves": [move['move']['name'] for move in pokemon_data_raw['moves'][:5]],
                "image_url": pokemon_data_raw['sprites']['front_default']
            }

            # Guarda los datos procesados en un archivo JSON
            save_pokemon_data(processed_data)

            # Descarga la imagen
            img_pil = None
            if processed_data['image_url']:
                img_pil = get_image_from_url(processed_data['image_url'])

            # Muestra la GUI con todos los datos
            show_pokemon_gui(processed_data, img_pil)
        else:
            print("No se pudo obtener información del Pokémon o no existe.")

if __name__ == "__main__":
    main()