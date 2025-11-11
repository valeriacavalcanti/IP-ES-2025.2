def e_primo(num: int) -> bool:
    qtd = 0

    for i in range(2, num):
        if num % i == 0:
            return False
        
    if qtd == 2:
        return True
    else:
        return False


# PP

qtd = 0
num = 1

while qtd < 4000:
    if e_primo(num) == True:
        #print(num)
        qtd += 1
    num += 1

print(num)
