def simple_wsd(sentence, target_word, knowledge_base):
    context = set(sentence.lower().split())
    
    best_sense = None
    max_overlap = 0

    for sense, definition in knowledge_base[target_word].items():
        signature = set(definition.lower().split())
        overlap = len(context.intersection(signature))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense


# Knowledge base (manual)
knowledge_base = {
    "bank": {
        "finance": "money deposit withdraw cash account",
        "river": "river water shore land edge"
    }
}

# Test
sentence = "I went to the bank to deposit money"
word = "bank"

sense = simple_wsd(sentence, word, knowledge_base)

print("Sentence:", sentence)
print("Predicted Sense:", sense)
