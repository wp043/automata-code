# complement of ww
from nltk import CFG

cfg_L3 = CFG.fromstring("""
    S -> A B | B A | A | B
    X -> '0' A '1' | '1' A '0' | '1' A '1' | '0' A '0' | '0'
    Y -> '0' B '1' | '1' B '0' | '1' B '1' | '0' B '0' | '1'
""")

print(cfg_L3)