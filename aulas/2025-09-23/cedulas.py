valor = int(input('Digite o valor: '))

cedula_200 = valor // 200
cedula_100 = (valor % 200) // 100
cedula_50 = ((valor % 200) % 100) // 50
cedula_20 = (((valor % 200) % 100) % 50) // 20
cedula_10 = ((((valor % 200) % 100) % 50) % 20) // 10
cedula_5 = (((((valor % 200) % 100) % 50) % 20) % 10) // 5
cedula_2 = ((((((valor % 200) % 100) % 50) % 20) % 10) % 5) // 2
cedula_1 = ((((((valor % 200) % 100) % 50) % 20) % 10) % 5) % 2

print(cedula_200)
print(cedula_100)
print(cedula_50)
print(cedula_20)
print(cedula_10)
print(cedula_5)
print(cedula_2)
print(cedula_1)
