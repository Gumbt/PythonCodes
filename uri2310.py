ar=float()
br=float()
cr=float()
a1r=float()
b1r=float()
c1r=float()
cont = int(input())
for i in range(cont):
    nome = input()
    a,b,c = map(int,input().split())
    a1,b1,c1 = map(int,input().rsplit())
    ar+=a
    br+=b
    cr+=c
    a1r+=a1
    b1r+=b1
    c1r+=c1
print('Pontos de Saque: {:.2f} %.\n'
      'Pontos de Bloqueio: {:.2f} %.\n'
      'Pontos de Ataque: {:.2f} %.'
      .format(100*a1r/ar,100*b1r/br,100*c1r/cr))