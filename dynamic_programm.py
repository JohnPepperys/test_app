import sys

# ---------------------------------------------------------------------------------------------- #


def vych_max( mas, dl ):
    itog = 0
    #print(mas)
    n = len(mas)
    k = mas[-1]

    temp_dl = [0 for _ in range(n)]
    flag = False
    #print(temp_dl)
    for i in range(n-2, -1, -1):
        if k % mas[i] == 0:
            temp_dl[i] = dl[i]
            flag = True

    if flag:
        max_ind = temp_dl.index(max(temp_dl))
        itog = dl[max_ind] + 1
    #print(temp_dl)
    return itog



# ---------------------------------------------------------------------------------------------- #

def reccurent_function( mass ):
    print(mass)
    dl = []
    dl.append(0)
    n = len(mass)
    for i in range(1, n):
        dl.append( vych_max(mass[:i+1], dl) )
    print(dl)
    return max(dl) + 1

def main():
    #print('script start')

    # -------------------- input block ------------------------
    n = int(input())
    mass = list(map( int, input().split() ))

    maxk = reccurent_function(mass)
    # ------------------- output block ------------------------
    print(maxk)

    # ------------ end of function MAIN -----------------------------

if __name__ == "__main__":
    main()
    
    
