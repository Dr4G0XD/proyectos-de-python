
# Simulación de la Máquina de Galton en Python

Este proyecto es una simulación de la famosa máquina de Galton, que ilustra el teorema del límite central y la distribución normal de manera visual. La simulación utiliza números aleatorios para modelar la caída de miles de canicas a través de una serie de obstáculos.

## ¿Cómo funciona?

El programa simula el recorrido de 3000 canicas a lo largo de 12 niveles de obstáculos. En cada nivel, cada canica toma una decisión aleatoria: ir a la izquierda o a la derecha. El número total de veces que una canica se desvía a la derecha determina el contenedor en el que finalmente cae.

El resultado de esta simulación es una distribución binomial que, con un gran número de canicas, se aproxima a una **distribución normal** o en forma de campana. Los resultados se visualizan a través de un histograma que muestra la cantidad de canicas en cada uno de los contenedores.

## Requisitos

Para ejecutar el programa, necesitas tener Python instalado, junto con las siguientes bibliotecas:

* **NumPy**: Para la generación eficiente de números aleatorios.
* **Matplotlib**: Para la visualización de los datos mediante un histograma.

Puedes instalar ambas bibliotecas usando `pip` con los siguientes comandos:

```bash
pip install numpy matplotlib
