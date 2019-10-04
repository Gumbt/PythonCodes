n = int(input())
for i in range(n):
    f = float(input())
    cont = 0
    while f >= 1:
        f = 0.5*f
        cont = cont+1;
    print("%d dias" %cont)
