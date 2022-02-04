from time import sleep
nome = str(input('\033[1;34;107m Informe seu nome:\033[m ')).title()
nota = [0, 1]
nota[0] = float(input('\033[1;34;107mInforme a primeira nota:\033[m '))
nota[1] = float(input('\033[1;34;107mInforme a segunda nota:\033[m '))
print('>' * 30)
sleep(2)
media = sum(nota) / len(nota)
print(media)
if media < 5.0:
    resultado = '\033[1;36;107mREPROVADO\033[m'
elif 5.0 <= media < 6.9:
    resultado = '\033[1;36;107mRECUPERAÇÃO\033[m'
else:
    print('\033[1;36;107mAPROVADO\033[m')
print(resultado)