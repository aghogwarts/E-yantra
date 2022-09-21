# cook your dish here
T = int(input(""))

if T in range(1,26):
    for a in range(0,T):
        n = int(input(""))
        if n in range(0,101):
            for i in range(0,n):
                if i == 0:
                    print(i + 3, end = " ")
                elif (i == n - 1):
                    if ((i % 2) == 1):
                        print(i*i)
                    else:
                        print(i*2)
                else:
                    if ((i % 2) == 1):
                        print(i*i, end=" ")
                    else:
                        print(i*2,end = " ")
