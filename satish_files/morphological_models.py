# Dictionary Lookup
morph_dict = {
    "children": "child",
    "mice": "mouse",
    "cars": "car"
}

word = input("Enter word: ")

# 1. Dictionary Model
if word in morph_dict:
    root = morph_dict[word]
    feature = "irregular (dictionary)"

# 2. Finite State (Rule-Based)
elif word.endswith("ing"):
    root = word[:-3]
    feature = "continuous"
elif word.endswith("ed"):
    root = word[:-2]
    feature = "past tense"
elif word.endswith("s"):
    root = word[:-1]
    feature = "plural"

# 3. Unification (Feature tagging)
else:
    root = word
    feature = "base form"

# Output
print("Word   :", word)
print("Root   :", root)
print("Feature:", feature)
