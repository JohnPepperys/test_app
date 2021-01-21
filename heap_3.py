# ---------- file:      heap_3.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      21/01/2021



# ---------------------------------------------------------------------------------------------------------

def my_Check_Last_Element_in_Heap(heap, nowpos):
    heapsize = len(heap)
    i = nowpos
    while i != 0:
        if heap[i] > heap[(i - 1) // 2]:
            heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        else:
            break
        i = (i - 1) // 2

    if heap[0] < heap[1]:
        heap[0], heap[1] = heap[1], heap[0]
    elif heapsize > 2 and heap[0] < heap[2]:
        heap[0], heap[2] = heap[2], heap[0]



def q_insert(heap, num):
    # there are no elements in heap
    if len(heap) == 0:
        heap.append(num)

    # we have one or more element in heap
    else:
        heap.append(num)
        qq = len(heap)
        my_Check_Last_Element_in_Heap(heap, qq - 1)




def q_extract_max(heap):
    maxval = heap[0]
    heap[0] = -1
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop(-1)
    heapsize = len(heap)
    i = 0
    while i < heapsize:
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

    return maxval

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
