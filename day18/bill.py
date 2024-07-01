c=[1,5,7] 
c.sort(reverse=True)
a=18
i=0
s=0
while a>0:
 if a>=c[i] and i<len(c):
    s+=1
    a=a-c[i]
 else:
    i+=1
print(s)    





