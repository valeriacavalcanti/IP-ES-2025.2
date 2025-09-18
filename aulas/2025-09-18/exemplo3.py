valor_compra = float(input('Digite o valor da compra: '))

quantidade_cupons = int(valor_compra // 20)
# quantidade_cupons = int(quantidade_cupons)

#saldo = valor_compra - (quantidade_cupons * 20)
saldo = valor_compra % 20
valor_proximo_cupom = 20 - saldo

print('Quantidade de cupons =', quantidade_cupons)
print('Saldo =', saldo)
print('Valor para próximo cupom =', valor_proximo_cupom)
