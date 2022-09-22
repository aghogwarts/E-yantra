# cook your dish here
def dec_to_binary(n):
    bin_num = None
    if (n == 0):
        bin_num = 0
    else:
        bin_num = ((n%2)+10*dec_to_binary(n//2))
    return bin_num
    
if __name__ == '__main__':
    
    # take the T (test_cases) input
    T = int(input())
    
    if T in range(1, 26):
        # Write the code here to take the n value
        for a in range(0,T):
        # take the n input values
            n = int(input())
            if n in range(0, 256):
                # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
                bin_num = dec_to_binary(n)
                bin_num = str(bin_num)
                bin_num = bin_num.zfill(8)
                print(bin_num)
    
