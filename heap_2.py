# ---------- file:      heap_2.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      17/01/2021

# ---------------------------------------------------------------------------------------------------------

def my_Check_Last_Element_in_Heap(nowpos):
    global heap
    heapsize = len(heap)
    i = nowpos
    while i != 0:
        if heap[i] > heap[(i - 1) // 2]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        else:
            break
        i = i // 2

        # print(i, heap)
    if heap[0] < heap[1]:
        heap[0], heap[1] = heap[1], heap[0]
    elif heapsize > 2 and heap[0] < heap[2]:
        heap[0], heap[2] = heap[2], heap[0]




# ---------------------------------------------------------------------------------------------------------

def my_Insert_Heap(num):
    global heap

    # there are no elements in heap
    if len(heap) == 0:
        heap.append(num)

    # we have one or more element in heap
    else:
        heap.append(num)
        qq = len(heap)
        my_Check_Last_Element_in_Heap(qq - 1)

    print(heap)

# ---------------------------------------------------------------------------------------------------------


def my_ExtractMax_Heap():
    maxval = heap[0]
    heap[0] = -1
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop(-1)
    heapsize = len(heap)
    i = 0
    while i < heapsize:
        # print(i, heapsize, heap)
        if heapsize > (2 * i + 2):
            if heap[i + 1] > heap[i + 2]:
                heap[i], heap[i+1] = heap[i+1], heap[0]
                i = i * 2 + 1
            else:
                heap[i], heap[i + 2] = heap[i + 2], heap[0]
                i = i * 2 + 2
        elif heapsize > (2 * i + 1):
            heap[i], heap[i + 1] = heap[i + 1], heap[0]
            i = i * 2 + 1
            break
        else:
            break

    print(heap)
    return maxval

# ----------------- MAIN ---------------------------------------------------------
# -------------------------------- MAIN ------------------------------------------
heap = []
extract = []

n = int(input())
for i in range(n):
    s = input()
    if 'Insert ' in s:
        tmp = s.split(' ')
        my_Insert_Heap(int(tmp[1]))

    if 'ExtractMax' in s:
        extract.append(my_ExtractMax_Heap())

for i in range(len(extract)):
    print(extract[i])