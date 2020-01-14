def s(sum1):
 while(sum1>9):
   n=sum1
   sum1=0
   while(n!=0):
       sum1=sum1+n%10
       n=n//10
 return sum1


a=int(input('num'))
s2=s(a)

print("digital root",s2)

print("USING MOD 9:",a%9)

      
