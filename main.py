def decryptWord(word):

    counter = 0 #counts tries
    while True: #keep looping until guessed
        ordWord = [] #holds the ord value of every char from the input
        newWord = "" #stores the next iteration of the word

        #gets the ord value of each char from the input
        for i in word:
            ordWord.append(ord(i))

        #generates next iteration
        for i in ordWord:
            if i == 32: #handles space character
                i = 33
            elif i - 1 < 97: #handles looping the alphabet
                i = 123
            newWord += chr(i-1) #gets the char from the alphabet before the current char
            
        print('Is it "'+ newWord + '"?', end = "")
    
        answer = input("\ny/n: ")        
        if answer == "y" or answer == "Y": #if guessed
            counter+=1
            print("\nCiphertext cracked in", counter, "tries.")
            input("Press any key to exit...")
            break
        elif answer == "n" or answer == "N": #if not guessed
            word = newWord #stores the new iteration of the word
            counter+=1
            continue
        else: #wrong input
            print("Wrong input. Exiting...")
            break

def main():

    cipherText = input("Enter ciphertext: ")
    decryptWord(cipherText.lower())


if __name__ == '__main__':
    main()
