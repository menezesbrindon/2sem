class wordplay:
    words=[]
    x=[]
    def __init__(self,l):
        self.words=self.words+l
        
    def wwl(self,l):
        x=[]
        if len(self.words)>0:
            for i in self.words:
               # print(i)
                if len(i)==l:
                   # print(i)
                    x.append(i)
        return x

    def sw(self,t):
      x=[]
      if len(self.words)>0:
            for i in self.words:
                if i.startswith(t):
                    x.append(i)
      return x
    def ew(self,t):
      x=[]
      if len(self.words)>0:
            for i in self.words:
                if i[-1]==t:
                    x.append(i)
      return x
    def pal(self):
         x=[]
         if len(self.words)>0:
            for i in self.words:
                w=i[::-1]
                print(w)
                if i==w:
                    x.append(i)
         return x
    def ol(self,t):
         x=[]
         if len(self.words)>0:
            for i in self.words:
                if t in i:
                    x.append(i)
            
         return x
    def nl(self,t):
         x=[]
         if len(self.words)>0:
            for i in self.words:
                if not t in i:
                    x.append(i)
            
         return x
lis=['cat','rat','bat','saturday','mat','malayalam']
a=wordplay(lis)
while(1):
 print('\n')
 i=int(input("1:words with lenght \n2:starts with \n3:end with\n4:palindrome\n5:only l\n6:not l"))
 if i==1:
    l=int(input('len'))
    j=a.wwl(l)
    print(j)
 elif i==2:
    s=input("enter letter")
    m=a.sw(s)
    print(m)
 elif i==3:
    s=input("enter letter")
    m=a.ew(s)
    print(m)
 elif i==4:
    #s=input("enter letter")
    m=a.pal()
    print(m)
 elif i==5:
    s=input("enter letter")
    m=a.ol(s)
    print(m)
 elif i==6:
    s=input("enter letter")
    m=a.nl(s)
    print(m)
 else:
    break
