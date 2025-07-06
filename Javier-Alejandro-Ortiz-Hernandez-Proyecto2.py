
print("Bienvenido al programa de longitudes y cuadrantes")
# Este programa solicita al usuario una palabra y valida su longitud
#cololcamos una variable para almacenar la palabra
Palabra= ""

# Validación de la longitud de la palabra
#colocamos un bucle que se repite hasta que la palabra tenga entre 4 y 8 caracteres
while not (len(Palabra) >= 4 and len(Palabra) <= 8):
    Palabra= input("Introduce una palabra de cuatro a ocho caracteres: ")
# Comprobamos si la longitud de la palabra es menor que 4 o mayor que 8
    # Si es menor que 4, mostramos un mensaje indicando que faltan letras
    if len(Palabra) < 4:
        print(f"Hacen falta letras. Solo tienes {len(Palabra)} letras")
    # Si es mayor que 8, mostramos un mensaje indicando que sobran letras
    elif len(Palabra) > 8:
        print(f"sobran letras. Tienes {len(Palabra)} letras")
    # Si la longitud es correcta, salimos del bucle
# Si la longitud es correcta, mostramos un mensaje de éxito y la longitud de la palabra        
print(f"Tu palabra es \"{Palabra}\" y tiene {len(Palabra)} letras")      
print("tu palabra es correcta")

# --- Identificación de cuadrantes ---
x = 0
y = 0

# Bucle para asegurar que las coordenadas no sean cero
while x == 0 or y == 0:
    # Pedimos al usuario que ingrese las coordenadas X e Y
    #try es utilizado para manejar errores de entrada
    # Si el usuario ingresa un valor no numérico, se captura la excepción ValueError
    try:
        x = float(input("Ingrese la coordenada X (no puede ser 0): "))
        y = float(input("Ingrese la coordenada Y (no puede ser 0): "))

        if x == 0 or y == 0:
            print("Las coordenadas no pueden ser cero. Por favor, inténtalo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")

# Determinamos el cuadrante
if x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuadrante IV")