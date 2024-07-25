# a^i b^j c^k d^l such that i = j or k = l but not both, ijkl all >= 0
from nltk import CFG

cfg_L1 = CFG.fromstring("""
    S -> A | B | C | D
    A -> 'a' A1 A2
    A1 -> 'a' A1 | 'a' A1 'b' | 'eps'
    A2 -> 'c' A2 'd' | 'eps'
    B -> B1 'b' A2
    B1 -> B1 'b' | 'a' B1 'b' | 'eps'
    C -> C1 'c' C2
    C1 -> 'a' C1 'b' | 'eps'
    C2 -> 'c' C2 | 'c' C2 'd' | 'eps'
    D -> C1 D1 'd'
    D1 -> D1 'd' | 'c' D1 'd' | 'eps'
""")

print(cfg_L1)
