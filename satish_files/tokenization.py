text = "Natural Language Processing is interesting"
tokens = []
word = ""
for ch in text:
    if ch != " ":
        word += ch
    else:
        tokens.append(word)
        word = ""
tokens.append(word)

print("Original Text:", text)
print("Tokens:", tokens)
