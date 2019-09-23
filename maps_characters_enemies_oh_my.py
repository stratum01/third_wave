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
    player_name = player_name.title()
    sleep(2)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print(".::::::::::::::::::::::::::::::::::::::::::::::.")
    sleep(.5)
    print("Well, {}, you seem up to the task {}.".format(player_name, player_name))
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
    print(hero)


if __name__ == "__main__":
    main()
