def mylist(n):
    mylist=[]
    for i in range(1,n+1):
        if n%i==0:
            mylist.append(i)
    return mylist
print(mylist(256))