import random
import time


def reccurent_function2(mass):
    n = len(mass)
    inf = max(mass) + 1
    L = [inf] + [-inf] * (n+1)
    Lpos = [-inf] *(n+2)
    Prev = [-2] * n

    for i in range(n):
        left = 0
        right = n+1
        while left+1 < right:
            midd = (left+right) // 2
            if L[midd] >= mass[i]:
                left = midd
            else:
                right = midd

        L[right] = mass[i]
        Lpos[right] = i
        Prev[i] = Lpos[right-1]

    #print('L:', L)
    #print('Lpos:', Lpos)
    #print('Prev:', Prev)

    j = n+1
    while L[j] == -inf:
        j -= 1
    return [j, Lpos[j]] + Prev

# -----------------------------------------------------------------------------------------------


def print_need_data(mass_retr):
    allelem = mass_retr[0]
    startel = mass_retr[1]
    count = 0
    arr = [0] * allelem

    while startel >= 0:
        arr[count] = startel + 1
        count += 1
        startel = mass_retr[startel+2]

    print(allelem)
    for i in range(count-1, -1, -1):
        print(arr[i], end=' ')
    


# ----------------------------------------------------------------------------------------------- 
# ----------------------------------------------------------------------------------------------- 
def main():
    #n = int(input())
    #mass = list(map(int, input().split()))
    n = 200000
    mass = [random.randint(1,1000) for i in range(n)]
    #print(mass)
    start = time.time()
    maxk = reccurent_function2(mass)
    print_need_data(maxk)
    end = time.time()

    print()
    print('Worktime:', end - start)

if __name__ == "__main__":
    main()