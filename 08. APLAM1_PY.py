# cook your dish here
# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []
    term = a1
    AP_series.append(term)
    for i in range(1,n):
        term = term + d
        AP_series.append(term)
        
    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    T = int(input())

    if T in range(1,26):
        for i in range(0,T):
            data = input()
            a1, d, n = data.split()
            a1 = int(a1)
            d = int(d)
            n = int(n)
            
            if a1 > 0 and a1 < 101 and d > 0 and d < 101 and n > 0 and n < 101:
                AP_series = generate_AP(a1, d, n)
                print(*AP_series)
                
                # Using lambda and map functions, find squares of terms in AP series and print it
                square = lambda x: x*x
                sqr_AP_series = list(map(square, AP_series))
                print(*sqr_AP_series)

                # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
                sum_sqr_AP_series = reduce(lambda a, b: a + b, sqr_AP_series)
                print(sum_sqr_AP_series)







