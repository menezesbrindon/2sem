a=int(input("enter the no"))
fib=[1,1]
i=1
while a>i:
    fib.append(fib[i]+fib[i-1])
    i=i+1
for x in fib:
    print(str(x),end=' ')
