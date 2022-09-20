''' 
    Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem,
    considerando que o carro faz 12 km com um litro. Deverão ser fornecidos tempo
    gasto e a velocidade média.
'''
tempo = int(input("Informe o tempo gasto na viagem: "))
vel_media = int(input("Informe a velocidade média durante a viagem: "))
KM_LITRO = 12

qtd_litros = (vel_media * tempo) / KM_LITRO

print("Quantidade de litros gastos é {:.2f}L".format(qtd_litros))