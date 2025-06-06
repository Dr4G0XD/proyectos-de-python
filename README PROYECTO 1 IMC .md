#En este readme me dedicare a explicar el funcionamiento de mi programa de INDICE DE MASA CORPORAL

#Como primer paso usamos la keyword (def) que se utiliza para definir funciones, con esta podemos crear bloques reutilizables

#definimos la funcion encargada de calcular el IMC

def calcular_IMC(peso, altura):       #definimos lo que es el nombre de la funcion y en los parentesis añadimos los dos parametros a utilizar
    return peso / (altura ** 2)       #agregamos un valor de return esto perimite enviar de vuelta un valor a la funcion ya llamada

#generamos ahora la funcion encargada valorar el nivel de peso de la persona y catalogarla segun los parametros en alguno de los returns
#dependiendo el resultado

def nivel_peso(imc):
    if imc < 18.5:              #Utilizamos la keyboard (if) que se utiliza para implementar estructuras condicionales 
        return "Bajo peso"      #es decir si la primera condicion de imc < 18.5: es verdadera el return regresara un valor de texto.
    elif 18.5 <= imc < 24.9:    
        return "Peso normal"    #En caso de que el valor fuera falso es decir no cumple con la condición imc < 18.5: utilizaremos un (elif).
    elif 25 <= imc < 29.9:      #La keyboard (elif) se utiliza para verificar condiciones adicionales si la condicion (if) o cualquier anterior
        return "Sobrepeso"      #(elif) resulte falsa se pueden tener tantas como sean necesarias.
    elif 30 <= imc < 34.9:
        return "Obesidad I"     #En caso de hacer utilizado la cantidad necesarios de (elif) utilizaremos un (else).
    elif 35 <= imc < 39.9:
        return "Obesidad II"
    elif 40 <= imc < 49.9:
        return "Obesidad III"
    else:                       #La keyboard (else) se utiliza solamente si ninguna de las condiciones anteriores fue verdadera esta debe ir al
        return "Obesidad IV"    #al final de la cadena de (if) y (else) solo puede haber una por cada estructura, no tiene una condicion asociada

  def calcular_peso_ideal(altura):              #como extra decidí añadir una funcion para calcular es peso ideal para cada persona dentro
    imc_min = 18.5                              #de imc minimo y maximo
    imc_max = 24.9
    peso_ideal_min = imc_min * (altura ** 2)
    peso_ideal_max = imc_max * (altura ** 2)
    return peso_ideal_min, peso_ideal_max

        
#Una forma de ejemplificar las keyboards (if,elif y else) seria como:
#if: "Si esto es cierto, hazlo."
#elif: "De lo contrario, si esto es cierto, hazlo." (Y puedes tener varios de estos)
#else: "Si nada de lo anterior fue cierto, entonces haz esto.

#Ya teniendo los valores pricipales decidí introducir un bucle esto por dos razones, en caso de que el usuario ingrese datos erroneos y para poder
#repetir el programa en caso de querer realizar otra consulta para ello utilizaremos la keyboard (while) con la condicion (true)

