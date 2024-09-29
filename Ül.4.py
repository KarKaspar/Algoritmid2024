
def binaar(alist,n):
    mid=(len(alist)-1)//2
    middle=alist[mid]
    mid2=mid
    algus=0
    lõpp=len(alist)-1
    for i in range(mid+1):
        vastus=mid2
        if n<alist[mid2]:
            lõpp=mid2-1
            mid2=(algus+lõpp)//2
        elif n>alist[mid2]:
            algus=mid2+1
            mid2=(algus+lõpp)//2
        if alist[vastus]==n:
            return vastus
    return "lost"
    

print(binaar([1,2,3,4,5],5))
print(binaar([2,4,6,8,10,12,14,16,18,20],2))
