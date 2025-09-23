hora = int(input('Digite a hora: '))
minuto = int(input('Digite o minuto: '))
segundo = int(input('Digite o segundo: '))

segundos = hora * 3600 + minuto * 60 + segundo

print(f'Tempo em segudos = {segundos}')
