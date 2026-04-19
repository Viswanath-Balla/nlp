def stem(word):
  
    if word.endswith("sses"):
        word = word[:-2]
    elif word.endswith("ies"):
        word = word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        word = word[:-1]

  
    if word.endswith("ing"):
        word = word[:-3]
    elif word.endswith("ed"):
        word = word[:-2]


    if word.endswith("ational"):
        word = word[:-7] + "ate"
    elif word.endswith("tional"):
        word = word[:-6] + "tion"

 
    if word.endswith("e"):
        word = word[:-1]

    return word



words = ["playing", "connected", "relational", "studies"]
word = input("Enter a word: ")
print(word, "->", stem(word))

for w in words:
    print(w, "->", stem(w))
