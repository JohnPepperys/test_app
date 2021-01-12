# --------------------------- caesar.py -------------------------------------
# ---- Oleg T-------------
# ---- 17 12 2020 --------
# ---- Learing project ---

digit = list(range(10))
ll = list(range(26))
for i in range(26):
    ll[i] = chr(ord('a') + i)

rusll = list(range(32))
for i in range(32):
    rusll[i] = chr(ord('а') + i)

# nt(digit, ll, lu, rusll, ruslu)

    # -------------------------------- Block insert data ----------------------------------------
phrase = input('Enter phrase: ')

enc = 0                                         # - enc = 0 - encrypt       enc = 1: decrypt
while 2 > 0:
    ss = input('Encrypt or Decrypt (e/d): ')
    if ss.lower() == 'e':
        break
    elif ss.lower() == 'd':
        enc = 1
        break

while 2 > 0:
    ron = int(input('Input encrypt|decrypt offset: (english 1...25, rus 1...31): '))
    if ron >= 1:
        break

    # ------------------------------ FUNCTION BLOCK --------------------------------------------------

def my_caesar_func(phr, enc, ron):
    global ll
    global rusll
    
    phr = phr.lower()
    if enc == 0:                                        # encrypt phrase
        if ord(ll[0]) <= ord(phr) <= ord(ll[-1]):
        # work with english
            t = ll.index(phr) + ron
            if t > 25:
                t -= 26
            return ll[t]
    
        else:
            # work with russia
            t = rusll.index(phr) + ron
            if t > 31:
                t -= 32
            return rusll[t]
    
    elif enc == 1:                                      # decrypt phrase
        if ord(ll[0]) <= ord(phr) <= ord(ll[-1]):
        # work with english
            t = ll.index(phr) - ron
            if t < 0:
                t += 26
            return ll[t]
    
        else:
            # work with russia
            t = rusll.index(phr) - ron
            if t < 0:
                t += 32
            return rusll[t]


    # ------------------------------- Work Block -------------------------------------------------------

ss = phrase.split()
for jj in range(len(ss)):
    ttm = list(ss[jj])
    for i in range(len(ttm)):
        if ttm[i].isalpha():
            if ttm[i].isupper():
                ttm[i] = my_caesar_func(ttm[i], enc, len(ss[jj]) - 1).upper()
            else:
                ttm[i] = my_caesar_func(ttm[i], enc, len(ss[jj]) - 1)

    print(*ttm, sep='', end=' ')


#for jj in range(26):
#    ttm = list(phrase)
#    #print(ttm, len(ttm))
#    for i in range(len(ttm)):
#        if ttm[i].isalpha():
#            if ttm[i].isupper():
#                ttm[i] = my_caesar_func(ttm[i], enc, jj).upper()
#            else:
#                ttm[i] = my_caesar_func(ttm[i], enc, jj)

#   print(*ttm, sep='')