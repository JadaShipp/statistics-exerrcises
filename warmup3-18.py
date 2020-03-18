import pandas as pd
with open('/usr/share/dict/words') as f:
    words = f.read().split()
    
words[:10]
pd.Series(words)
pd.DataFrame({'word': words})
df = pd.DataFrame({'word': words})
df.word

def alphabetical_value(ch: str) -> int:
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) + 1

def whole_word_value(word: str) -> int:
     return sum([alphabetical_value(ch) for ch in word])

def triangle_number_formula(n: int):
    return (n*(n+1))/2


def is_triangle_number(x):
    if x == 



