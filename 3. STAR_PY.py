# cook your dish here

T = int(input())

if T in range(1, 26):
    for x in range(0, T):
        N = int(input())
        if N in range(1,101):
            for i in range(N, 0, -1):
                for j in range(1, i+1):
                    if j % 5 == 0:
                        print("#", end = "")
                    else:
                        print("*", end = "")
                print("\r")
