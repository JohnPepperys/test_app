# --------------------------- ugadayka.py -------------------------------------
# ---- Oleg T-------------
# ---- 19 12 2020 --------
# ---- Learing project ---

import os
import random
dictinary = []
open_symbol = []

def create_dictionary():
    global dictinary
    filehandle = open('wordbook.txt', encoding="utf-8")
    for line in filehandle:
        line = line.strip()
        line = line.lower()
        if line.isalpha() and line not in dictinary:
            dictinary.append(line)
    
    filehandle.close()
    # ------------ end of function create-dictionary() -------------------------

def get_random_word():
    global dictinary
    global open_symbol
    tmp = dictinary[random.randint(0, len(dictinary) - 1)]
    open_symbol = [0] * len(tmp)
    open_symbol[0], open_symbol[-1] = 1, 1
    return tmp
    # -------------- end of function   get random word() ----------------------------


def show_string_part(s, ll):
    for i in range(len(s)):
        if ll[i] == 1:
            print(s[i], ' ', sep='', end='')
        else:
            print('_ ', end='')



# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]



def my_main_play():
 
    input_letter = []
    
    password = get_random_word()
    print('Hello. We start play! Im guess a word: ', end='')
    show_string_part(password, open_symbol)
    tryes = 6
    
    while tryes != 0:
        while 2 > 0:
            s = input('Enter all word or one letter: ')
            if s in input_letter:
                print('You have already entered these characters.')
            elif s.isalpha() and len(s) >= 1:
                break
        s = s.lower()
        input_letter.append(s)

        if len(s) > 1:
            # enter word
            if s == password:
                print('Yeeeeeeeeeeeeeeeeees!!! You WIN!!!! Its write: ', s.upper())
                break
            else:
                print('Not guessed! ', end='')
                tryes -= 1
                print('You have left', tryes, 'attempts')
                print(display_hangman(tryes))
        else:
            # enter letter
            if s in password:
                for i in range(len(password)):
                    if s == password[i]:
                        open_symbol[i] = 1
                if 0 not in open_symbol:
                    print('Congratilation!!! You are guess word: ', password.upper(), '! You made ', 6 - tryes, ' attempts!', sep='')
                    break
                else:
                    print('Yeees. Letter: ', s, '.  Word now: ', end='')

            else:
                tryes -= 1
                print('No letter', s, 'in this word. You have', tryes, 'attempts.')
                print(display_hangman(tryes))

            show_string_part(password, open_symbol)
    print('Sorry. Did not guess. It was word: ', password.upper())            
                
        


    # -------------- end of function   my_main_play () ----------------------------

# ---------------------------- MAIN CODE ----------------------------------------------------------------------------
# ---------------------------- MAIN CODE ----------------------------------------------------------------------------

print(os.getcwd())
create_dictionary()

while 2 > 0:
    my_main_play()
    qq = input('New game? (Y/n): ').lower()
    if qq == 'n':
        break;

print('Good bye!!!')

