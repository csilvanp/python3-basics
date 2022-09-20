'''
    Dado um número de conta corrente com três dígitos, retorne o
    seu dígito verificado. Considere a conta 235, o dígito é calculado
    da seguinte maneira:
        - Somar o número da conta com o seu inverso: 235 + 532 = 767
        - Multiplicar cada dígito pela sua orgem posicional e somar
            estes números. (A soma dos produtos de ordem posicional de 767 é 40)
'''

conta = int(input("Informe o número da conta com 3 dígitos: "))

c = (conta % 1000) // 100
d = (conta % 100) // 10
u = (conta % 10) // 1

inverso = (u * 100) + (d * 10) + c
soma_conta = conta + inverso

soma_conta_c = (soma_conta % 1000) // 100
soma_conta_d = (soma_conta % 100) // 10
soma_conta_u = (soma_conta % 10) // 1

verificador = soma_conta_u + (soma_conta_d*2) + (soma_conta_c*3)

print("Dígito verificador é:",verificador)