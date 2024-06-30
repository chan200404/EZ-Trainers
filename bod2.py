s=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
l=len(s)
li=[]
for i in range (l):
    next_greater=-1
    for j in range(i+1,l):
        if s[j]<s[i]:
          next_greater=s[j]
          break
    li.append(next_greater)
        
print(li)

        