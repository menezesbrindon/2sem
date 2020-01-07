a=input('enter the string')
b=len(a)
s=''
d=''

x=[]

print('the encoded text is:')
for i in range(0,b,2):
    x.append(a[i])
for i in range(1,b,2):
    x.append(a[i])
    
s=''.join(x)
print(s)
print('the decoded text is:')
#print(x)
m=0

for i in s[0:b//2+1]:
    #print(i)
    x[m]=i
    m=m+2

m=1
for i in s[b//2+1:]:
    #print(i,m,len(x))
    x[m]=i
    m=m+2
#print(x)   
d=''.join(x)
print(d)


