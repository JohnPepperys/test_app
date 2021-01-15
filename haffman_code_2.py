# --- File:         haffman_code_2.py
# --- Project:      algoritm cource in Stepik.org
# --- Author:       O.Trushman
# --- Data:         15/01/2021

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

def create_tree(sym, symcount):
    tempsym = sym
    tempsymcount = symcount
    code = {}

    while len(tempsym) > 0:

        # --  find first min element and delete it
        if len(tempsymcount) >= 1:
            tmp1 = min(tempsymcount)
            tmp1index = tempsymcount.index(tmp1)
            elem1 = tempsym[tmp1index]
            elemcount1 = tmp1
            tempsym.pop(tmp1index)
            tempsymcount.pop(tmp1index)
            for j in range(len(elem1)):
                if elem1[j] in code.keys():
                    code[elem1[j]] = '0' + code[elem1[j]]
                else:
                    code[elem1[j]] = '0'
        else:
            break

        # -- find second min element and delete it
        if len(tempsymcount) >= 1:
            tmp2 = min(tempsymcount)
            tmp2index = tempsymcount.index(tmp2)
            elem2 = tempsym[tmp2index]
            elemcount2 = tmp2
            tempsym.pop(tmp2index)
            tempsymcount.pop(tmp2index)
            for j in range(len(elem2)):
                if elem2[j] in code.keys():
                    code[elem2[j]] = '1' + code[elem2[j]]
                else:
                    code[elem2[j]] = '1'
        else:
            break

        # --- append new element
        if len(tempsym) != 0:
            tempsym.append(elem1 + elem2)
            tempsymcount.append(elemcount1 + elemcount2)
        else:
            break
        #print(elem1, elemcount1, elem2, elemcount2, len(tempsymcount))
    return code


# -------------------------------------------------------------------------------------------------

def encode_string(s, code):
    news = ''
    for i in range(len(s)):
        news += code[s[i]]

    return news

# ------------------------------- MAIN ------------------------------------------------------------
# ------------------------------- MAIN ------------------------------------------------------------

instring = input()
instringlen = len(instring)

sym = []
symcount = []

for i in range(instringlen):
    if instring[i] in sym:
        ind = sym.index(instring[i])
        symcount[ind] += 1
    else:
        sym.append(instring[i])
        symcount.append(1)

symcount, sym = my_bubles_sort(symcount, sym)
code = create_tree(sym, symcount)

print(sym)
print(symcount)
print(code)

newstring = encode_string(instring, code)
print(instring, ':', newstring, len(newstring))


