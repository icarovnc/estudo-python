peso = float(input('Digite seu peso(KG): '))
altura = float(input('Digite sua altura(CM): '))
imc = peso/((altura / 100) ** 2)
if imc <= 18.5:
    print(f'ABAIXO DO PESO! Seu IMC é {imc:.1f} kg/m2')
elif imc <= 25:
    print(f'PESO IDEAL! Seu IMC é {imc:.1f} kg/m2')
elif imc <= 30:
    print(f'SOBREPESO! Seu IMC é {imc:.1f} kg/m2')
elif imc <= 40:
    print(f'OBESIDADE! Seu IMC é {imc:.1f} kg/m2')
else:
    print(f'OBESIDADE MORBIDA! Seu IMC é {imc:.1f} kg/m2')
