#----------------------------FUNCTIONS---------------------------#

#a function which validats the user entered shift key
def validateShiftValue():
    valid=False
    while valid==False:
        #try/except catches any instance when any other character other than an integer is entered
        try:  
            print("-------------------------------------------------")
            key=int(input("Enter Shift key value : "))  #get the shift key value
            print("-------------------------------------------------")
            while ((key<1)or(key>25)):   #checks whether the key is a value between 1 and 25
                print("Key is out of range!!!Enter a key between range 1-25")
                key=int(input("Enter Shift key value : "))
                print("-------------------------------------------------")
            else:
                valid=True
        except:
            print("Please Enter a Valid Key!!!")
    return key

#a function which encodes a given string
def encoding():
    text=input("Enter Text to be Encoded : ")
    key=validateShiftValue()   #calls function to input and validate the shift key value
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
    print("Encoded text : ",en_text)

#a function which decodes an encoded string
def decoding():    
    text=input("Enter Text to be Decoded : ")
    key=validateShiftValue()   #calls function to input and validate the shift key value
    de_text=''
    for letter in text:
        for index in range(26):
            if letter in alphabet:
                while letter==alphabet[index]:
                    de_text=de_text+alphabet[(26+index)-key]
                    break
            else:
                de_text=de_text+letter
                break
    print("Decoded text : ",de_text)

#a function which compares the encoded against decoded to determine the key and the rest of the string
def analysingKey():
    en_text=input("Enter encoded text : ")
    de_text=input("Enter part of decoded text : ")
    en_positionCount=0
    de_positionCount=0

    #find the letter occurence position ii the alphabet string variable
    for i in range (len(de_text)):
        if en_text[i]==de_text[i]:
            continue
        else:
            break        
    for letter in alphabet:
        if de_text[i]==letter:
            break
        else:
            de_positionCount+=1

    for letter in alphabet:
        if en_text[i]==letter:
            break
        else:
            en_positionCount+=1
            
    #Calculating the shift key
    key=en_positionCount-de_positionCount
    
    #decoding the string
    de_text=''
    for letter in en_text:
        for index in range(26):
            if letter in alphabet:
                while letter==alphabet[index]:
                    de_text=de_text+alphabet[index-key]
                    break
            else:
                de_text=de_text+letter
                break
    print("Decoded text :",de_text)

    #when the alphabet string wraps the key value can change
    #this section calculates the correct key value
    if de_text[i]<en_text[i]:
        print("Shift key :",key)
    else:
        print("Shift key :",26+key)


#----------------------------MAIN PROGRAM---------------------------#


#Display options to the user       
print("--------------------------------------------")
print("    Part 2 : Encoding/Decoding Strings ")
print("--------------------------------------------")
print("Options")
print("---------")
print("'e'- Encode Text")
print("'d'- Decode Text")
print("'a'- Analyse key and decode")
print("'q'- Quit Program")
print("--------------------------------------------")

#variable to hold the alphabet
alphabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
while True:
    #Getting the user option
    option=input("Enter your Option : ")

    #validating the user option
    while ((option!='e')and(option!='d')and(option!='q')and(option!='a')):
        option=input("Invalid option please re-enter : ")
    else:
        print("--------------------------------------------")


    #the user option is directed to the specific module 
    if option=="e":
        encoding()
    elif option=="d":
        decoding()
    elif option=="a":
        analysingKey()
    else:
        print("program is exiting.....")
        break
    print("=============================================")
        
