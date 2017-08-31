import random

def hangman(word):
    wrong = 0
    guessed = []
    stages = ["",
              "___________     ",
              "|        |      ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               ",
              "|_______________"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages)-1:
        print("\n")
        print(" ".join(board))
        if len(guessed) > 0:
            print("You have guessed: " + " ".join(guessed))
        msg = "Guess a letter "
        char = input(msg)
        guessed.append(char)
        guessed = sorted(guessed)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        e = wrong+1
        if "__" not in board:
            print("\n".join(stages))
            print("You win! It was:")
            print("".join(board))
            win = True
            break
        else:
            print("\n".join(stages[:e]))
    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))

wordlist = ['time','year','people','way','day','man','thing','woman','life',
            'child','world','school','state','family','student','group',
            'country','problem','hand','part','place','case','week','company',
            'system','program','question','work','government','number','night',
            'point','home','water','room','mother','area','money','story',
            'fact','month','lot','right','study','book','eye','job','word',
            'business','issue','side','kind','head','house','service','friend',
            'father','power','hour','game','line','end','member','law','car',
            'city','community','name','president','team','minute','idea','kid',
            'body','information','back','parent','face','others','level',
            'office','door','health','person','art','war','history','party',
            'result','change','morning','reason','research','girl','guy',
            'moment','air','teacher','force','education']

hangman(random.choice(wordlist))
