def kmpalgo(p,s):
    m=len(p)
    n=len(s)
    lps=[]
    lps(p,m,lps)
    print(lps)
    i=0 
    j=0
    
    while(n-i)>(m-j):
        if p[j]==s[i]:
            i+=1
            j+=1

            if j==m:
                print("pattern found",i-j)
                j=lps[j-1]
            elif i<n and p[j]!=s[i]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1

def lps(p,m,lps):
    lps.append(0)
    l=[]
    for i in range(len(p)):
        if p[i]==p[j]:
            l.append(j+1)
            j=j+1
        else:
            j=0
            l.append(j)

if __name__=="__main__"  :
    p='ABABACDEABABABCABCABDAA'
    s='ABCAB'


kmpalgo(p,s)        





    

       

       


