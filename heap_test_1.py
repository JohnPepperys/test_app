# ---------- file:      heap_test_1.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      18/01/2021

# ---------------------------------------------------------------------------------------------------------

T = []
heap = []

def t_insert(x):
    T.append(x)

def t_extract_max():
    m = 0
    for i in range(1, len(T)):
        if T[i] > T[m]:
            m = i
    result = T[m]
    del T[m]
    return result

# --------------------------------------------------------------------------------------------------
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


def q_insert(num):
    global heap

    # there are no elements in heap
    if len(heap) == 0:
        heap.append(num)

    # we have one or more element in heap
    else:
        heap.append(num)
        qq = len(heap)
        my_Check_Last_Element_in_Heap(qq - 1)

def q_extract_max():
    maxval = heap[0]
    heap[0] = -1
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop(-1)
    heapsize = len(heap)
    i = 0
    while i < heapsize:
        # print(i, heapsize, heap)
        if heapsize > (2 * i + 2):          
            if heap[2 * i + 1] > heap[2 * i + 2]:
                if heap[i] < heap[2 * i + 1]:
                    heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                    i = i * 2 + 1
                else:
                    break
            else:
                if heap[i] < heap[2 * i + 2]:
                    heap[i], heap[2 * i + 2] = heap[2 * i + 2], heap[i]
                    i = i * 2 + 2
                else:
                    break

        elif heapsize > (2 * i + 1):
            if heap[i] < heap[2 * i + 1]:
                heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
            i = i * 2 + 1
            break
        else:
            break

    # print(maxval, heap)
    return maxval



# --------------------------------------------------------------------------------------------------
n = 10000
for i in range(n, 0, -1):
    q_insert(i)
    t_insert(i)

print('T: ', T)
print('Heap: ', heap)

for i in range(n):
    a = q_extract_max()
    b = t_extract_max()
    if a == b:
        print(i, a, heap)
    else:
        print(i, a, b, heap, "ERROR")
        break

