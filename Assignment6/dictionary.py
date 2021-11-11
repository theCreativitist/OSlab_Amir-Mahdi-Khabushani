WORDS = []
def load_data():
    print("Loading...") 
    try:
        with open( 'words_bank.txt', 'r') as f:
            big_text = f.read()
            lines = big_text.split('\n')

            for i in range(0, len(lines), 2):
                WORDS.append({ 'english':lines[i], 'persian':lines [i+1]})
    except(FileNotFoundError):
        print("ERROR LOADING - the word bank file is not present in the current directory.")
        exit()
    print('Loaded!')

def add_word(en_word,fa_word):
    already_added = []
    for WORD in WORDS:
        already_added.append(WORD['english'])
        already_added.append(WORD['persian'])
    if en_word in already_added or fa_word in already_added:
        print("Word is already in the bank!")
    else:
        with open('words_bank.txt', 'a') as f:
            f.write('\n'+en_word)
            f.write('\n'+fa_word)
        print('word added!')

def delete_dot(str):
    str = str.replace('.','')
    return str

def translate_en2fa(input_text):
    user_words = input_text.split(' ')
    output_text = ""
    for user_word in user_words: 
        has_dot = False
        user_word2 = delete_dot(user_word)
        if '.' in user_word:
            has_dot = True
        for WORD in WORDS: 
            if user_word2 == WORD ['english']:
                output_text += WORD ['persian']
                if has_dot:
                    output_text += '. '
                else:
                    output_text += ' '
                break
        else:
            output_text += user_word + " "
    return output_text


def translate_fa2en(input_text):
    user_words = input_text.split(' ')
    output_text = ""
    for user_word in user_words: 
        has_dot = False
        user_word2 = delete_dot(user_word)
        if '.' in user_word:
            has_dot = True
        for WORD in WORDS: 
            if user_word2 == WORD ['persian']:
                output_text += WORD ['english']
                if has_dot:
                    output_text += '. '
                else:
                    output_text += ' '
                break
        else:
            output_text += user_word + " "
    return output_text

print("Bilingual dictionary fa_en by AM khabushani!")
load_data() 
while(True):
    print("""
    MENU:
    1-en to fa
    2-fa to en
    3-add a new word
    4-exit
    """)
    command = input(">>>")
    if command=='1':
        user_text = input('please write your text: ')
        output_text = translate_en2fa(user_text) 
        print (output_text)
    elif command=='2':
        user_text = input('please write your text: ')
        output_text = translate_fa2en(user_text) 
        print (output_text)
    elif command=='3':
        en_word = input('please enter the English word: ')
        fa_word = input('please enter the Farsi word: ')
        add_word(en_word,fa_word)
        load_data()
    elif command=='4':
        exit()
    else:
        print("error - command not recognized. try again.")