# --- Bucle principal para permitir nuevas consultas ---
while True:                                                                          #La keyboard (while) es para crear bucles(loops) condicioneales esto permite que un bloque de codigo se repita               
    print("\n--- Cálculo del Índice de Masa Corporal (IMC) ---")                     #mientras una condicion especifica sea verdadera. si la condicion es falsa el bucle termina y la ejecucion del programa 
                                                                                     #termina.   
  # Inicializamos las variables con un valor que indica que no han sido validadas
  nombre = None                    
    apellido_paterno = None
    apellido_materno = None
    edad = None
    peso = None
    altura = None

  # --- Bucle para toda la validación de entrada (nombre, apellidos, edad, peso, altura) ---
  while True:                                                                                                       # este (while true) Su propósito es asegurarse de que todos los datos necesarios se recojan 
      # --- Validar el Nombre ---                                                                                   #validen con éxito antes de que el programa pueda pasar a los cálculos y resultados.
        if nombre is None: # Comprueba si la variable 'nombre' no ha sido asignada aún (o se ha resetado a None)    #Si el usuario ingresa un dato inválido en cualquier punto
            nombre_input = input("Por favor, introduce tu nombre (entre 2 y 50 caracteres): \n")                    #un continue lo devolverá al principio de este bucle
      # 1. ¿Está vacío el nombre?
            if not nombre_input.strip():                                                  # .strip() elimina espacios en blanco al inicio y final, Comprueba si la entrada está vacía después de quitar los espacios.
                print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
                continue                                                                  # Si está vacío, volvemos a pedirlo (al inicio del while True).
      # 2. ¿Tiene la longitud correcta?
            if len(nombre_input.strip()) < 2 or len(nombre_input.strip()) > 50:           #(len) Valida que la longitud de la cadena esté dentro de un rango específico
                print("Error: El nombre debe tener entre 2 y 50 caracteres. Por favor, inténtalo de nuevo.")
                continue                                                                  # Si la longitud es incorrecta, volvemos a pedirlo.
       # 3. ¿Contiene solo letras y espacios?
            if all(char.isalpha() or char.isspace() for char in nombre_input):            #Para nombres y apellidos, verifica que todos los caracteres sean letras o espacios
       # 4. ¿Contiene al menos una letra (para evitar nombres como "   ")?
                if any(char.isalpha() for char in nombre_input):                          #Para nombres y apellidos, asegura que haya al menos una letra en la entrada 
                    nombre = nombre_input                                                 # Si todo es válido, asignamos el nombre.
                    print(f"Nombre ingresado: {nombre}\n")
                else:
                    print("Tu nombre debe tener al menos una letra. Por favor, inténtalo de nuevo.")
                    continue                                                              # Si no tiene letras, volvemos a pedirlo.
            else:                                                                         # Si hay caracteres no válidos (números, símbolos)
                print("Eso no parece un nombre válido. Por favor, inténtalo de nuevo sin números o caracteres especiales.")
                continue                                                                  # Volvemos a pedirlo.

  # --- Validar el Apellido Paterno --- #repetimos el proceso que con nombre
  if nombre is not None and apellido_paterno is None: #------------------------------------------------------------------------- Esta variable indica que si nombre ya tiene un valor asignado y apellido paterno no
            apellido_paterno_input = input("Por favor, introduce tu apellido paterno (entre 2 y 50 caracteres): \n")            #se continue preguntando por el apellido paterno
            if not apellido_paterno_input.strip():                                                                              #Esto asegura que el programa pida los datos en un orden específico y no repita preguntas innecesarias.
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

  # --- Validar el Apellido Materno --- #repetimos el proceso que con nombre
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
  if nombre is not None and apellido_paterno is not None and apellido_materno is not None and edad is None:  #----------------------------------esta linea indica que si nombre y apellidos ya tiene valores asignados y la 
            try: #El bloque try "intenta" ejecutar el código, y si ocurre un ValueError, la ejecución salta al bloque except ValueError:        #variable edad aún no, comienze a preguntar edad 
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
            except ValueError: #Si en la línea edad_input = int(input(...)) el usuario no ingresó un número es decir colocar letras o simbolos un ValueError se dispararía y el control pasaría aquí.
                print("Error: Por favor, ingresa un valor numérico válido para la edad.")
                continue 

   # --- Validar el Peso --- #repetimos el proceso como en edad solo que ahora con valores (float) e identificando a edad con un valor ya asignado
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

   # --- Validar la Altura --- #repetimos el proceso como en edad solo que ahora con valores (float) e identificando a edad y peso con un valor ya asignado
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
            break     #la sentencia (break) detiene el bucle while True principal, permitiendo que el programa continúe con los cálculos.

  # --- Cálculos y Resultados Finales ---
  imc_calculado = calcular_IMC(peso, altura)
  nivel = nivel_peso(imc_calculado)

  print(f"\n--- Hola! {nombre} {apellido_paterno} {apellido_materno} (Edad: {edad}) ---")
    print(f"Su IMC es: {imc_calculado:.2f}")
    print(f"Su nivel de peso es: {nivel}")

  peso_ideal_min, peso_ideal_max = calcular_peso_ideal(altura)
    print(f"Su peso ideal se encuentra entre {peso_ideal_min:.2f} kg y {peso_ideal_max:.2f} kg.")    #El .2f en los print formatea los números flotantes para que muestren solo dos decimales.

  # --- Preguntar si desea realizar otra consulta ---
  while True: # Bucle para validar la respuesta 'sí'/'no'       #Otro while True interno se usa aquí para asegurar que la respuesta del usuario sea solo "sí" o "no".
        otra_consulta = input("\n¿Desea realizar otra consulta? (sí/no): ").lower().strip() #.lower Convierte la entrada a minúsculas y .strip elimina espacios para facilitar la comparación.
        if otra_consulta == "no":
            print("\nGracias por usar el programa de cálculo del Índice de Masa Corporal (IMC). ¡Hasta pronto!")
            exit()                                              # Termina el programa completamente
        elif otra_consulta == "si" or otra_consulta == "sí":    
            print("¡De acuerdo! Iniciando una nueva consulta...\n")
            break                                               # Sale de este bucle interno, y el bucle principal (while True) se repite
        else:
            print("Respuesta no válida. Por favor, escriba 'sí' o 'no'.")


  #Este fue mi proyecto de imc al principio fue complicado ya que en un inicio coloque varios while true en cada valor de peso altura etc, pero investigando
  #verifique que se puede colocar todo en un solo ciclo  mas el que añadi para repetir el ciclo principal, tambien descubri condiciones como .trip, .lower y len
  #que me permitieron añadir condiciones para pedir los valores exactos al programa y que este no cerrara, un me complico con el while y con los breaks pero espero pronto
  #aprender mas de esto
  # Javier alejandro ortiz hernandez Ucamp



