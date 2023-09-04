def mergesort(lo,hi,arr):
    if(lo>=hi):
        return
    mid=(lo+hi)//2
    mergesort(lo,mid,arr)
    mergesort(mid+1,hi,arr)
    merge(arr,lo,mid,hi)
    return(arr)
def merge(arr,lo,m,hi):
    p1=lo
    p2=m+1
    ar=[]
    while(p1<=m and p2<=hi):
        if(arr[p1]<arr[p2]):
            ar.append(arr[p1])
            p1+=1
        else:
            ar.append(arr[p2])
            p2+=1
    while(p1<=m):
        ar.append(arr[p1])
        p1+=1
    while(p2<=hi):
        ar.append(arr[p2])
        p2+=1
    k=0
    for i in range(lo,hi+1):
        arr[i]=ar[k]
        k+=1
a=[3,1,8,0,4]
print(mergesort(0,4,a))
    
