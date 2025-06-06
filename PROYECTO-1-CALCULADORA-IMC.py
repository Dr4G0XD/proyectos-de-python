# Índice de Masa Corporal (IMC)
# Este programa va a calcular el Índice de Masa Corporal (IMC) de una persona

def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

def nivel_peso(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidad I"
    elif 35 <= imc < 39.9:
        return "Obesidad II"
    elif 40 <= imc < 49.9:
        return "Obesidad III"
    else:
        return "Obesidad IV"

def calcular_peso_ideal(altura):
    imc_min = 18.5
    imc_max = 24.9
    peso_ideal_min = imc_min * (altura ** 2)
    peso_ideal_max = imc_max * (altura ** 2)
    return peso_ideal_min, peso_ideal_max

# --- Bucle principal para permitir nuevas consultas ---
while True:
    print("\n--- Cálculo del Índice de Masa Corporal (IMC) ---")

    # Inicializamos las variables con un valor que indica que no han sido validadas
    nombre = None
    peso = None
    altura = None

    # --- Bucle para toda la validación de entrada (nombre, peso, altura) ---
    while True:
        # --- Validar el Nombre ---
        if nombre is None: # Solo pide el nombre si aún no es válido
            nombre_input = input("Por favor, introduce tu nombre (entre 2 y 50 caracteres): \n")
            if not nombre_input.strip():
                print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
                continue # Vuelve al inicio del bucle principal
            if len(nombre_input.strip()) < 2 or len(nombre_input.strip()) > 50:
                print("Error: El nombre debe tener entre 2 y 50 caracteres. Por favor, inténtalo de nuevo.")
                continue # Vuelve al inicio del bucle principal
            if all(char.isalpha() or char.isspace() for char in nombre_input):
                if any(char.isalpha() for char in nombre_input): # Asegura que hay al menos una letra
                    nombre = nombre_input # Si es válido, asigna el valor a la variable final
                    print(f"Bienvenido: {nombre}\n")
                else:
                    print("Tu nombre debe tener al menos una letra. Por favor, inténtalo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
            else:
                print("Eso no parece un nombre válido. Por favor, inténtalo de nuevo sin números o caracteres especiales.")
                continue # Vuelve al inicio del bucle principal

        # --- Validar el Peso ---
        # Solo pide el peso si el nombre ya es válido y el peso aún no lo es
        if nombre is not None and peso is None:
            try:
                peso_input = float(input("Por favor ingrese su peso en kilogramos: \n"))
                if peso_input <= 0:
                    print("Error: El peso debe ser mayor que cero. Por favor, inténtelo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
                elif peso_input > 300:
                    print("Error: El peso debe ser razonable (máximo 300 kg). Por favor, inténtelo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
                else:
                    peso = peso_input # Si es válido, asigna el valor
                    print(f"Peso ingresado: {peso} kg.\n")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para el peso.")
                continue # Vuelve al inicio del bucle principal

        # --- Validar la Altura ---
        # Solo pide la altura si el nombre y el peso ya son válidos, y la altura aún no lo es
        if nombre is not None and peso is not None and altura is None:
            try:
                altura_input = float(input("Ingrese su altura en metros: \n"))
                if altura_input <= 0:
                    print("Error: La altura debe ser mayor que cero. Por favor, inténtelo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
                elif altura_input < 0.5:
                    print("Error: La altura debe ser razonable (mínimo 0.5 metros). Por favor, inténtelo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
                elif altura_input > 3:
                    print("Error: La altura debe ser razonable (máximo 3 metros). Por favor, inténtelo de nuevo.")
                    continue # Vuelve al inicio del bucle principal
                else:
                    altura = altura_input # Si es válido, asigna el valor
                    print(f"Altura ingresada: {altura} metros.\n")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para la altura.")
                continue # Vuelve al inicio del bucle principal

        # --- Si todos los datos son válidos, salimos de este bucle interno ---
        if nombre is not None and peso is not None and altura is not None:
            print("¡Todos los datos han sido ingresados y validados correctamente!\n")
            break # Salimos del bucle de validación de entradas

    # --- Cálculos y Resultados Finales ---
    imc_calculado = calcular_IMC(peso, altura)
    nivel = nivel_peso(imc_calculado)

    print(f"\n--- Resultados para {nombre} ---")
    print(f"Su IMC es: {imc_calculado:.2f}")
    print(f"Su nivel de peso es: {nivel}")

    peso_ideal_min, peso_ideal_max = calcular_peso_ideal(altura)
    print(f"Su peso ideal se encuentra entre {peso_ideal_min:.2f} kg y {peso_ideal_max:.2f} kg.")

    # --- Preguntar si desea realizar otra consulta ---
    while True: # Bucle para validar la respuesta 'sí'/'no'
        otra_consulta = input("\n¿Desea realizar otra consulta? (sí/no): ").lower().strip()
        if otra_consulta == "no":
            print("\nGracias por usar el programa de cálculo del Índice de Masa Corporal (IMC). ¡Hasta pronto!")
            exit() # Termina el programa completamente
        elif otra_consulta == "si" or otra_consulta == "sí":
            print("¡De acuerdo! Iniciando una nueva consulta...\n")
            break # Sale de este bucle interno, y el bucle principal (while True) se repite
        else:
            print("Respuesta no válida. Por favor, escriba 'sí' o 'no'.")