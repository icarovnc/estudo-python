from time import sleep
def contador (inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()


contador(1, 10, 2)
contador(10, 1, 1)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))
