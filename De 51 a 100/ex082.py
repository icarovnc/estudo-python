numeros = []
lista_par = []
lista_impar = []
continuar = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 == 1:
            lista_impar.append(n)
    continuar = str(input('Deseja continuar? [S/N]')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('Opção inválida. \nDeseja continuar? [S/N]')).strip().lower()
    if continuar == 'n':
        break
print(lista_par)
print(lista_impar)