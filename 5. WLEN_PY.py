# cook your dish here
T = int(input())

if T in range(1, 26):
    for x in range(0, T):
        str = input()
        str = str[1:]
        wordlist = str.split(" ")
        for i in wordlist:
            if i.isalpha() == False:
                exit()
        for a in range(0, len(wordlist)):
            if a == len(wordlist) - 1:
                print(len(wordlist[a]))
            else:
                print(len(wordlist[a]), end = ",")
