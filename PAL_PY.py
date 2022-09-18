# cook your dish here

T = int(input(""))
if T in range(1,26):
    for i in range(0,(T+1)):
        string=(input("")).lower()
        if len(string) in range(2,101):
            if(string==string[::-1]):
                print("It is a palindrome")
            else:
                print("It is not a palindrome")
