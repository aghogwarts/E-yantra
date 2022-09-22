# cook your dish here

import math
from math import sqrt

def compute_distance(x1, y1, x2, y2):

    distance = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print("Distance: %.2f" % distance)
    
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    T = int(input())
    
    # Write the code here to take the x1, y1, x2 and y2 values
    if T in range(1, 26):
        for i in range(0, T):
            cood = input().split(" ",3)
            
            
            x1 = int(cood[0])
            y1 = int(cood[1])
            x2 = int(cood[2])
            y2 = int(cood[3])
            if((x1>-101 and x1<101) and (y1>-101 and y1<101) and (x2>-101 and x2<101) and (y1>-101 and y2<101)):
                
                # Once you have all 4 values, call the compute_distance function to find Euclidean distance
                compute_distance(x1, y1, x2, y2)
