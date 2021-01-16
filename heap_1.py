# ---------- file:      heap_1.py
# ---------- project:   test_algoritms
# ---------- author:    O.Trushman
# ---------- data:      16/01/2021

# ---------------------------------------------------------------------------------------------------------

def my_Check_Last_Element_in_Heap():
    global heap
    heapsize = len(heap)

    i = heapsize-1
    while i != 0:
        if heap[i] < heap[i // 2]:
            heap[i], heap[i // 2] = heap[i // 2], heap[i]
        else:
            return
        i = i // 2
    
    # 
    # print(i)
    if heap[0] > heap[1]:
        heap[0], heap[1] = heap[1], heap[0]
    elif heapsize > 2 and heap[0] > heap[2]:
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
        my_Check_Last_Element_in_Heap()

    print(heap)



# ---------------------------------------------------------------------------------------------------------


def my_ExtractMax_Heap():
    global heap
    return heap.pop(-1)



# ----------------- MAIN ---------------------------------------------------------
# -------------------------------- MAIN ------------------------------------------
heap = []
extract = []

n = int(input())
for i in range(n):
    s = input()
    if 'Insert ' in s:
        tmp = s.split(' ')
        my_Insert_Heap( int(tmp[1]) )

    if 'ExtractMax' in s:
        extract.append( my_ExtractMax_Heap() )

for i in range(len(extract)):
    print(extract[i])




# ------------- end of file heap_1.py ---------------------------------------------