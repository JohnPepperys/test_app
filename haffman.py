# ----------- Code Haffman 1 ----------------------------------------
# ---- data:    10/01/2021
# ---- author:  O.Trushman
#

# // ---------------------------------------------- MAIN ----------------------------------------------------
# // ---------------------------------------------------------------------- MAIN ----------------------------

instring = input()
instinglen = len(instring)

    # ------------- find Frequence for letters ---------------------------
s = []
counts = []
code = []
for i in range(instinglen):
    if instring[i] in s:
        fi = s.index(instring[i])
        counts[fi] += 1

    else:
        s.append(instring[i])
        counts.append(1)     
        code.append('')

print(s)
print(counts)

    # ---------- find Code for letters ----------------------------------
    minfreq = min(counts)
    indmf = counts.index(minfreq)
