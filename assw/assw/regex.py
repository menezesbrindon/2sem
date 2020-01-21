import re
d={'I':1,
   'V':5,
   'X':10,
   'L':50,
   'C':100,
   'M':1000}
m1={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,
"September":9,"October":10,"November":11,"December":12}
   
def rep(x):
    x=x.replace('abc','*')
    return x
def rom(x):
    #print(d['M'])
    s=0+d[x[0]]
    for i in range(1,len(x)):
        if d[x[i]]>d[x[i-1]]:
            s=d[x[i]]-s
        else:
            s=s+d[x[i]]
    return s
def date(x):
    x=x.split(',')
    s=x[0].split()
    print("date:"+str(m1[s[0]])+'/'+s[1]+'/'+x[1])
def m(l):
    g=re.findall('[hb][aiu]t',l)
    print(g)

def id(l):
    g=re.findall('[A-Za-z][A-Za-z0-9]*',l)
    print(g)

i=int(input("1:replace abc by * \n2:roman to arabic\n3:date formatting\n4:match pattern\n5:id \n6:not l"))
if i==1:
    x=input('str')
    y=rep(x)
    print(y)
elif i==2:
    x=input("roman num")
    g=rom(x)
    print(g)
elif i==3:
    x=input('date')
    date(x)
elif i==4:
    x=input('sentence')
    m(x)
else:
    x=input('statement')
    id(x)
    
