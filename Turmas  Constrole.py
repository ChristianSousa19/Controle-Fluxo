media = float(input("media: "))
nome = input("nome: ")
sexo = input("sexo:; ")
nota1 = float(input("nota 1 : "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))

result = (nota1 + nota2 + nota3) / 3

if result >= media:
    if sexo == "feminino" or sexo == "f":
        print(" a aluna", nome, "foi aprovada com media", result)
    elif sexo == "masculino" or sexo == "m":
        print("o aluno", nome, "foi aprovado com media", result)
    else:
        print(nome, "foi aprovado com maior nota", result)

else:

    if sexo == "feminino" or sexo == "f":
        print(" a aluna", nome, "foi aprovada com media ", result)
    elif sexo == "masculino" or sexo == "m":
        print("o aluno", nome, "foi aprovado com media", result)
    else:
        print(nome, "foi reprovada com a menor nota", result)