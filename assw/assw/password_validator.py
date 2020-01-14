d={"a":"123456",
   "b":"456789",
   "b":"123",
   "c":"456",
   "d":"346",
   "e":"469",
   "f":"236",
   "g":"4689",
   "h":"1456",
   "i":"4",}
a=input("enter the user name")
b=input('enter the password')
if a in d:
    if d[a]==b:
        print('logged in')
    else:
        print('password is invalid')
else:
    print('not valid user')
        
