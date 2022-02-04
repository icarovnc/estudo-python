from datetime import date
nascimento = int(input('\033[7;36;107mQual sua data de nascimento?\033[m '))
idade = date.today().year - nascimento
print(f'\033[7;32;107mO atleta em {idade} anos\033[m')
if idade <= 9:
    print('\033[7;32;107mMIRIM\033[m')
elif idade <= 14:
    print('\033[7;32;107mINFANTIL\033[m')
elif idade <= 19:
    print('\033[7;32;107mJUNIOR\033[m')
elif idade <=20:
    print('\033[7;32;107mSENIOR\033[m')
elif idade > 20:
    print('\033[7;32;107mMASTER\033[m')