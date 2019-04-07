def no_space(x):
    A=x.split()
    striped=''
    for i in range(0,len(A)):
        striped=str(striped)+A[i]
    return striped


print(no_space('hey my name is paolo'))