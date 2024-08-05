import math
import os
import random
import re
import sys
def plusminus(arr):
    n=len(arr)
    positive=0
    negative=0
    zero=0
    for i in arr:
        if (i>0):
            positive+=0
        elif(i<0):
            negative+=0
        else:
            zero+=0
    print(round(positive/n,5))
    print(round(negative/n,5))
    print(round(zero/n,5))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
