# ---------- file:      find_points.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      25/01/2021

# ---------------------------------------------------------------------------------------------------------
import random
import time

# ---------------------------------------------------------------------------------------------------------

def object_sort(s, s1):
    newlist = []    
    nl1 = []
    lenstr = len(s)
    part1 = s[:lenstr // 2]
    part2 = s[lenstr // 2:]
    part11 = s1[:lenstr // 2]
    part22 = s1[lenstr // 2:]    
    len1 = len(part1)
    len2 = len(part2)
    if len1 > 1:
        part1, part11 = object_sort(part1, part11)
    if len2 > 1:
        part2, part22 = object_sort(part2, part22)

    i = 0
    j = 0
    while 1 < 10:
        if part1[i] <= part2[j]:
            newlist.append(part1[i])
            nl1.append(part11[i])
            i += 1
        else:
            newlist.append(part2[j])
            nl1.append(part22[j])
            j += 1

        if i == len1:
            newlist += part2[j:]
            nl1 += part22[j:]            
            break
        if j == len2:
            newlist += part1[i:]
            nl1 += part11[i:]
            break

    return newlist, nl1    

# ---------------------------------------------------------------------------------------------------------


def myBinFind_up(mass, x):
    print('start', x, mass)
    if mass[0] > x:
        return -1
    if mass[-1] < x:
        return len(mass) - 1

    l = -1
    r = len(mass)
    while (r - l) != 1:
        # print('!!!', x, l, r, mass)
        n = l + ((r - l) // 2)
        if mass[n] < x:
            l = n
        elif mass[n] >= x:
            r = n
    if mass[r] > x:
        return l
    else:
        return r 

def myBinFind_down(mass, x):
    print('start', x, mass)
    if mass[0] > x:
        return -1
    if mass[-1] < x:
        return len(mass) - 1

    l = -1
    r = len(mass)
    while (r - l) != 1:
        # print('!!!', x, l, r, mass)
        n = l + ((r - l) // 2)
        if mass[n] <= x:
            l = n
        elif mass[n] > x:
            r = n
    if mass[r] > x:
        return l
    else:
        return r 


# ---------------------------------------------------------------------------------------------------------

def lets_find_Points(sb, se, point):
    newsb, newse = object_sort(sb, se)
    print(newsb, newse)
    pointsadd = []

    for i in range(len(point)):
        # return index in list, were all elem left index are small, and right more X
        pointsadd.append((myBinFind_up(newsb, point[i]) + 1) - myBinFind_down(newse, point[i]) - 1)
        

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
    Mpoint = []
    for i in range(M):
        Mpoint.append(int(s[i]))

    
    #n = 15000
    #s = []
    #for i in range(n):
    #    s.append(random.randrange(1000))

    print(N, M, sb, se, Mpoint)

    # ---------- work block -----------------------------
    start = time.time()

    ph = lets_find_Points(sb, se, Mpoint)

    end = time.time()    
    # ------------- output block --------------------------
    print(ph)
    print('Worktime for', M, 'items: ', end - start)


# ------------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------
if __name__ == "__main__":
    main()