# 0^i 1^j for some non-negative x, y such that x + y = i and 4x + 3y = j
from nltk import CFG

cfg_L2 = CFG.fromstring("""
    S -> X
    X -> '0' X '1' '1' '1' '1' | Y
    Y -> '0' Y '1' '1' '1' | 'eps'
""")

print(cfg_L2)