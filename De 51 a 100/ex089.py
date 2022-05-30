temp = []
aluno = []
temp_soma = []
while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    aluno.append(temp[:])
    temp.clear()
    opt = str(input('Continuar? [S/N]')).strip().upper()
    while opt not in 'SN':
        opt = str(input('Opção inválida. \nContinuar? [S/N]')).strip().upper()
    if opt == 'N':
        break

print(f"{'N°' : <5}{'Nome' : <10}{'Média' : >8}")
print('-' * 30)
for i, c in enumerate(aluno):
    temp_soma.append((c[1] + c[2]) / 2)
    print(f"{i:<5}{c[0]: <10}{temp_soma[i]:>8}")
print('-' * 30)
mostrar = 0
while mostrar != 999:
    mostrar = int(input('Mostrar a nota de qual aluno? (999 interrompe)'))
    for i, c in enumerate(aluno):
        if mostrar == aluno.index(c):
            print(f'Notas de {aluno[i][0]} são: {aluno[i][1:3]}')
print('Fim')