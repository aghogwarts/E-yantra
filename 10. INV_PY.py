# cook your dish here
T = int(input())

if T in range(1,26):
    for i in range(0,T):
        N = int(input())
        L = []
        if N in range(1,101):
            for i in range(0,N):
                item = input().split()
                item[1] = int(item[1])
                L.append(item)
        M = int(input())
        if M in range(1,101):
            for i in range(0,M):
                operation = input().split()
                operation[2] = int(operation[2])
                if operation[0] == "ADD" or "DELETE":
                    if operation[2] in range(1,101):
                        if operation[0] == "ADD":
                            present = False
                            for i in range(0,len(L)):
                                if L[i][0] == operation[1]:
                                    L[i][1] = operation[2] + L[i][1]
                                    print(f"UPDATED Item {L[i][0]} {L[i][1]}")
                                    present = True
                            if present == False:
                                addinv = operation[1:]
                                L.append(addinv)
                                print(f"ADDED Item {operation[1]}")
                            #print(L)
                        if operation[0] == "DELETE":
                            present = False
                            for i in range(0,len(L)):
                                if L[i][0] == operation[1]:
                                    if L[i][1] < operation[2]:
                                        print(f"Item {operation[1]} could not be deleted")
                                    else:
                                        L[i][1] = L[i][1] - operation[2]
                                        print(f"DELETED Item {operation[1]}")
                                    present = True
                            if present == False:
                                    print(f"Item {operation[1]} does not exist")
                            #print(L)
            sum = 0
            for i in L:
                sum = sum + i[1]
            print(f"Total items in inventory: {sum}")
                        
