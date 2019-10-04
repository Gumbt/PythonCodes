n = int(input())
for i in range(n):
    p = int(input())
    ini = 1
    grao = 1
    for j in range(p-1):
        ini = (ini*2)
        grao = grao+ ini
    grama = int(grao/12)
    print(int(grama/1000), "kg")
    
