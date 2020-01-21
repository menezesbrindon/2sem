import re
x=''
b=[]
fh=open("file.txt",'r')
for i in fh:
 m=i.split()
 for k in m:
  #print(k)
  a=re.findall(".*a+.*e+.*i+.*o+.*u+.*",k)
  #print(a)
  for j in a:
   if j==" ":
       continue
   else:
       b.append(j)

x=''.join(b)
print(x.strip())

