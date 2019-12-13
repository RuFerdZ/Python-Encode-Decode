#variable which stores the alphabet letters
alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

print("-------------------------------------------------")
print("                 Text Encoding")
print("-------------------------------------------------")

#ask the user for the text that is to be encoded
text=input("Enter Text to be Encoded : ")

valid=False
while valid==False:
    #try/except catches any instance when any other character other than an integer is entered
    try:
        print("-------------------------------------------------")
        key=int(input("Enter Shift key value : ")) #get the shift key value
        print("-------------------------------------------------")
        while ((key<1)or(key>25)):   #checks whether the key is a value between 1 and 25
            print("Key is out of range!!!Enter a key between range 1-25")
            key=int(input("Enter Shift key value : ")) #get the shift key value
            print("-------------------------------------------------")
        else:
            valid=True
    except:
        print("Please Enter a Valid Key!!!")
            
#algorithm which encodes the user input text
en_text=''
for letter in text:
    for index in range(26):
        if letter in alphabet:
            while letter==alphabet[index]:
                en_text=en_text+alphabet[index+key]
                break
        else:
            en_text=en_text+letter
            break
print("Encrypted Text : ",en_text)
print("=================================================")
