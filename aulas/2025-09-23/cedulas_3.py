valor = int(input('Digite o valor: '))
valor_original = valor

cedula_200 = valor // 200

valor = valor % 200
cedula_100 = valor // 100

valor = valor % 100
cedula_50 = valor // 50

valor = valor % 50
cedula_20 = valor // 20

valor = valor % 20
cedula_10 = valor // 10

valor = valor % 10
cedula_5 = valor // 5

valor = valor % 5
cedula_2 = valor // 2

cedula_1 = valor % 2

print(valor_original)
print(cedula_200)
print(cedula_100)
print(cedula_50)
print(cedula_20)
print(cedula_10)
print(cedula_5)
print(cedula_2)
print(cedula_1)
