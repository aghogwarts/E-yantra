# cook your dish here

T = int(input())

if T in range(1,26):
    for i in range(0,(T)):
        length = int(input())
        num_list = input()
        L = num_list.split(" ")
        sum = 0
        run = True
        new_L = list()
        if length in range(8,51):
            for n in L:
                try:
                    int_n = int(n)
                    new_L.append(int_n)
                except ValueError:
                    run = False
            if run == True:
                for n in new_L:
                    if n not in range(-100,101):
                        run = False
                if run == True:
                    rev_L = new_L[::-1]
                    for i in rev_L:
                        print(i, end = ' ')
                    print("\r")
                    third_L = new_L[::3]
                    third_L = third_L[1::]
                    for a in range(0,len(third_L)):
                        third_L[a] = third_L[a] + 3
                    print(*third_L)
                    fifth_L = new_L[::5]
                    fifth_L = fifth_L[1::]
                    for a in range(0,len(fifth_L)):
                        fifth_L[a] = fifth_L[a] - 7
                    print(*fifth_L)
                    sum = 0
                    sum_L = new_L[3:8:]
                    for i in sum_L:
                        sum = sum + i
                    print(sum)
