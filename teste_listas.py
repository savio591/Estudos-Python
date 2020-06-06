"""
Listas funcionam como arrays(vetores/matrizes)
As listas em python são representadas por colchetes []
"""
lista1 = [23, 23, 23, 12, 88, 99, 4]
print(lista1)

lista2 = ["g", "e", "e", "k"]
print(lista2)

lista3 = []
print(lista3)

# lista com seq. range(Observar os parênteses)
lista4 = list(range(11))
print(lista4)

# lista com seq. string(Observar os parênteses)
lista5 = list("Geek")
print(lista5)

print()

if "e" in lista5:
    print(f"Tem 'e' na lista {lista5}.")
else:
    print(f"Não tem 'e' na lista {lista5}")

print()

# Pode-se facilmente ordenar uma lista
print("Ordenar lista")
print(lista1)
lista1.sort()
print(lista1)

print()

# Pode-se facilmente contar o número de ocorrências de um valor em uma lista
print(f"Quantidade do valor '23' na 'lista1' - {lista1}")
print(lista1.count(23))
print()
print(f"Qt de 'e' na 'lista2' - {lista2}")
print(lista2.count("e"))

print()

# Adicionar valor numa lista(.append), só é possível adicionar um elemento por vez.
print("Adicionar 100 na lista1:")
print(lista1)
lista1.append(100)
print(lista1)

print()

# Adicionar lista numa lista(.append)
print("Adicionar lista dentro lista1:")
print(lista1)
lista1.append([251, 12, 44])
print(lista1)

print()

# adicionar valores numa lista(.extend), com vários elementos por vez.
print("Adicionar 42, 55, 85 na lista1:")
print(lista1)
lista1.extend([42, 55, 85])
print(lista1)

print()

# adicionar valores nume lista(.insert), em posição específica.
print("Adicionar 2 na primeira posição")
print(lista1)
lista1.insert(0, 2)
print(lista1)

print()

# contar elementos dentro de uma lista(conta a partir de 1)
print(f"Qt de elementos na lista1 - {lista1}")
print(len(lista1))

print()

# remover o último elemento da lista e retorna o valor(.pop)
print(f"Remover último elemento da lista1 - {lista1}")
print(f"{lista1.pop()} removido!")
print(lista1)

print()
