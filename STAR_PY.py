# cook your dish here

T = int(input(""))

if T in range(1,26):
    for i in range(0,(T)):
        N = int(input(""))
        if N in range(2,101):
            for i in range(N, 0, -1):
                for j in range(0, i):
                    print("*",end="")
                print("\r")
