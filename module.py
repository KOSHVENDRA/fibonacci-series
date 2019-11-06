def fibon(n):
    L=[0,1]
    for i in range(n):
        L=L+[L[i]+L[i+1]]

    print(L)
