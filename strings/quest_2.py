# Demonstre que uma string é imutável
string = "palavra"
try :
    string[0] = 'l'
except TypeError:
    print("String não pode ser mudada diretamente")
    