# ---------- file:      find_inversion_2.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      24/01/2021

# ---------------------------------------------------------------------------------------------------------
import random
import time

invers = 0


def object_sort(s):
    global invers
    newlist = []
    
    lenstr = len(s)
    part1 = s[:lenstr // 2]
    part2 = s[lenstr // 2:]    
    len1 = len(part1)
    len2 = len(part2)
    #print('!!!', part1, len1, part2, len2)
    if len1 > 1:
        part1 = object_sort(part1)
    if len2 > 1:
        part2 = object_sort(part2)

    i = 0
    j = 0
    # print('!!!', part1, len1, part2, len2)
    while 1 < 10:
         
        if part1[i] <= part2[j]:
            newlist.append(part1[i])
            i += 1
        else:
            invers += len1 - i
            print("!!!", part1, part2, i, j)
            newlist.append(part2[j])
            j += 1

        if i == len1:
            newlist += part2[j:]            
            break
        if j == len2:
            newlist += part1[i:]
            break

    return newlist    
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



# ------------------------------ MAIN PART ----------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------

def main():
    print('Binary Find Start!!!')

    # ---------- input block ----------------------------

    n = int(input())
    s = input().split(' ')
    for i in range(n):
        s[i] = int(s[i])
    #n = 15000
    #s = []
    #for i in range(n):
    #    s.append(random.randrange(1000))

    print(s)

    # ---------- work block -----------------------------
    start = time.time()

    #invers = myFindInversion(s)
    s = object_sort(s)
    print(s)

    end = time.time()    
    # ------------- output block --------------------------
    print(invers)
    print('Worktime for', n, 'items: ', end - start)


# ------------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------
if __name__ == "__main__":
    main()