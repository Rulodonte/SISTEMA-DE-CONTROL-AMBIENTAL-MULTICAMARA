import matplotlib.pyplot as plt
import numpy as np
import math

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



# Ingresar los valores de los catetos
cateto1 = float(input("Ingresa la longitud del primer cateto: "))
cateto2 = float(input("Ingresa la longitud del segundo cateto: "))

# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostrar el resultado
print(f"La hipotenusa es: {hipotenusa}")