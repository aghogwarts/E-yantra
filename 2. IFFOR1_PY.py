# cook your dish here

T = int(input())

if T in range(1,26):
    for x in range(0,(T)):
        n = int(input())
        if n in range(0,101):
            for i in range(0,n):
                if i == 0:
                    i = i + 3
                    print(i, end=" ")
                else:
                    if i % 2 == 1:
                        print(i*i, end=" ")
                    else:
                        print(i*2, end=" ")
        print("\r")
