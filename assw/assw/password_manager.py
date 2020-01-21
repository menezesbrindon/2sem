class pman:
    pw=[]
    def get_password(self):
        if len(self.pw)>0:
            
         x=self.pw[-1]
         return x

    def set_password(self,t):
        if not t in self.pw:
          self.pw.append(t)
        else:
            print("password exists")

    def is_correct(self,t):
        if t == self.pw[-1]:
            return True
        else:
            return False

a=pman()
while(1):
 print('\n')
 i=int(input("1:get password \n2:set password \n3:verify\n"))
 if i==1:
    j=a.get_password()
    print(j)
 elif i==2:
    s=input("enter new password")
    a.set_password(s)
 elif i==3:
    s=input("enter password")
    x=a.is_correct(s)
    if x:
        print("verified")
    else:
        print("wrong password")
 else:
    break
          
