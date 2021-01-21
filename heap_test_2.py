# ---------- file:      heap_test_2.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      21/01/2021

# ---------------------------------------------------------------------------------------------------------

import random
from heap_3 import q_insert, q_extract_max

def t_insert(x):
    T.append(x)

def t_extract_max():
    m = max(T)
    T.remove(m)
    return m


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------

for j in range(100):
    n = 10
    T = []
    Bigheap = []
    stop = False

    for i in range(n):
        k = random.randint(0, 100)
        q_insert(Bigheap, k)
        t_insert(k)

    print(j, 'T: ', T)
    print(j, 'Heap: ', Bigheap)

    for i in range(n):
        a = q_extract_max(Bigheap)
        b = t_extract_max()
        if a == b:
            print(i, a, Bigheap)
        else:
            print(i, a, b, Bigheap, "ERROR")
            stop = True
            break
    
    if stop:
        break

