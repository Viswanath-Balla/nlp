import nltk
from nltk import CFG
from nltk.parse import ChartParser


grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'The' | 'an'
N -> 'boy' | 'apple'
V -> 'eats'
""")

parser = ChartParser(grammar)

sentence = "The boy eats an apple".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
