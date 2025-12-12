def misterio1(p1: int):
    print(id(p1))
    p1 = 100
    print(id(p1))

## PP
numero = 10
print(id(numero))
print(f'{numero=}')
misterio1(numero)
print(f'{numero=}')
