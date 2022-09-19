# Dados dois números x e y, troque o valor de um pelo outro
x = int(input("Informe x: "))
y = int(input("Informe y: "))

print("\nValor original de x:", x)
print("Valor original de y:", y)

aux = x
x = y
y = aux

print("\nValor alterado de x:", x)
print("Valor alterado de y:", y)