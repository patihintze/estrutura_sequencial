print("Dados da primeira pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("Idade: "))

print("Dados da segunda pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("Idade: "))

media_idade = (idade1 + idade2) / 2

print(f"A idade média de {nome1} e {nome2} é de {media_idade:.1f}")