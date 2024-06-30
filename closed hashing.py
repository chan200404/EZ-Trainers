# linear hashing
l=[]
def linear_probing(k):
    if k==0:
        return False
    n=len(k)
    for i in  range (0,n+1):
        x=k[i]%10
        l[x].append(k)



k=[22,10,47,42,56,100,50,92,99,79]
print(linear_probing)
