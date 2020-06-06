"""Estruturas lógicas: and(e), or(ou), not(não), is(é)

    Operadores uniários:
        not, is
    Operadores binários:
        and, or
"""
print("insira seu nick")
nome_usuario = input("nick: -> ")
logado = False
ativado = False

if nome_usuario == 'savio591':
    nome = "Savinho"
    logado = True
else:
    nome = ""
    logado = False

if logado:
    print(f"Seja bem vindo(a) {nome}!")
    print()

if not logado:
    print("Você não tem cadastro neste sistema.")

if not ativado and logado:
    print("Parece que você ainda não ativou sua conta")
    print()
    print("Insira o código que enviamos no seu cérebro.")
    cod = input("código -> ")
    if cod == "shoppng591":
        ativado = True

if ativado and logado:
    print("Você já está logado no sistema")
