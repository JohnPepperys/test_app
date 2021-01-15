# --- File:         haffman_decode_2.py
# --- Project:      algoritm cource in Stepik.org
# --- Author:       O.Trushman
# --- Data:         15/01/2021


def input_data():
    # first string:
    n = input()
    sn = n.split(' ')
    sn[0] = int(sn[0])
    sn[1] = int(sn[1])

    # next n string
    sinput = []
    code = {}
    for i in range(sn[0]):
        sinput.append(input())
    for i in range(sn[0]):
        tmp = sinput[i]
        code[tmp[0]] = tmp[3:]

    # last input - string
    inputstr = input()

    return inputstr, code


# -------------------------------------------------------------------------------------------------


def haffman_decode(s, code):
    tmp = s
    newstring = ''
    pp = []

    pp = list(code.keys())
    j = 0
    while len(tmp) > 0:
        tmp1 = tmp[:j + 1]
        j += 1
        for i in range(len(code)):
            if tmp1 == code[pp[i]]:
                newstring += pp[i]
                tmp = tmp[len(tmp1):]
                j = 0
                break

    return newstring


# ------------------------------- MAIN ------------------------------------------------------------
# ------------------------------- MAIN ------------------------------------------------------------

instr, code = input_data()
# print(instr, code)

newstring = haffman_decode(instr, code)
print(newstring)
