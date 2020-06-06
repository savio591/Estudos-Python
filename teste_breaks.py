"""
Saindo de loops com o break
"""

# exemplo 1
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print("Pronto!")

# exemplo 2
while True:
    print("Digite 'sair' ou 'q' para sair,")
    comando = input("-> ")
    if comando.lower() == "sair" or comando.lower() == "q":
        break

print()

print("Okay")
