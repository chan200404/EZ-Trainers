n=list(map(int,input().split()))
temp=1
for i in range(0,len(n)):
    if n[i]<temp:
        temp=n[i]
print(temp)        