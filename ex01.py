largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_mt2 = float(input("Digite o valor do metro quadrado: "))
area = largura * comprimento
preco = area * valor_mt2

print(f"Area do terreno = {area:.2f} \nPreco do terreno: {preco:.2f}")