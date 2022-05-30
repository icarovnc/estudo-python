a1=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razão da PA: '))
c=0
print(a1)
while c<9:
    an=a1+razao
    a1=an
    print(an)
    c+=1