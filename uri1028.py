n = int(input())
for i in range(n):
    f1, f2 = map(int,input().split())
    resto = None
    while resto is not 0:
        resto = f1 % f2
        f1 = f2
        f2 = resto
    print(f1)