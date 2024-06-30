n=int(input())
count=0
if n<1000:
    None
for i in range(1000,n+1):
    if i%1000<10:
        count+=1
    if i%100000<10:
        count+=1

print(count)
    


