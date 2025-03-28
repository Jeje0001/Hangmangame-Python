import random

words=("apple","orange","banana","coconut","pineapple")

hangman_art={0:("   ",
                "   ",
                "   "),
             1:(" o ",
                "   ",
                "   "),
             2:(" o ",
                " | ",
                "   "),
             3:(" o ",
                "/| ",
                "   "),
             4:(" o ",
                "/|\\",
                "   "),
             5:(" o ",
                "/|\\",
                "/  "),
             6:(" o ",
                 "/|\\",
                 "/ \\" )}


# print(hangman_art[0])

def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    
    answer=random.choice(words)
    hint=["_"] * len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running == True:
        pass
# continue at 6:17:19
    print(hint)
if __name__ == "__main__":
    main()
