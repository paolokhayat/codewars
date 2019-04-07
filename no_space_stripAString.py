def no_space(x):
    A=x.split()
    stripped=''
    for i in range(0,len(A)):
        stripped=str(stripped)+A[i]
    return stripped


print(no_space('hey my name is paolo'))
