"""
Experimentos com string rs
"""
nome = 'Savio Henrique dos Santos Castelo'
print(nome)

print()

print("Nome apenas os 3 primeiros caracteres selecionados")
print(nome[0:3])

print()

print("Nome com o .split")
print(nome.split())

print()

print("Nome com apenas o segundo split selecionado")
print(nome.split()[1])

print()

# [::-1] -> ":" Seleciona o primeiro, ":" seleciona até o último, "-1" inverte os dados <3
print("String Invertida")
print(nome[::-1])

print()

print('Substituir o "S" por "L"')
print(nome.replace("S", "L"))
