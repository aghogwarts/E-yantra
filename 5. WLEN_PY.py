# cook your dish here
T = int(input())

if T in range(1, 26):
    for x in range(0, T):
        str = input()
        str = str[1:]
        if str.isalpha() == True:
            print("a")
            wordlist = str.split(" ")
            for i in wordlist:
                print(len(i), end = ",")
        print("\r")
