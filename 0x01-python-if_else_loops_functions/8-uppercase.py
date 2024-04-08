#!/usr/bin/python3
#!/usr/bin/python3

def uppercase(word):
    for char in word:
        if not (ord('A') <= ord(char) <= ord('Z')):
            return False
    return True

word = input("Enter a word: ")
if uppercase(word):
    print("The word is all uppercase.")
else:
    print("The word contains non-uppercase characters.")

