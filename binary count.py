import math
import os
import random
import re
import sys



if __name__ == '__main__':
    max=0
    n = int(input())
    st=""
    while n>0:
        r=n%2
        n=n//2
        st=str(r)+st
    count=0
    for i in range(0,len(st)):
        if st[i]=='1':
            count=count+1
            if count>max:
                max=count
        else:
            count=0
    print(max)   

