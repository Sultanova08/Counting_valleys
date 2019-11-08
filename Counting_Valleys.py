import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    position = 0
    for i in range(n):
        if position == -1 and s[i] == 'U':
           position += 1
           valleys += 1
        elif s[i] == 'D':
            position -= 1
        else:
            position += 1
    return valleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
