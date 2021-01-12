
import random
import time

# ------------------ bubles sort algoritm -----------------------------

def bubles_sort(s):
    lenstr = len(s)
    
    for i in range(lenstr):
        tmp = min(s[i:])
        tmpindex = s[i:].index(tmp)
        #print(i, tmp, tmpindex, s[i:])

        for j in range(tmpindex + i, 0, -1):
            if s[j] < s[j-1]:
                s[j], s[j-1] = s[j-1], s[j]

        #print(i, tmp, tmpindex, tmplist, newlist)
    return s



# ------------------- sorting by sliyanie -----------------------------

def object_sort(s):
    newlist = []
    
    lenstr = len(s)
    part1 = s[:lenstr // 2]
    part2 = s[lenstr // 2:]    
    len1 = len(part1)
    len2 = len(part2)
    #print(part1, len1, part2, len2)
    if len1 > 1:
        part1 = object_sort(part1)
    if len2 > 1:
        part2 = object_sort(part2)

    i = 0
    j = 0
    while 1 < 10:
        if part1[i] < part2[j]:
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
        
        #print(i, j, newlist)

    #print(part1, part2)
    return newlist


# // ----------------------------------------------------------------------------------------------------------------------



def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data



# // ----------------------------------------------------------------------------------------------------------------------
# // ----------------------------------------------------------------------------------------------------------------------

# ------------ main code ----------------------------------------------

#lstr = input().split(' ')
#for i in range(len(lstr)):
#    lstr[i] = int(lstr[i])

lstr = []
for i in range(int(input())):
    lstr.append(random.randrange(10000))

#print(lstr)
start = time.time()
#nwstr = bubles_sort(lstr)
nwstr = object_sort(lstr)
#nwstr = merge_sort(lstr)
end = time.time()
#print(nwstr)
print(nwstr[0], nwstr[-1])
print('Worktime:', end - start)
