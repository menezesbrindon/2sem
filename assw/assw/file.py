a=input('enter the file name')
fh=open(a,'r')
fk=open('file2.txt','w')
for i in fh:
    s=i.split(" ")
    #x=s[0].split()
    #print(s)
    fk.write(s[0].capitalize()+' '+s[1].capitalize()+" "+s[2]+" "+"301-"+s[3])
    
fh.close()
fk.close()
