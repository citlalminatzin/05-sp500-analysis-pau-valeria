#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ


def make_plot(x, y, titulo="Grafica", xlabel="x", ylabel="y"):
    """
    Funcion para graficas.
    """
    plt.figure()
    plt.plot(x, y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show() # Esto significa implementación pendiente, lo puedes eliminar

def main():
    """
    (Si no modificas esta cadena de texto lloro)
    Aquí va el código, recuerda reutilizar el 
    código que ya escribiste en otros archivos
    """
    ... # Esto significa implementación pendiente, lo puedes eliminar

if __name__ == "__main__":
    main()
