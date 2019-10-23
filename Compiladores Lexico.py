lista = []
expressao = str(input('Digite a expressão: '))
lista = expressao.split(' ')
print(lista)

for i,v in enumerate(lista):
    if v == '/' or v == '*':
        print(f'{lista[i]} <operador1>')
    elif v == '+' or v == '-':
        print(f'{lista[i]} <operador2>')
    elif not v.isnumeric():
        print(f'{lista[i]} Não é aceito!')
    else:
        print(f'{lista[i]} <constante>')

