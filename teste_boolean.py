"""
Booleano são os valores lógicos binários
True e False
Tem q comçar maiusculos e não minúsculos
"""
booleano = True
print(booleano)

print()

# imprimir booleano inverso com a função "not"
print("Boleano com o operador 'not'")
print(not booleano)

print()

# imprimir booleano 'or', que retorna se tiver a partir de um valor verdadeiro.
print("Booleano com 'or' e falso")
print(booleano or False)

print()

# imprimir not booleano 'or'
print("Booleano falso com 'or' e falso")
print(not booleano or False)

print()

# imprimir booleano com a proposição "and".
print("Booleano e falso com sentença 'and'")
print(booleano and True)

vdd = bool(1)
nn = bool(0)
print(vdd)
print(nn)

print()
print()

vdd_to_int = int(True)
nn_to_int = int(False)

print(vdd_to_int)
print(nn_to_int)
