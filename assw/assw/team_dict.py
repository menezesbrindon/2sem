num=int(input("Enter the Value"))
d={}
for i in range(num):
    t1=input("Enter the team Name :")
    t2=int(input("Enter the wins :" ))
    t3=int(input("Enter the loss :"))
    d[t1]=[t2,t3]
print(d)
t3=input("Enter the team name")
a=d[t3]
print((a[0]/(a[0]+a[1]))*100)
l=[]
for i in d:
    a=d[i]
    l.append(a[0])
print(l)
