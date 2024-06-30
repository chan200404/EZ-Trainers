def calc_max(p,w,C,n):
    if n==0 or C==0:
        return 0
    if (w[n-1]>C):
        return calc_max(p,w,C,n-1)
    else:
        return max((p[n-1]+calc_max(p,w,C-w[n-1],n-1)),calc_max(p,w,C,n-1))





p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
C=15
n=len(p)
print(calc_max(p,w,C,n))