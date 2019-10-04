n = int(input())
for i in range(n):
    n1, n2 = input().split()
    n1len = len(n1)
    n2len = len(n2)
    if(n1[(n1len-n2len):n1len]==n2):
        print("encaixa")
    else:
        print("nao encaixa")
    
