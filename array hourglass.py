import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    max=-1000000
    s=0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            s=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if s>max:
                max=s
            s=0   
    print(max)
        }
    }
    
}
