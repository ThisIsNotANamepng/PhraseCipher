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

def mostFrequentLetters(plaintext, passphrase, amount=10, stats=False, type="count"):
    """
    Requires two variables, the ciphertext in the format 'x/x x/x x/x a x/x x/x' and the string passphrase

    The other three optional variables are amount, stats, and type
        - amount (Int) dictates how many of the most frequently used letters are returned. Returns from most to least used. Defaults to 10.
        - stats (Boolean) dictates whether the call will return the stats for how often each letter is used. Flagging this as true will make the call return a dictionary of two lists, the first being the stats of the letters in the seconds list. The indexes for each list correlate with each other. For example, maxNumbers[1][3] is the third most used letter, and maxNumbers[0][3] is the stats for how often the letter is used. Deafults to False.
        - type (String) dictates which format the stats are returned in. Defaults to count
            Formats are
                - Percentage - The percentage of each letter relative to the overall ciphertext
                - Count (Default) - The count of each letter

    When stats = False, returns one list of the top {amount} most used letters in descending order. When stats = True, returns a dictionary of two lists, the first list being the stats of the top {amount} used letters plus the list already explained

    """

    if type not in ['count', 'percentage']:
        raise Exception("The type of stats you passed is not recognized. Try not passing a type or using 'count' or 'percentage'") 

    ciphertext = encrypt(plaintext, passphrase)
    wefwe = frequencyAnalysis(ciphertext, type)

    letter = wefwe[0]
    frequency = wefwe[1]

    max_letters=[]
    max_frequencies=[]

    k=0
    while k<amount:
        ma=(max(frequency))
        max_frequencies.append(ma)
        inde=frequency.index(ma)

        letter.pop(inde)
        frequency.pop(inde)

        check=(letter[inde])
        #print(check)
        max_letters.append(decrypt(check, passphrase))

        k+=1

    if stats:
        return(max_frequencies, max_letters)
    return(max_letters)


