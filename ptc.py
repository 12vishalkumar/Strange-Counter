import math
import os
import random
import re
import sys
# Complete the 'strangeCounter' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
def strangeCounter(t):
    # Write your code here
    cy = 3
    while(t > cy):
        t -= cy
        cy *= 2
    return(cy-t+1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    result = strangeCounter(t)
    fptr.write(str(result) + '\n')
    fptr.close()