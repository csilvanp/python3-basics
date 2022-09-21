# Escreva um programa que recebe uma strin e informa se ela é um palíndromo.

my_str = input("Informe uma string única: ")
my_inv_str = my_str[::-1]
if my_str == my_inv_str: print("É palíndromo.")
else: print("Não é palíndromo.")