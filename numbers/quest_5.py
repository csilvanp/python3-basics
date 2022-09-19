# Resolva o mesmo exercício acima sem a utilização de variáveis temporárias
x,y = map(lambda a : int(a), input("Informe x e y (separados por espaço): ").split(" "))

print("\nValor original de x:", x)
print("Valor original de y:", y)

x,y = y,x

print("\nValor alterado de x:", x)
print("Valor alterado de y:", y)