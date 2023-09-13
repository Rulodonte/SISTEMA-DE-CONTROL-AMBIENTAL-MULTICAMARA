import matplotlib.pyplot as plt
import numpy as np

# Crear datos para la gráfica
x = np.linspace(0, 2 * np.pi, 100)  # Valores de x de 0 a 2*pi
y = np.sin(x)                      # Valores de y = sin(x)

# Crear la gráfica
plt.plot(x, y)
plt.title('Gráfica de la función seno')
plt.xlabel('x')
plt.ylabel('y')

# Mostrar la gráfica en pantalla
plt.show()


# En esta parte agregamos la primera modificacion
print("Primea modificacion")