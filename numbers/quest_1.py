# Faça um programa que calcule o volume de uma esfera, dado o seu raio.
from math import pi

raio = float(input("Informe o raio de uma esfera em metros: "))
volume=(4*pi*raio**3)/3
print("Volume igual a %.2f" % volume, "m³")