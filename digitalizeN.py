def digitize(n):
    b=str(n)
    A=[0 for i in range(0,len(b))]
    i=0
    j=len(b)-1
    while (i<=len(b) and j>=0):
        A[i]=b[j]
        i=i+1
        j=j-1
    A=[int(k) for k in A]
    return A
