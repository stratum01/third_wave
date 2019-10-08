from time import sleep


class Player():
    def __init__(self, player_name, hp, money, defence, speed):
        self.player_name = player_name
        self.hp = hp
        self.money = money
        self.defence = defence
        self.speed = speed

    def __str__(self):
        return f'{self.player_name} HP:{self.hp} Money:{self.money}'


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
    print("That was a rhetorical question.  We should begin immediately.  Here, Take this sword")



if __name__ == "__main__":
    main()
