a=input('enter the string')

print('the lenth of the string is',len(a))
print('string *10=',a*10)
print('first char of the string is',a[0])
print('first 3 char of the string is',a[0:3])
print('last 3 char of the string is',a[len(a)-3:])

print('the string backwards is',a[::-1])
print('the 7 char of the string is',a[6])
print('last and first  char removed of the string is',a[1:len(a)-1])
print('string in upper',a.upper())
b=a.replace('a','e')
print(b)
for i in a:
    print(' ',end='')
    
