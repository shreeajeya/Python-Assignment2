def BinarySort(arr, start, end, key):
    if end >= start:
        mid = start + (end - start) // 2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return BinarySort(arr, start, mid - 1, key)
        else:
            return BinarySort(arr, mid + 1, end, key)
    else:
        return -1
arr=sorted(['4','6','7','8','9'])
key='4'
result=BinarySort(arr,0,len(arr)-1,key)
if result!=-1:
    print("element is at:"+str(result))
else:
    print("element not found")
