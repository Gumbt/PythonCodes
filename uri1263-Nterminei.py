entrada = input()
vet = [len(entrada)]
cont = 0
for i in range(len(entrada)):
    if(i==0):
        vet[0] = entrada[i]
    else:
        if(entrada[i]==' '):
            vet.append(entrada[i+1])
#for i in range(len(vet)):
    #for j in range(len(vet)):
        ##if(i!=j and (ord(vet[i])==ord(vet[j]) or ord(vet[i]) == (ord(vet[j])-32))):
