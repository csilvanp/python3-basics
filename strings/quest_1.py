'''
    Escreva um programa em Python que recebe uma string e imprime na tela:
        - O conteúdo da string em ordem direta;
        - O conteúdo inverso;
        - O número de caracteres;
        - Fatias (slices) da string;
'''
str1 = input("Informe uma string maior ou igual a 5 caracteres: ")
print("String na ordem direta:", str1)
print("String na ordem inversa:", str1[::-1])
print("Nº de caracteres:", len(str1))
print("Fatias:\n\tde 0 a 3 -> {} \n\tde 3 a len()-1 -> {}".format(str1[:3], str1[3:]))