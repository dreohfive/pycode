#binary search recursive approach
def binary_search(lst,n):
    low=0
    high=len(lst)-1
    while low<=high:
        mid=(low+high)//2
        if lst[mid]<n:
            low=mid+1
        elif lst[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
lst=[1,2,3,4,5,6,7]
print(binary_search(lst,5))

#binary search itertive approach
def binary_search(lst,low,high,n):
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==n:
            return mid
        elif lst[mid]<n:
            return binary_search(lst,mid+1,high,n)
        else:
            return binary_search(lst,low,mid-1,n)
        return mid
    return -1
lst=[1,2,3,4,5,6,7]
print(binary_search(lst,0,len(lst)-1,5))

#linear search
def linear_search(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            return i
    return -1
lst=[1,2,3,4,5,6,7]
print(linear_search(lst,5))
