import cs50
import sys

# check if correct number of command line arguments were given
if len(sys.argv) != 2:
    print("Usage: python vigenere.py k")
    sys.exit(1)

key = sys.argv[1]

# check if key is alphabetical
if not key.isalpha():
    print("Usage: python vigenere.py k")
    sys.exit(1)

# get plaintext input from user
p = cs50.get_string("plaintext: ")

# translate key into list of numbers
k = []

for c in key:
    if c.islower():
        k.append(ord(c) - 97)
    elif c.isupper():
        k.append(ord(c) - 65)

# start output to user
print("ciphertext: ", end="")

# go through each character in plaintext, adding key to each char and printing result
j = 0
key_len = len(key)
for c in p:
    # j is used to cycle through the key
    j %= key_len

    # add k[j] to the numeric value of c, making sure to wrap around the alphabet. Print the result
    a = ord(c)
    if c.isupper():
        if a + k[j] > ord('Z'):
            a -= ord('Z') - ord('@')
        print(chr(a + k[j]), end="")
        j += 1
    elif c.islower():
        if a + k[j] > ord('z'):
            a -= ord('z') - ord('`')
        print(chr(a + k[j]), end="")
        j += 1
    else:
        print(c, end="")

# if we get here, all of the ciphertext is printed – print new line and exit
print()