# Longitudes y cuadrantes
# Este programa combina dos funcionalidades principales:
1. Validación de la longitud de una palabra ingresada por el usuario.
2. Identificación del cuadrante de un punto dadas sus coordenadas X e Y.

print("Bienvenido al programa de longitudes y cuadrantes")

# --- Reto 1: Validación de la longitud de la palabra ---

Creamos una variable para almacenar la palabra que el usuario va a introducir.

Se inicializa vacía para que el bucle de validación pueda comenzar.

Palabra = ""

 Iniciamos un bucle 'while' que se repetirá continuamente
 
 hasta que la longitud de la palabra cumpla con las condiciones:
 
 que sea mayor o igual a 4 Y menor o igual a 8 caracteres.
 
    while not (len(Palabra) >= 4 and len(Palabra) <= 8):
Solicitamos al usuario que introduzca una palabra.

    Palabra = input("Introduce una palabra de cuatro a ocho caracteres: ")

Comprobamos la longitud de la palabra ingresada.

Si la longitud es menor que 4, significa que faltan letras.

    if len(Palabra) < 4:
Mostramos un mensaje informativo indicando cuántas letras faltan.

    print(f"Hacen falta letras. Solo tienes {len(Palabra)} letras.")
Si la longitud es mayor que 8, significa que sobran letras.

    elif len(Palabra) > 8:
Mostramos un mensaje informativo indicando cuántas letras sobran.

        print(f"Sobran letras. Tienes {len(Palabra)} letras.")
Si la longitud está entre 4 y 8 (inclusive), el bucle finalizará automáticamente
porque la condición 'while not (len(Palabra) >= 4 and len(Palabra) <= 8)'
se volverá falsa.

Una vez que la palabra tiene la longitud correcta, salimos del bucle.

Mostramos un mensaje de éxito, confirmando la palabra y su longitud.

    print(f"Tu palabra es \"{Palabra}\" y tiene {len(Palabra)} letras.")
    print("¡Tu palabra es correcta!")

---

# --- Reto 2: Identificación de cuadrantes ---

    print("\n--- Identificación de cuadrantes ---")

 Inicializamos las coordenadas X e Y a 0.
 
Esto es importante para que el bucle de validación de coordenadas se ejecute al menos una vez.

    x = 0
    y = 0

Iniciamos un bucle 'while' que continuará pidiendo coordenadas

hasta que ambas (x e y) sean diferentes de cero.

    while x == 0 or y == 0:
Usamos un bloque 'try-except' para manejar posibles errores de entrada.

Si el usuario ingresa algo que no es un número (ej. texto), se captura el error.

    try:
        # Solicitamos al usuario que ingrese la coordenada X y la convertimos a un número flotante.
        x = float(input("Ingrese la coordenada X (no puede ser 0): "))
        # Solicitamos al usuario que ingrese la coordenada Y y la convertimos a un número flotante.
        y = float(input("Ingrese la coordenada Y (no puede ser 0): "))

        # Después de obtener las entradas, verificamos si alguna de las coordenadas es cero.
        if x == 0 or y == 0:
            # Si alguna es cero, informamos al usuario y el bucle se repetirá.
            print("Las coordenadas no pueden ser cero. Por favor, inténtalo de nuevo.")
    except ValueError:
        # Si el usuario ingresó algo que no se pudo convertir a número (ej. letras),
        # mostramos un mensaje de error y el bucle se repetirá.
        print("Entrada inválida. Por favor, ingresa un número.")

# Una vez que tenemos coordenadas válidas (ninguna es cero), procedemos a determinar el cuadrante.

    # Cuadrante I: X positiva y Y positiva.
    if x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I.")
    # Cuadrante II: X negativa y Y positiva.
    elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II.")
    # Cuadrante III: X negativa y Y negativa.
    elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III.")
    # Cuadrante IV: X positiva y Y negativa.
    elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante IV.")
    
Nota: No se necesita un 'else' final porque la validación previa

asegura que x e y no serán 0, cubriendo así todos los cuadrantes posibles.
