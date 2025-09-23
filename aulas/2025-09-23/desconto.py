valor_pago = float(input('Valor pago: '))
valor_desconto = float(input('Valor do desconto: '))

valor_bruto = valor_pago + valor_desconto

aliquota = valor_desconto * 100 / valor_bruto

print(f'Desconto: {aliquota:10.1f}%')

print(valor_bruto, valor_pago, valor_desconto)
print(f'{valor_bruto}|{valor_pago}|{valor_desconto}')

print(valor_bruto, '|',valor_pago, '|', valor_desconto, end='$')

print(valor_bruto, valor_pago, valor_desconto, sep='IFPB')

print('eita', 10, sep='|')

print('eita', 'e agora', sep='\n'*10)

print('oi\n\n\n\nhummmmm')
