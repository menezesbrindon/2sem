def merge(a,b):
    c=a+b
    #print(c)
    return c


a=[1,2,3,4,5,6]
b=[1,8,10,12]
x=merge(a,b)
#print(x)
print("using sort method",sorted(x))
print("without using sort")
for i in range(0,len(x)):
    for j in range(0,len(x)-1):
     if x[j]>x[j+1]:
        a=x[j]
        x[j]=x[j+1]
        x[j+1]=a
        
print(x)
