def binarysearch(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else: 
            right=mid-1
    return -1
arr=[23,25,28,32,37,42,48,49,56,59]
target=59
result=binarysearch(arr,target)
if result !=-1:
    print("Element is Found!! at index {}".format(result))
else:   
    print("Element is not Found!!")