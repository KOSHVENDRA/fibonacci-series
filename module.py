n=5
L=[0,1]
for i in range(5):
    L=L+[L[i]+L[i+1]]

print(L)
