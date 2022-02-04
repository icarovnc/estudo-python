import math

ang = float(input('Digite o ângulo: '))
print('O coseno é {:.2f}'.format(math.cos(math.radians(ang))))
print('O Seno é {:.2f}'.format(math.sin(math.sin(ang))))

# angulo = float(input('Digite o angulo que você deseja'))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tan = math.tan((math.radians(ang)))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
print('O angulo de {} tem o COSENO de {:.2f}'.format(ang, seno))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
