def Merge_sort(L,low,mid,high):
    left=L[low:mid]   
    right=L[mid+1:high]
    temp=[0]*len(l)
    i,j,t=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp[t]=right[j]
            j+=1
            t+=1
    while i<len(left):
        temp[t]=right[j] 
        j+=1
        t+=1       

def Merge(l,low,high):
    if low<high:
        mid=low+(high-low)//2
        Merge(l,low,mid)
        Merge(l,low,mid,high)

if __name__=="__main__":
        l=list(map(int,input().split()))        
        Merge_sort(l,0,len(l)//2,len(l)-1)
        Merge(l,0,len(l)-1)
        print("sorted array=",l)



