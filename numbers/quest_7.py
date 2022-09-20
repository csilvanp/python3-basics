# Entrar com um número no formato CDU e imprimir na ordem inversa UDC
num = int(input("Informe um número de três dígitos: "))
c = (num % 1000) // 100
d = (num % 100) // 10
u = (num % 10) // 1

print("Valor invertido: {}{}{}".format(u,d,c))
