"""

Provides interfaces for automatic encrption and decryption, as well as cryptanalysis tools such as
    - Frequency analysis
    - Brute force attack measurements

Encryption and decryption treat puncuation as another letter

During encryption, if there isn't a corresponding letter in the passphrase, it's saved as the plaintext equivalent

"""

import random

def encrypt(plaintext, passphrase):
    phrase=passphrase.lower().split()
    plaintext=plaintext.lower()
    encrypted=""

    for i in plaintext:
        availableWords=[]

        j=0
        while j<len(phrase):
            if i in phrase[j]:
                availableWords.append(j)

            j+=1

        if not availableWords:
            encrypted+=i+" "
            continue

        wordIndex=random.choice(availableWords)
        
        k=0
        availableLetters=[]

        while k<len(phrase[wordIndex]):
            if phrase[wordIndex][k]==i:
                availableLetters.append(k)
            k+=1
        
        letterIndex=random.choice(availableLetters)

        encrypted+=str(wordIndex)+"/"+str(letterIndex)+" "

    return(encrypted)

def decrypt(ciphertext, passphrase):
    passphrase=passphrase.lower()
    sentence=ciphertext.split("   ")
    passphrase=passphrase.split()
    decrypted=""
    
    for word in sentence:
        letters=word.split()
        for letter in letters:
            if "/" not in letter:
                decrypted+=letter
            else:
                numbers=letter.split("/")
                decrypted+=passphrase[int(numbers[0])][int(numbers[1])]
        decrypted+=" "

    return(decrypted)

def frequencyAnalysis(ciphertext, format='count'):
    """
    Takes two variables, the ciphertext in the format 'x/x x/x x/x a x/x x/x' and the format of the data to be returned

    Formats are
        - Percentage - The percentage of each letter relative to the overall ciphertext
        - Count (Default) - The count of each letter

    Returns two lists, letters and frequency, which are the unique letters in the taken ciphertext and their respective frequency in the specified format (If there isn't a specified format it returns as counts)

    """

    ciphertext=ciphertext.replace("  ", "").split()

    letters=[]
    counts=[]

    for letter in ciphertext:
        if letter not in letters:
            letters.append(letter)
            counts.append(1)
        else:
            index=letters.index(letter)
            counts[index]+=1
    if format=='percentage':
        i=0
        total=0
        amount=len(counts)
        for l in counts:
            total+=l
        while i<amount:
            counts[i]=(counts[i]/total)*100
            i+=1

    return(letters, counts)
