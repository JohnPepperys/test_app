# ---------- file:      find_points.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      26/01/2021

# ---------------------------------------------------------------------------------------------------------
import time

# ---------------------------------------------------------------------------------------------------------
def object_sort(s):
    newlist = []
    lenstr = len(s)
    part1 = s[:lenstr // 2]
    part2 = s[lenstr // 2:]
    len1 = len(part1)
    len2 = len(part2)
    print('Object sort: ', part1, len1, part2, len2)

    if len1 > 1:
        part1 = object_sort(part1)
    if len2 > 1:
        part2 = object_sort(part2)

    if len1 == 1 and len2 == 1:
        if part1[0] <= part2[0]:
            return part1 + part2
        else:
            return part2 + part1

    i = 0
    j = 0
    while 1 < 10:
        if part1[i] <= part2[j]:
            newlist.append(part1[i])
            i += 1
        else:
            newlist.append(part2[j])
            j += 1

        if i == len1:
            newlist += part2[j:]
            break
        if j == len2:
            newlist += part1[i:]
            break
    
    #print('End!!!: ', part1, part2, ' -> ', newlist)
    return newlist


# ---------------------------------------------------------------------------------------------------------


def myBinFind_up(mass, x):
    masslen = len(mass)
    if mass[0] > x:
        return 0
    if x >= mass[-1]:
        return masslen

    l = 0
    r = masslen

    while (r - l) != 1:
        n = (r - l) // 2
        n = l + n
        if x >= mass[n]:
            l = n
        else:
            r = n
    return r


def myBinFind_down(mass, x):
    masslen = len(mass)
    if x <= mass[0]:
        return 0
    if mass[-1] < x:
        return masslen

    l = 0
    r = masslen
    while (r - l) != 1:
        n = (r - l) // 2
        n = l + n
        if x <= mass[n]:
            r = n
        else:
            l = n
    return r

# ---------------------------------------------------------------------------------------------------------


def lets_find_Points(sb, se, point):
    if len(sb) > 1:
        newsb = object_sort(sb)
        newse = object_sort(se)
    else:
        newsb = sb
        newse = se
    print(newsb, newse)
    pointsadd = []

    for i in range(len(point)):
        # return index in list, were all elem left index are small, and right more X
        q = myBinFind_up(newsb, point[i])
        w = myBinFind_down(newse, point[i])
    #    print('start, finish: ', point[i], q, w)
        pointsadd.append(q - w)

    return pointsadd


# ------------------------------ MAIN PART ----------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------

def main():
    print('Binary Find Start!!!')

    # ---------- input block ----------------------------
    s = input().split(' ')
    N = int(s[0])
    M = int(s[1])
    sb = []
    se = []

    for i in range(N):
        s = input().split(' ')
        sb.append(int(s[0]))
        se.append(int(s[1]))

    s = input().split(' ')
    if M != 0:
        Mpoint = []
        for i in range(M):
            Mpoint.append(int(s[i]))

    print(N, M, sb, se, Mpoint)

    # ---------- work block -----------------------------
    start = time.time()
    if N == 0:
        for i in range(M):
            print(0, end = ' ')
    else:
        ph = lets_find_Points(sb, se, Mpoint)
        for i in range(len(ph)):
            print(ph[i], end=' ')

    end = time.time()
    # ------------- output block --------------------------

    print('Worktime for', M, 'items: ', end - start)


# ------------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
