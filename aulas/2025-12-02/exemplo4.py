def misterio1():
    global numero
    numero = 100
    print('f', id(numero))
    print('f', numero)
    

## PP
numero = 10
print('pp', id(numero))
misterio1()
print('pp', numero)
