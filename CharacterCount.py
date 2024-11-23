randomstr = input("Please enter string.")
charcount = {}
randomstr = randomstr.lower()

for char in randomstr:
    if char.isalpha(): 
        if char in charcount: 
            charcount[char] +=1
        else:
            charcount[char] = 1
print(charcount)