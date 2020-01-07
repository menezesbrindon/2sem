i=3
p=[]
while i<10001:
    x=[0]
    #print(i)
    for j in range(1,i):
        
        if i%j==0:
            x.append(j)
            
    #print(x)
    if sum(x)==i:
        p.append(i)
    i=i+1
print("the perfect num are",p)
     
    
