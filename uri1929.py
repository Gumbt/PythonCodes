A,B,C,D = map(int,input().split())
aux = 0
if(A+B>C and B+C>A and A+C>B):
    print('S')
elif(D+B>C and B+C>D and D+C>B):
    print('S')
elif(D+A>C and A+C>D and D+C>A):
    print('S')
elif(D+B>A and B+A>D and D+A>B):
    print('S')
else:
    print('N')