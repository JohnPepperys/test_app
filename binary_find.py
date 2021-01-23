# ---------- file:      start.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      22/01/2021

# ---------------------------------------------------------------------------------------------------------




def myBinFind(mass, x):

    l = -1
    r = len(mass)
    while (r - l) != 1:
        n = l + ((r - l) // 2)
        if mass[n] == x:
            return n + 1
        elif mass[n] < x:
            l = n
        elif mass[n] > x:
            r = n
    return -1


# ------------------------------ MAIN PART ----------------------------------------------------------------------
# ------------------------------ MAIN PART ----------------------------------------------------------------------

def main():
    print('Binary Find Start!!!')

    # ---------- input block ----------------------------
    s1 = input()
    Mass = s1.split(' ')
    masslen = int(Mass[0])
    Mass = Mass[1:]
    for i in range(masslen):
        Mass[i] = int(Mass[i])
    
    s1 = input()
    Elem = s1.split(' ')
    elemlen = int(Elem[0])
    Elem = Elem[1:]
    for i in range(elemlen):
        Elem[i] = int(Elem[i])

    print(masslen, Mass)
    print(elemlen, Elem)

    # ---------- work block ------------------------------

    for i in range(elemlen):
        print(myBinFind(Mass, Elem[i]), end=' ')

# ------------------------------------------------------------------------

if __name__ == "__main__":
    main()