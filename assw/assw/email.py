a=int(input('enter the num of addresses'))
flag=1
for i in range(0,a):
    x=input('enter the address')
    d=x.split('@')
    d=d[1].split('.')
    if d[0]=='prof':
        flag=0

if flag==0:
    print('prof addresses were present')
else:
    print('only student address were present')
    
