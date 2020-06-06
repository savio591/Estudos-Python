nome = input("Seja vem vindo! Digite o seu nome por favor!")

print()

print(f"muito bem! {nome.lower()} adicione a primeira numeração.")
num_1 = input()

print("Agora a segunda")
num_2 = input()

print("Por fim, a terceira")
num_3 = input()

soma = num_1 + num_2 + num_3

print()

print(f"Bom, {nome} o resultado de {num_1} + {num_2} + {num_3} é {num_1 + num_2 + num_3}!")
print()

print(f"Brinks, o resultado é {int(num_1) + int(num_2) + int(num_3)} kksks")

print()

print("Obrigado por baixar esse programa de alta complexidade!")

print()

print("Agora vamos testar um outro método")
print("Digite a quantidade de cálculos")
qtd = int(input("qtd ->"))
soma = int(0)
for n in range(1, qtd + 1):
    num = int(input(f"Digite o valor {n}/{qtd}."
                    f"-> "))
    soma = num + soma
print(f"A soma é {soma}")
