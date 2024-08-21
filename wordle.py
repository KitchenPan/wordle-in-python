import random, re;from colorama import*
init()

user_word = word_of_day = "";num_tries = 0
good = ["GENIUS", "UNBEATEN", "COOL", "GOOD JOB", "CLOSE ONE", "PHEW"]

def game(correct = Back.GREEN, there = Back.YELLOW):
    global user_word, word_of_day, num_tries

    solved = False
    word_of_day = chooseWord("wordle\\pan\\wordle words.txt")
    print(word_of_day)

    while num_tries < 6:
        final_answer = ""
        user_word = wordInput()
        for i in range(5):
            if user_word[i] == word_of_day[i]:
                final_answer += correct + user_word[i] + Back.RESET
            elif user_word[i] in word_of_day:
                final_answer += there + user_word[i] + Back.RESET
            else:
                final_answer += user_word[i]
        print(final_answer);num_tries += 1
        like = re.match(user_word,word_of_day,re.IGNORECASE)
        if (like):
            print(Back.WHITE + Fore.BLACK + good[num_tries-1] + Style.RESET_ALL)
            num_tries += 6
            solved = True
                
    if solved != True:
        print("GOOD TRY!\nTHE WORD WAS: ", word_of_day)

def wordInput():
    user_word = ""
    while len(user_word) < 5:
        user_word = input(Back.WHITE + "ENTER A 5 LETTER WORD: " + Back.RESET)
        if len(user_word) > 5 or len(user_word) < 5:
            print(Back.RED + Fore.WHITE + "NOT ENOUGH LETTERS" + Style.RESET_ALL)
            print()
    return user_word.upper().strip()

def chooseWord(filepath):
    file = open(filepath, "r")
    file_read = file.readlines()
    word = file_read[random.randrange(0, len(file_read))]
    file.close()
    return word.upper().strip()

def tutorial():
    print(Back.GREEN + "W" + Back.RESET + "EARY")
    print("The letter W is in the word and in the correct spot.\n")
    print("P" + Back.YELLOW + "I" + Back.RESET + "LLS")
    print("The letter I is in the word but in the wrong spot.\n")
    print("VAG" + Back.LIGHTBLACK_EX + Fore.WHITE + "U" + Style.RESET_ALL + "E")
    print("The letter U is not in the word in any spot.\n")

def query():
    mainChoice = input("DO YOU WANT TO CONTINUE? (Y/N)")
    if mainChoice.upper() == "Y":
        choice()             
    else:
        print("HOPE YOU HAD FUN :D")

def choice():
    print("[1] START A NEW GAME")
    print("[2] VIEW TUTORIAL")
    print("[3] VIEW SCORE | WORK IN PROGRESS")
    print("[4] TURN ON EASY READ AND PLAY")
    print("[5] EXIT GAME")
    choice = int(input("ENTER CHOICE: "))          
    if choice == 1:
        game()
        query()
    if choice == 2:
        tutorial()
        query()
    if choice == 5:
        print("HOPE YOU HAD FUN :D")
        pass

choice()