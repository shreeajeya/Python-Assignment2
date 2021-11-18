def table(n):
    return lambda a:a*n
n=2
b=table(n)
for i in range(1,11):
    print(b(i))