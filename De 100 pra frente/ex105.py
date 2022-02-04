lista = []
situação = False

def ficha(lst, sit=False):
    '''
    ->>> pega uma lista e verifica a situação do aluno
    parametro 1: pega uma lista que vai ser incorporada em um dicionário
    parametro 2: verifica se a pessoa quer ver ou nao a situação do aluno
    return: retorna dicionario com iformações do aluno
    '''
    notas = {}
    media = sum(lst) / len(lst)
    notas['total'] = len(lst)
    notas['maior'] = max(lst)
    notas['menor'] = min(lst)
    notas['media'] = media
    if sit == True:
        if notas['media'] < 5:
            notas['sitação'] = 'RUIM'
        if notas['media'] < 8:
            notas['sitação'] = 'RAZOAVEL'
        if notas['media'] >= 8:
            notas['sitação'] = 'BOA'
    return notas

# main program #
while True:
    lista.append(float(input('Digite as notas: ')))
    opt = str(input('Adicionar outra nota? [S/N] ')).strip().upper()
    while opt not in 'SN':
        opt = str(input('Opção inválida. Adicionar outra nota? [S/N] ')).strip().upper()
    if opt == 'N':
        break
while True:
    opt = str(input('Mostrar situação? [S/N]')).strip().upper()
    while opt not in 'SN':
        opt = str(input('Opção inválida. Mostrar situação? [S/N] ')).strip().upper()
    if opt == 'S':
        situação = True
        break
    if opt == 'N':
        situação = False
        break
print(ficha(lista, situação))
help(ficha)