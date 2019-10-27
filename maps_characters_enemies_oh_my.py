from time import sleep
import requests
from bs4 import BeautifulSoup
import random


class Player:
    def __init__(self, player_name, hp, money, defence, speed):
        self.player_name = player_name
        self.hp = hp
        self.money = money
        self.defence = defence
        self.speed = speed

    def __str__(self):
        return f'{self.player_name} HP:{self.hp} Money:{self.money}'


class GenerateEnemy:
    def __init__(self):
        enemy_types = ['Ogre', 'Giant Spider', 'Troll']
        self.enemy_type = enemy_types[random.randint(0, len(enemy_types))]
        self.hp = random.randint(0, 50)
        self.defence = random.randint(0, 50)
        self.speed = random.randint(0, 50)

    def __str__(self):
        return f'{self.enemy_type} HP:{self.hp} Defence:{self.defence}'


def choose_player_type():
    while True:
        char_choice = input('Would you rather be (S)tronger or (F)aster? (Choose S or F)')
        possible_answers = ['S', 's', 'F', 'f']
        if char_choice in possible_answers:
            break
    return char_choice.lower()


def name_your_player():
    while True:
        name_input = input('What is your name? ')
        if name_input is not '':
            break
    return name_input


def invert_player_name(string_in):
    string_in = string_in.lower()
    return string_in[::-1]


def get_the_news():
    news_choices = ['minecraft', 'dungeons', 'Adventure.Time', 'xbox.one']
    try:
        rando_news_choice = news_choices[random.randint(0, len(news_choices) - 1)]
        r1 = requests.get('https://www.google.com/search?q=' + rando_news_choice + '&source=lnms&tbm=nws')
        news_page = r1.content
        soup1 = BeautifulSoup(news_page, 'html5lib')
        soupdivs = soup1.find("div", class_='g')
        news_headline = soupdivs.text
    except(ConnectionError, Exception):
        news_headline = 'Ogres, Giant Spiders, and DemonFerries - oh my.  Old maleficent news, or something to watch'
    return news_headline.split()


def slowprint(slowinput):
    string_in = slowinput.split()
    for x in range(0, len(string_in)):
        print(string_in[x] + ' ', end='')
        sleep(random.random())
    print("")
    return True

def main():
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print(".::.           Welcome                      .::.")
    sleep(.5)
    print(".::. I hope you are ready for an adventure. .::.")
    sleep(.5)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.\n\n")
    sleep(2)
    player_name = name_your_player()
    player_name = invert_player_name(player_name)
    player_name = player_name.title()  # This capitalizes first letters
    sleep(2)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print("Well, {}, you seem up to the task {}.".format(player_name, player_name))
    input()
    player_type = choose_player_type()
    if player_type == 's':
        hero_def = 80
        hero_speed = 40
    elif player_type == 'f':
        hero_def = 60
        hero_speed = 80
    else:
        hero_def = 50
        hero_speed = 50
    hero = Player(player_name, 90, 100, hero_def, hero_speed)
    sleep(1)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print("\n\n So, " + hero.player_name + ", my new friend... \n    I'm glad to have found you at the ")
    sleep(.2)
    print("         *** The Round Table ***\n Home of Double Sized Beers and Endless Nachos on Tuesday")
    sleep(.3)
    print("\n     I need your help to find a treasure.\n")
    while True:
        helping_hand = input("Will you help? y/n ")
        if helping_hand == 'y':
            break
        elif helping_hand == 'n':
            print("\n\n\nWell... thanks for nothing.")
            exit(0)
        else:
            continue
    sleep(1)
    print("\nWell, get some sleep my friend, tomorrow we begin. \n\n")
    sleep(2)
    print("ZzzzzzzzzzZZZZzzzzzZZzzzzzZZzzZzzzzzzzzzZZZZzzzzzZZzzzzzZZzzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzz")
    sleep(2)
    print("ZzzzzzzzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzz")
    sleep(1)
    print("ZzzzzzzzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZZzzzzzzzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZZzzzzzzzzzZZZZzzzzzZZ")
    sleep(3)
    print("ZZZZzzzzzZZzzzzzZZzzZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzz")
    sleep(1)
    print("zzzZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzz")
    print("ZzzzzZZzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzz")
    sleep(1)
    print("ZzZZzzzzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzz")
    sleep(1)
    print("ZzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzzZZZZZZ")
    sleep(3)
    print("Jeez.  Wake up man.  Were you planning on sleeping all day?")
    sleep(2)
    print("That was a rhetorical question.  We should begin immediately.  My name is Wazzere.  Here, Take this sword.")
    sleep(3)
    print("ZZZZzzzzzZZzzzzzZZzzZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzzZZzzZZzZZzzzZZZzzzZZzzZZzzzzzzzz")
    sleep(1)
    print("zzzZzzzzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzZZZzzZzzzZZzzZZzzzZzzz")
    print("ZzzzzZZzzzZZZZzzzzzZZzzzzzZZzzZZzzZzzZZZZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZZZzzzzzZZzzZZzzZzzZZZZZZzzZZzzZZzzz")
    sleep(1)
    print("damn it, man.  You shouldn't fall asleep with a sword in your hand.  Get up.  It's time to go.")
    print("\n\n\n\n")
    sleep(4)
    print("{} and Wazzere emerge from The Round Table, swords in hand.\n\n".format(player_name))
    sleep(2)
    print("Looking left, {} sees the town Newspaper.  The headline reads: ".format(player_name))
    print("\n\n **********************************************")
    print("*******The Herald of Heralds by Herald**********")
    print(" **********************************************")
    news_words = get_the_news()
    counter = 0
    for x in range(0, len(news_words)):
        if counter < 8:
            print(news_words[x] + ' ', end='')
            counter = counter + 1
        else:
            print(news_words[x])
            counter = 0
        if x == 11:
            if len(news_words[x]) > 3:
                magic_word = news_words[x]
            else:
                magic_word = 'Open Sesame in the bottom corner'
    print("\n**********************************************")
    print("**********************************************")
    sleep(2)
    print("\nThe word {} really stuck out to {}".format(magic_word, player_name))
    sleep(2)
    print("\n . . . . Lets get going, buddy.\n")
    sleep(2)
    slowprint("  The pair proceed punctually picking up the pace, with Wazzere leading the way, the path takes them")
    slowprint("into a thick forrest. Wazzere grabs a fallen branch, and utters .:Incendio:. and the end of the branch")
    slowprint("burst into flames.")
    print("")
    slowprint("Now that we can see what is in front of us, how do you look?")
    print(hero)
    print("\n\n")
    slowprint("Wazzere exclaims, That's good, because here comes our first challenge.")
    enemy = GenerateEnemy()
    print(enemy)


if __name__ == "__main__":
    main()
