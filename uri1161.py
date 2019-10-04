def fatorial(num):
    fat = 1
    i = 2
    while i <= num:
        fat = fat*i
        i = i + 1
    return fat
while True:
    try:
        f1, f2 = map(int,input().split())
        print(fatorial(f1)+fatorial(f2))
    except EOFError:
        break