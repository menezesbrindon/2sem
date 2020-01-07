a=input('enter the string')
a=a.lower()
x=a.split()
count=0
for i in x:
    if i in ['a','the','an']:
        count=count+1
print('count=',count)
