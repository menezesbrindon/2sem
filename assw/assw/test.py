class analyzer:
    l=[]
    #count=0
    #c1=0
    def __init__(self,t):
        self.l=self.l+t
    def s(self):
        l1=len(self.l)
        print("Number of words:",l1)
    def et(self,x):
        count=int(0)
        print(x)
        for i in self.l:
            if i.startswith(x):
                count=count+1
            
        print("Number of words starting with "+ x +" :")
        print(count)
    def lt(self,x):
        c=0
        for i in self.l:
            if len(i)==x:
                c=c+1
        print("Number of {} letter words:".format(x),end=" ")
        print(c)
str=input("enter the string")
str=str.split()
a=analyzer(str)
a.s()
a.et("c")
a.lt(2)
