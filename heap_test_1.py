# ---------- file:      heap_test_3.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      21/01/2021

# ---------------------------------------------------------------------------------------------------------
from heap_3 import q_insert, q_extract_max

H = []
extract = []

n = int(input())
for i in range(n):
    s = input()
    if 'Insert ' in s:
        tmp = s.split(' ')
        q_insert(H, int(tmp[1]))
        print(n, H)

    if 'ExtractMax' in s:
        extract.append(q_extract_max(H))

print('H: ', H)
for i in range(len(extract)):
    print(extract[i])
