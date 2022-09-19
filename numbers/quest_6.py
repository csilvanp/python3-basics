# Faça um programa que leia o lado de um quadrado e imprima perímetro, diagonal e área.
lado = float(input("Informe o lado de um quadrado: "))
perimetro = 4*lado
diagonal = (2**(1/2))*lado
area = pow(lado,2)

print("Perímetro = {:.2f}m".format(perimetro))
print("Diagonal = {:.2f}m".format(diagonal))
print("Área = {:.2f}m".format(area))
