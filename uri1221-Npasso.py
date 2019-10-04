##Tem que ser mais rapido
def isPrimo(num):
    if num == 2:
        return 1
    if num !=0 and num != 1 and num%2!=0:
        for i in range(3,int(num/2),2):
            if(num%i==0):
                return 0
        return 1
    return 0

n = int(input())
for i in range(n):
    f = int(input())
    if(isPrimo(f)):
        print("Prime")
    else:
        print("Not Prime")
