def calc_max(p,w,C,n):
    if n==0 or C==0:
        return 0
    if DP[n][C]!=-1:
        return DP[n][C]
    if (w[n-1]>C):
        DP[n][C]=max((p[n-1]+calc_max(p,w,C-w[n-1],n-1)),calc_max(p,w,C,n-1))

        return DP([n][C])
    else:
        DP[n][C]=calc_max(p,w,C,n-1)
        return DP[n][C]
    





p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
C=15
n=len(p)
DP=[[-1 for i in range(C+1)] for j in range(n+1)]
calc_max(p,w,C,n-1)
print(DP)
