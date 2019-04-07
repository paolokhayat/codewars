def summation(num):
    if num==1 or num==0:
        return num
    else:
        return num+summation(num-1)
