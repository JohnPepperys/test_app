# --------------- Haffmann code 1 ------------------------------
# ---- File:    haffman_code_1.py
# ---- data:    12/01/2021
# ---- author:  O.Trushman
#


def my_bubles_sort(s1, s2):
    lenstr = len(s1)

    for i in range(lenstr):
        tmp = max(s1[i:])
        tmpindex = s1[i:].index(tmp)

        for j in range(tmpindex + i, 0, -1):
            if s1[j] > s1[j - 1]:
                s1[j], s1[j - 1] = s1[j - 1], s1[j]
                s2[j], s2[j - 1] = s2[j - 1], s2[j]
                # s3[j], s3[j - 1] = s3[j - 1], s3[j]
    return s1, s2


# -------------------------------------------------------------------------------------------------

def my_code_haffman(string, symlist, codelist):
    newstring = ''
    for i in range(len(string)):
        newstring += code[symlist.index(string[i])]
    return newstring


# ------------------------------- MAIN ------------------------------------------------------------
# ------------------------------- MAIN ------------------------------------------------------------

instring = input()
instringlen = len(instring)

sym = []
symcount = []
code = []

for i in range(instringlen):
    if instring[i] in sym:
        ind = sym.index(instring[i])
        symcount[ind] += 1
    else:
        sym.append(instring[i])
        symcount.append(1)

symcount, sym = my_bubles_sort(symcount, sym)

if len(sym) < 2:
    code.append('0')
else:
    for i in range(len(sym) - 1):
        code.append('1' * i + '0')
    code.append('1' * (len(sym) - 1))

ns = my_code_haffman(instring, sym, code)
print(len(sym), len(ns))

for i in range(len(sym)):
    print(sym[i], ": ", code[i], sep='')

print(ns)
