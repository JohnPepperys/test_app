# --------------- algoritm otrezki 2 ------------------------------
# ---- data:    10/01/2021
# ---- author:  O.Trushman
#

# ------------------ bubles sort algoritm -----------------------------

def bubles_sort(s1, s2, s3):
    lenstr = len(s)
    
    for i in range(lenstr):
        tmp = min(s1[i:])
        tmpindex = s1[i:].index(tmp)
        #print(i, tmp, tmpindex, s[i:])

        for j in range(tmpindex + i, 0, -1):
            if s1[j] < s1[j-1]:
                s1[j], s1[j-1] = s1[j-1], s1[j]
                s2[j], s2[j-1] = s2[j-1], s2[j]
                s3[j], s3[j-1] = s3[j-1], s3[j]

        #print(i, tmp, tmpindex, tmplist, newlist)
    return s1, s2, s3

# // --------------------------------------------------------------------------------------------------

def my_sort_otrezok(s):
    slen = []
    sl = []
    sr = []
    lenlist = len(s)
    print(lenlist, s)   
    
    for i in range(lenlist):
        tmp = s[i]
        slen.append(tmp[2])
        sl.append(tmp[0])
        sr.append(tmp[1])
    slen, sl, sr = bubles_sort(slen, sl, sr)

    print(lenlist, s)   

    return s


# // --------------------------------------------------------------------------------------------------


def find_points(s):
    slen = len(s)
    sl = []
    sr = []
    point = []
    for i in range(slen):
        tmp = s[i]
        sl.append(tmp[0])
        sr.append(tmp[1])

    while len(sl) != 0:
        #point1 = sr[0]
        #point1 = sl[0]
        point1 = min(sr)
        k = -1
        j = 0
        while j < slen:
            if sl[j] <= point1 and point1 <= sr[j]:
                # print(point1, j, sl[j], sr[j])
                s.pop(j)
                sl.pop(j)
                sr.pop(j)
                k = point1
                slen -= 1
                j -= 1
            j += 1

        if k != -1:
            point.append(k)

    return point

# // ---------------------------------------------- MAIN ----------------------------------------------------
# // ---------------------------------------------------------------------- MAIN ----------------------------


n = int(input())
s = [0 for i in range(n)]
# sl = [0 for i in range(n)]
# sr = [0 for i in range(n)]


for i in range(n):
    lit = input().split(' ')
    lit[0] = int(lit[0])
    lit[1] = int(lit[1])
    lit.append(lit[1] - lit[0])
    s[i] = lit

#print(s)
#s = my_sort_otrezok(s)
print(s)
itog = find_points(s)
print(len(itog))
for i in range(len(itog)):
    print(itog[i], end=' ')



# // --------------------------------------------------------------------------------------------------
