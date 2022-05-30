num = int(input('Digite o número para ver sua tabuada: '))
ate = int(input('Digite até qual numero vai ser a tabuada: '))
for i in range(1, ate+1):
    print(f'{num} X {i} = {num * i}')
