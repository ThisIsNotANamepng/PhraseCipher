# Phrase Cipher
Derived from the [Book Cipher](https://wikipedia.org/wiki/Book_cipher), the Phrase Cipher aims to be a reasonably secure cipher usable by humans in real time without the use of a computer. The cipher relies on human randomness and instance customization to create cryptographic strength.

In order to use the Phrase Cipher, you need a shared **key phrase**. To increase decryption time, memorization would be prefered. 

In this example, the key will be 

>O say can you see, by the dawn’s early light,
>What so proudly we hail’d at the twilight’s last gleaming,
>Whose broad stripes and bright stars through the perilous fight
>O’er the ramparts we watch’d were so gallantly streaming?

The ciphertext is stored in the form of w/ln w/ln w/ln where w = the index of a word in the key phrase and ln = the index in that word.

For example, the plaintext "Hello world" would be encrypted as
```
15/1 9/1 10/1 15/4 1/1 14/0 12/2 9/3 9/4 13/5
```
The vanilla cipher doesn't include spaces or punctuation, but that can be easily included in a custom cipher flavor. 

The letter index for each word starts at 1. In order to strengthen som custom implementations of the cipher, x/0 = x/1.

To increase randomness and try to mitigate [letter frequency attacks](https://en.wikipedia.org/wiki/Frequency_analysis), a user can use different instances of a letter in the text. For example, with the already established key phrase in this example, 15/1 20/3 10/1 10/0 1/1 (hello) = 11/2 14/2 9/4 10/0 12/2 (hello).

If a letter a user needs isn't in the key phrase, it's possible to leave the letter plain in the ciphertext. This will likely increase security, as including all letters in the english alphabet in the key phrase would likely decrease the available key phrases which are short enough to be memorable, and decrease the amount of key phrases for attackers to test. 

To further mitigate frequency attacks, leaving random letters plain in the ciphertext may make letter frequencies more unpredictable. For example, 
```
8/4 12/2 10/1 9/1 t 10/5 14/2 r
```
To increase security, i's possible to use plain letters left in the ciphertext as it's own cipher or messages. There is no limit to how to implement this, but these are a few exemples:
- Link each plain letter to another letter. For example, agree every plain "r" in a ciphertext actually means "e". Or increase the index for which letter the plain letter represents for each apperance. For example, in ```x/y q x/y r x/y r```, the q=t, the first r=b, and the seconds r=c
- Use the position of the letter in the ciphertext and the number that thye letter represents. For example, in ```x/y x/y x/y f x/y x/y```, f=4(the index of the letter in the ciphertext)/6(the index of f in the english alphabet). This example is limited by the lenght of most english words, as you can't use "w(=22)" in most english words, as most english words aren't 22 characters long.
- Use a plain letter to dictate which key phrase to use. For example, a=The Declaration of Independence, b=The Geneva Convention, c=The King Jame's Bible, d=Chapter 26 of *Inheritance* by Christopher Paolini, e=Twinkle Twinkle Little Star
- Agree to ignore all plain letters
- Agree that the first letter dictates which one of these examples are used

As long as all parties agree on what rules to use, the Phrase Cipher can be as simple or as complicated as the user needs it to be. There is no limit to how much it can be modified or what rules can be applied as long as the usung parties can keep track of the changes.

## Strengths

The true strength of the Library Cipher lies in two unique factors which differentiate it from almost every other cipher. 

### Limitless Parametrization

The vanilla Library Cipher, is a straightforward encryption method that aims to be understood by anybody. One of the advantages of being so simple is its adaptability. By adhering to uncomplicated procedures, the Cipher can be easily modified, ensuring that only individuals privy to the newly established standard can decipher data encrypted with it. Unlike relying on security through obscurity, this cipher functions more like employing a secondary key to specify the rules for encoding and decoding data. In order to defeat computers with only the resources of the human mind, creativity is key. 

### Human Randomness

There is little academic research done on how well humans can generate randomness, but it is widely accepted that humans cannot reliably generate truly random data. In theory, the unique strewn randomness of the Library Cipher may make it more secure, making the more randomness unpredictable. In order to understand the effectiveness of human vs. computer generated randomness in the context of this cipher, I will be conducting a study which investigates how humans using the vanilla cipher choose. 

## Ongoing Research

I'm continuing to research how strong the Library Cipher is and how to make it stronger, the current research is located [here](OnGoingResearch.md).