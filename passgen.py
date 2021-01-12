# ------------ pass generator ----------------------
import random

# ---------- initialize data -----------------------------------------------------------------------
digit = list(range(10))
ll = list(range(26))
lu = list(range(26))
for i in range(26):
    ll[i] = chr(ord('a') + i)
    lu[i] = chr(ord('A') + i)
punc = ['!', '#', '$', '%', '&', '*', '+', '-', '=', '@', '^', '_', '(', ')', '<', '>']
use_digit = True
use_lowlet = True
use_uplet = True
use_punc = True

# --------------------------  work function -------------------------------------------------------------
def my_gen_one_pass():
    global digit
    global ll
    global lu
    global punc
    global nlen
    s = ''
    while len(s) < nlen:
        t = random.randint(1,4)
        if t == 1 and use_digit:
            s += str(digit[random.randint(0, len(digit) - 1)])
        elif t == 2 and use_lowlet:
            s += ll[random.randint(0, len(ll) - 1)]
        elif t == 3 and use_uplet:
            s += lu[random.randint(0, len(lu) - 1)]
        elif t == 4 and use_punc:
            s += punc[random.randint(0, len(punc) - 1)]
    return s



def my_check_one_pass(pas):
    global digit
    global ll
    global lu
    global punc
    global nlen

    cd, cll, clu, cp = 0, 0, 0, 0
    count = 4
    for j in range(len(pas)):
        if pas[j].isdigit():
            for i in range(len(digit)):
                if pas[j] == str(digit[i]):
                    cd += 1
                    break
          
        elif pas[j].isalpha():
            if pas[j].islower():
                for i in range(len(ll)):
                    if pas[j] == ll[i]:
                        cll += 1
                        break
                
            else:
                for i in range(len(lu)):
                    if pas[j] == lu[i]:
                        clu += 1
                        break
        else:
            for i in range(len(punc)):
                if pas[j] == punc[i]:
                    cp += 1
                    break

    # tt = len(pas) // 4
    if use_digit:
        if cd >= 1:
            count -= 1
    else:
        count -= 1
    if use_lowlet:
        if cll >= 1:
            count -= 1
    else:
        count -= 1
    if use_uplet:
        if clu >= 1:
            count -= 1
    else:
        count -= 1
    if use_punc:
        if cp >= 1:
            count -= 1
    else:
        count -= 1
    
    if count == 0:
        return True
    else:
        return False



def my_gen_one_password():
    while 2 > 1:
        tmp = my_gen_one_pass()
        if my_check_one_pass(tmp):
            return tmp
    

    # -------------------------------------------------------------------------------


def check_password(passlist, onepassword):
    for c in passlist:
        if onepassword == c:
            return False
    return True



# ------------------------------ main code --------------------------------------------------------------

while 2 > 0:
    nlen = int(input('Enter please length of password (need be 6 or more): '))
    if nlen >= 6:
        break

while 2 > 0:
    ncol = int(input('Enter please number of passwords (need be 1 or more): '))
    if ncol >= 1:
        break

while 2 > 0:
    ss = input('Use digit [0...9] in passwords (y/n): ')
    if ss.lower() == 'y':
        break
    elif ss.lower() == 'n':
        use_digit = False
        break
    
while 2 > 0:
    ss = input('Use lower letters [a...z] in passwords (y/n): ')
    if ss.lower() == 'y':
        break
    elif ss.lower() == 'n':
        use_lowlet = False
        break
    
while 2 > 0:
    ss = input('Use upper letters [A...Z] in passwords (y/n): ')
    if ss.lower() == 'y':
        break
    elif ss.lower() == 'n':
        use_uplet = False
        break

while 2 > 0:
    ss = input('Use symbols [!@#$%^&*()-_=+<>,.] in passwords (y/n): ')
    if ss.lower() == 'y':
        break
    elif ss.lower() == 'n':
        use_punc = False
        break

while 2 > 0:
    ss = input('Exclude some-writing symbol [il1Io0O] from passwords (y/n): ')
    if ss.lower() == 'y':
        digit.remove(1)
        digit.remove(0)
        ll.remove('o')
        ll.remove('i')
        ll.remove('l')
        lu.remove('I')
        break
    elif ss.lower() == 'n':
        break

password_res = []
for i in range(ncol):
    while 2 > 0:
        tmp = my_gen_one_password()
        if check_password(password_res, tmp):
            password_res.append(tmp)
            break

print(*password_res, sep='\n')
