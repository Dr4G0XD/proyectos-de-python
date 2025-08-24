import numpy as np
import matplotlib.pyplot as plt

def simular_galton(num_canicas, num_niveles):
    """
    Simula la caída de canicas en una máquina de Galton.
    
    Args:
        num_canicas (int): El número total de canicas a simular.
        num_niveles (int): El número de niveles de obstáculos en la máquina.
        
    Returns:
        np.array: Un array con la posición final de cada canica.
    """
    # Se simula el camino de cada canica. 
    # Cada 1 representa ir a la derecha y cada 0 representa ir a la izquierda.
    # El tamaño del array es (num_canicas, num_niveles).
    # Se utiliza una matriz de 0s y 1s, donde 1 representa un movimiento hacia la derecha.
    desviaciones = np.random.randint(0, 2, size=(num_canicas, num_niveles))
    
    # La posición final de cada canica es la suma de sus desviaciones hacia la derecha.
    # Esto da el índice del contenedor en el que termina.
    posiciones_finales = np.sum(desviaciones, axis=1)
    
    return posiciones_finales

def graficar_histograma(posiciones_finales, num_niveles):
    """
    Genera y muestra un histograma de los resultados de la simulación.
    
    Args:
        posiciones_finales (np.array): Array con las posiciones finales de las canicas.
        num_niveles (int): El número de niveles de obstáculos en la máquina.
    """
    # El número de contenedores es igual al número de niveles + 1.
    # Los contenedores se numeran de 0 a num_niveles.
    num_contenedores = num_niveles + 1
    
    # Crea el gráfico de histograma.
    plt.figure(figsize=(10, 6))
    plt.hist(posiciones_finales, bins=np.arange(num_contenedores + 1) - 0.5, rwidth=0.8, color='skyblue', edgecolor='black')
    
    # Configura las etiquetas y el título del gráfico.
    plt.title('Simulación de la Máquina de Galton')
    plt.xlabel('Número de Contenedor')
    plt.ylabel('Cantidad de Canicas')
    plt.xticks(np.arange(num_contenedores))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Muestra el gráfico.
    plt.show()

# --- Parámetros de la simulación ---
NUM_CANICAS = 3000
NUM_NIVELES = 12

# --- Ejecución del programa ---
if __name__ == "__main__":
    # Simula la caída de las canicas.
    resultados = simular_galton(NUM_CANICAS, NUM_NIVELES)
    
    # Grafica los resultados en un histograma.
    graficar_histograma(resultados, NUM_NIVELES)