import itertools
x=[]
y=[]
a=(input())
for i in itertools.permutations(a):
    x.append(int(''.join(i)))
for i in x:
    
    minv=0
    #print(i)
    if i > int(a):
        y.append(i)
if len(y)==0:
   print(a)
else:
    print(min(y))
