print("Olá! Tô aq p adivinhar o ano de seu nascimento.")
print()
print("Para começar, digite o seu nome por favor.")
nome = input()

print(f"Muito bom! {nome} agora digite a sua idade pfv")
idade = input()

print(f"Belê!")
print(f"{nome} você tem {idade} e nasceu em {2020 - int(idade)}")

print("Até outro dia!")
