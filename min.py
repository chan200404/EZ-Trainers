l=[2,6,9,1]
for i in range (0,len(l)):
    for j in range (0,len(l)-1-i):
        if l[i]>l[i+1]:
            min=l[i+1]
            print(min)