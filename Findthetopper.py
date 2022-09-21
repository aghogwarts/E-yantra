T=int(input(""))
no_stud=int(input(""))
dictionary={}
if T in range(1,26):
    for i in range(0,no_stud):
        item=input("")
        x,y=item.split()
        dictionary.update({x:y})
keymax=max(dictionary, key= lambda x:dictionary[x] )        
print(keymax)
