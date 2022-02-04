cont = s = n = 0
while True:
    n = int(input(f'Digite o {cont + 1}° número: [999 para parar] '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados {cont} números e a soma deles é {s}')