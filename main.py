def openOrSenior(data):
    category=[]
    for i in range(len(data)):
        if (data[i][0]>=55 and data[i][1]>7):
            category.append('Senior')
        else:
            category.append('Open')
    return category
            
    