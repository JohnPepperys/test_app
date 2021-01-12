# --------------- algoritm ryukzak 1 ------------------------------
# ---- data:    10/01/2021
# ---- author:  O.Trushman
#

def work_with_summ(vmax, s):
    
    vtemp = 0
    vost = vmax
    maxlen = len(s)
    sc = []
    svol = []
    sotn = []
    cost = 0
    for i in range(maxlen):
        tmp = s[i]
        sc.append(tmp[0])
        svol.append(tmp[1])
        sotn.append(tmp[2])

    while vost > 0 and len(sc) > 0:
        point = max(sotn)
        index = sotn.index(point)
        if vost >= svol[index]:
            vtemp += svol[index]
            vost -= svol[index]
            cost += sc[index]
            del sc[index]
            del svol[index]
            del sotn[index]

        else:
            cost += sc[index] / (svol[index] / vost)
            break

    return cost

# // ---------------------------------------------- MAIN ----------------------------------------------------
# // ---------------------------------------------------------------------- MAIN ----------------------------


lit = input().split(' ')
think = int(lit[0])
vmax = int(lit[1])

s = []
for i in range(think):
    lit = input().split(' ')
    lit[0] = int(lit[0])
    lit[1] = int(lit[1])
    lit.append(lit[0] / lit[1])
    s.append(lit)

res = str(work_with_summ(vmax, s)).split('.')
#print(res)
if len(res) < 2:
    print(res[0], '000', sep='.')
else:
    if len(res[1]) < 3:
        res[1] = res[1].ljust(3, '0')
    elif len(res[1]) > 3:
        res[1] = res[1][0:3] 

    print(res[0], res[1], sep='.')
#print(maxcost)

