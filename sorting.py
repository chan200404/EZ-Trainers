l=[5,7,23,10,15]
for j in range (0,len(l)):
    for i in range(0,len(l)-1-j):
         if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
                                 
print(l)