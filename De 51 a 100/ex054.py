from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pessoas}° pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor =+ 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade e'
      f'\n{totmenor} pessoas menores de diade')