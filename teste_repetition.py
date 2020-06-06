"""
Tipos de Loops:
    For -

Loops iteram com sequências ou valores iteraveis.
"""
"""
    Exemplos de iteraveis:
        - String
            nome = 'Testekk'

        - Lista:
            lista = [1, 3, 5, 6]

        - Range:
            numeros = range(1, 10)
"""


nome = 'Savil Castelo'
lista = [4, 1, 2, 3, 0]
numeros = range(1, 10)

"""
# exemplo de for 1 (iterando em uma string)
for letras in nome:
    print(letras)

print()

# exemplo de for 2 (iterando em uma lista)
for numeros in lista:
    print(numeros)

print()

# ememplo for 3 (iterando em um range de numeros)
for numeros in range(1, 10):
    print(numeros)
"""

"""
for index, value in enumerate(string):
    print(string[index])
"""

# Uso do for para enumerar strings(valores)
for values in nome:
    print(values)

print()

# uso do for e enumate para printar os índices e valores.
for i, v in enumerate(nome):
    print(f"Index({i}), value({v})")

print()

# uso do for para enumerar apenas os índices
for i, v in enumerate(nome):
    print(nome[i])

# uso do for para enumerar apenas os índices
for i, v in enumerate(nome):
    print(nome[i])

# uso do for para enumerar com saída nula dos índices
for _, v in enumerate(nome):
    print(v)

# uso do for para enumerar com saída nula dos values
for i, _ in enumerate(nome):
    print(i)

print()

# uso do for com enumerar, imprimindo apenas a tupla 0(índice)
for indexes in enumerate(nome):
    print(indexes[0])

print()

# uso do for com enumerate, impriindo apenas a tupla 1(values)
for values in enumerate(nome):
    print(values[1])

print("Quantas vezes esse loop deve rodar?")
qdt =  int(input("-> "))

print()

for n in range(1, qdt + 1):
    print(f"Imprimindo{n}x")

print()

soma = 0

for n in range(1, qdt+1):
    num = int(input(f"Informe o {n}/{qdt} valor."))
    soma = soma + num

print(f"A soma é {soma}")
