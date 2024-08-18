preco = int(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro_recebido = int(input("Dinheiro recebido: "))
troco = dinheiro_recebido - (preco*quantidade)

print(f"Troco = {troco:.2f}")