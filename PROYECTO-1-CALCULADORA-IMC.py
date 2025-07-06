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
    apellido_paterno = None
    apellido_materno = None
    edad = None
    peso = None
    altura = None

    # --- Bucle para toda la validación de entrada (nombre, apellidos, edad, peso, altura) ---
    while True:
        # --- Validar el Nombre ---
        if nombre is None:
            nombre_input = input("Por favor, introduce tu nombre (entre 2 y 50 caracteres): \n")
            if not nombre_input.strip():
                print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
                continue
            if len(nombre_input.strip()) < 2 or len(nombre_input.strip()) > 50:
                print("Error: El nombre debe tener entre 2 y 50 caracteres. Por favor, inténtalo de nuevo.")
                continue
            if all(char.isalpha() or char.isspace() for char in nombre_input):
                if any(char.isalpha() for char in nombre_input):
                    nombre = nombre_input
                    print(f"Nombre ingresado: {nombre}\n")
                else:
                    print("Tu nombre debe tener al menos una letra. Por favor, inténtalo de nuevo.")
                    continue
            else:
                print("Eso no parece un nombre válido. Por favor, inténtalo de nuevo sin números o caracteres especiales.")
                continue

        # --- Validar el Apellido Paterno ---
        if nombre is not None and apellido_paterno is None:
            apellido_paterno_input = input("Por favor, introduce tu apellido paterno (entre 2 y 50 caracteres): \n")
            if not apellido_paterno_input.strip():
                print("El apellido paterno no puede estar vacío. Por favor, inténtalo de nuevo.")
                continue
            if len(apellido_paterno_input.strip()) < 2 or len(apellido_paterno_input.strip()) > 50:
                print("Error: El apellido paterno debe tener entre 2 y 50 caracteres. Por favor, inténtalo de nuevo.")
                continue
            if all(char.isalpha() or char.isspace() for char in apellido_paterno_input):
                if any(char.isalpha() for char in apellido_paterno_input):
                    apellido_paterno = apellido_paterno_input
                    print(f"Apellido Paterno ingresado: {apellido_paterno}\n")
                else:
                    print("Tu apellido paterno debe tener al menos una letra. Por favor, inténtalo de nuevo.")
                    continue
            else:
                print("Eso no parece un apellido válido. Por favor, inténtalo de nuevo sin números o caracteres especiales.")
                continue

        # --- Validar el Apellido Materno ---
        if nombre is not None and apellido_paterno is not None and apellido_materno is None:
            apellido_materno_input = input("Por favor, introduce tu apellido materno (entre 2 y 50 caracteres): \n")
            if not apellido_materno_input.strip():
                print("El apellido materno no puede estar vacío. Por favor, inténtalo de nuevo.")
                continue
            if len(apellido_materno_input.strip()) < 2 or len(apellido_materno_input.strip()) > 50:
                print("Error: El apellido materno debe tener entre 2 y 50 caracteres. Por favor, inténtalo de nuevo.")
                continue
            if all(char.isalpha() or char.isspace() for char in apellido_materno_input):
                if any(char.isalpha() for char in apellido_materno_input):
                    apellido_materno = apellido_materno_input
                    print(f"Apellido Materno ingresado: {apellido_materno}\n")
                else:
                    print("Tu apellido materno debe tener al menos una letra. Por favor, inténtalo de nuevo.")
                    continue
            else:
                print("Eso no parece un apellido válido. Por favor, inténtalo de nuevo sin números o caracteres especiales.")
                continue

        # --- Validar la Edad ---
        if nombre is not None and apellido_paterno is not None and apellido_materno is not None and edad is None:
            try:
                edad_input = int(input("Por favor, introduce tu edad (entre 1 y 120 años): \n"))
                if edad_input <= 0:
                    print("Error: La edad debe ser mayor que cero. Por favor, inténtalo de nuevo.")
                    continue
                elif edad_input > 120:
                    print("Error: La edad debe ser razonable (máximo 120 años). Por favor, inténtalo de nuevo.")
                    continue
                else:
                    edad = edad_input
                    print(f"Edad ingresada: {edad} años.\n")
            except ValueError:
                print("Error: Por favor, ingresa un valor numérico válido para la edad.")
                continue

        # --- Validar el Peso ---
        if nombre is not None and apellido_paterno is not None and apellido_materno is not None and edad is not None and peso is None:
            try:
                peso_input = float(input("Por favor ingrese su peso en kilogramos: \n"))
                if peso_input <= 0:
                    print("Error: El peso debe ser mayor que cero. Por favor, inténtalo de nuevo.")
                    continue
                elif peso_input > 300:
                    print("Error: El peso debe ser razonable (máximo 300 kg). Por favor, inténtalo de nuevo.")
                    continue
                else:
                    peso = peso_input
                    print(f"Peso ingresado: {peso} kg.\n")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para el peso.")
                continue

        # --- Validar la Altura ---
        if nombre is not None and apellido_paterno is not None and apellido_materno is not None and edad is not None and peso is not None and altura is None:
            try:
                altura_input = float(input("Ingrese su altura en metros: \n"))
                if altura_input <= 0:
                    print("Error: La altura debe ser mayor que cero. Por favor, inténtalo de nuevo.")
                    continue
                elif altura_input < 0.5:
                    print("Error: La altura debe ser razonable (mínimo 0.5 metros). Por favor, inténtalo de nuevo.")
                    continue
                elif altura_input > 3:
                    print("Error: La altura debe ser razonable (máximo 3 metros). Por favor, inténtalo de nuevo.")
                    continue
                else:
                    altura = altura_input
                    print(f"Altura ingresada: {altura} metros.\n")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido para la altura.")
                continue

        # --- Si todos los datos son válidos, salimos de este bucle interno ---
        if nombre is not None and apellido_paterno is not None and apellido_materno is not None and edad is not None and peso is not None and altura is not None:
            print("¡Todos los datos han sido ingresados y validados correctamente!\n")
            break

    # --- Cálculos y Resultados Finales ---
    imc_calculado = calcular_IMC(peso, altura)
    nivel = nivel_peso(imc_calculado)

    print(f"\n--- Hola! {nombre} {apellido_paterno} {apellido_materno} (Edad: {edad}) ---")
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