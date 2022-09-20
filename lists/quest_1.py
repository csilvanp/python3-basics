'''
    Escreva um script Python que possui duas listas: uma numérica
    e outra com caracteres. Faça as seguintes operações:
        - Imprima o conteúdo das listas.
        - Imprima o tamanho das listas.
        - Imprima fatias das listas.
        - Crie uma terceira lista que seja a junção (nested) das outras duas.
        - Acesse células da nova lista, de maneira similar ao acesso de uma matriz.
        - Remova todos os conteúdos das listas.
        - Imprima novamente cada uma das listas.
'''

lista1, lista2 = list(range(0,5)), ["a","b","c","d","e"]
print("Lista 1: {}\nLista 2: {}".format(lista1,lista2))
print("Tamanho da lista 1:", len(lista1),"\tTamanho da lista 2:", len(lista2))
print("Fatias:\n\tLista 1 (de 0 a 3) ->{}\n\tLista 2 (de 3 a n) -> {}".format(lista1[0:3],lista2[3:]))
lista3 = [lista1, lista2]
print("Lista 3:", lista3)
print("Acesso ao 3º elemento da lista 2 dentro da lista 3:", lista3[1][2])
lista1, lista2, lista3 = [], [], []
print("Lista 1:", lista1, "\nLista 2:", lista2, "\nLista 3:", lista3)