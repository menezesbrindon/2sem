'''import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('172.16.57.96',80))
msg='http://  HTTP/1.0'.encode()
s.send(msg)'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
 nd = input().split()
 l=0
 n = int(nd[0])
 x=[0,0,0,0,0]
 d = int(nd[1])

 a = list(map(int, input().rstrip().split()))
 
 ''' for i in range(0,d):
        t=a[0]
        del a[0]
        a.append(t)
    for i in a:
        print(i,end=" ")'''




