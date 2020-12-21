import random as rng

# Caverns game by Ethan May. Made purely for learning purposes. Expect trash code.

good_responses = {  # Used for good_room()
    "1": "Thick, hot air floods your face as you see a crystal clear, steaming pool of luxurious water.",
    "2": "A silent miner's home creaks as you step into it to gather the left behind food.",
    "3": "The crackle of a camp fire tickles your ears as you're greeted by an adventurer bearing food!",
    "4": "A boulder covers the path. As you push it your strength grows!",
    "5": "The sharp scraping of a grindstone startles you as a blacksmith asks to sharpen your sword.",
    "6": "Whispers of tortured souls wail as a robed wizard hands you a potion that makes your muscles bulge!"
}

neutral_responses = {  # Used for neutral_room()
    "1": "A dripping, cool cavern opens up in front of you, nothing but floor to bear.",
    "2": "A dry, cracked skeleton leans on a wall to your side, looted and pillaged",
    "3": "A glaring, bothered miner stares at you as you walk into the room"
}

poor_responses = {  # Used for poor_room()
    "1": "A maleficent arachnid crawls and leaps at you, getting a good bite in before it's demise",
    "2": "Dozens of gnarled, sickly rats rush towards you. They get several small bites before retreating",
    "3": "A starving ogre turns and clomps towards you. After a few strikes from your sword he yowls and runs away",
    "4": "A swarm of vampire bats crowd the cave. They take lots of blood before you can get to a safe place",
    "5": "An oppressing film of dark magic fills the room. A wretched witch drains your power before vanishing",
    "6": "As the next cavern collapses, a boulder traps your foot underneath it, it takes a great strength to free it"
}

boss_responses = {  # Used for boss_room()
    "1": "A dragon wakes at your entrance, spewing fire everywhere! You get past it before you're swallowed whole.",
    "2": "A wretched witch howls while electrocuting you! You get behind cover and she flees the room.",
    "3": "Through a ravine a huge scorpion tail emerges and slams you into a wall! You escape its blind attacks."
}


def new_game():  # Starts a new game!
    print("Welcome to Caverns!")
    hp = 20
    st = 1
    room_count = 0
    print("Current HP: " + str(hp) + " Current ST: " + str(st))
    enter_door(hp, st, room_count)


def enter_door(hp, st, room_count):  # User chooses a door and rng chooses consequences
    if hp < 1:
        end_game()
    if (room_count % 5 == 0) & (room_count != 0):  # Boss room every 5 rooms and increases difficulty after each one
        difficulty = room_count / 5
        boss_room(hp, st, room_count, difficulty)
    fake_door = input("Three doors appear! 1/2/3: ")  # User input currently has no effect on game-play - bad idea
    door = rng.randrange(1, 4)
    if door == 1:
        good_room(hp, st, room_count)
    elif door == 2:
        neutral_room(hp, st, room_count)
    elif door == 3:
        bad_room(hp, st, room_count)
    else:
        print("Error code 01")


def good_room(hp, st, room_count):
    current_response = str(rng.randrange(1, 6))
    print(good_responses[current_response])
    if (current_response == "1") | (current_response == "2") | (current_response == "3"):  # These rooms are +health
        hp += 4
        print("Effect: Gained 4 HP, Current HP = " + str(int(hp)))
    elif (current_response == "4") | (current_response == "5") | (current_response == "6"):  # These are +strength
        st += 1
        print("Effect: Gained 1 ST, Current ST = " + str(st))
    else:
        print("Error code 02")
    room_count += 1
    enter_door(hp, st, room_count)


def neutral_room(hp, st, room_count):  # Empty rooms. Brings you to boss rooms faster - inherently negative
    print(neutral_responses[str(rng.randrange(1, 4))])
    print("Effect: None")
    room_count += 1
    enter_door(hp, st, room_count)


def bad_room(hp, st, room_count):
    current_response = str(str(rng.randrange(1, 3)))
    print(poor_responses[current_response])
    if (current_response == "1") | (current_response == "2") | (current_response == "3"):  # These rooms are -health
        hp -= 4 / st
        lost_hp = "Effect: Lost {:.0f} HP! Current HP: " + str(int(hp))
        print(lost_hp.format(4 / st))
    elif (current_response == "4") | (current_response == "5") | (current_response == "6"):  # These rooms are -strength
        st -= 1
        print("Effect: Lost 1 ST, Current ST: " + str(st))
    else:
        print("Error code 03")
    room_count += 1
    enter_door(hp, st, room_count)


def boss_room(hp, st, room_count, difficulty):
    current_response = str(rng.randrange(1, 4))  # All boss rooms are -health
    print(boss_responses[current_response])
    hp -= ((10 / (st/2)) - difficulty)  # This algorithm might be too harsh for every 5 rooms
    lost_hp = "Effect: Lost {:.0f} HP! Current HP: " + str(int(hp))
    print(lost_hp.format(((10 / (st/2)) - difficulty)))
    room_count += 1
    enter_door(hp, st, room_count)


def end_game():
    print("You died!")
    print("Thanks for playing!")
    replay = input("Play again? y/n: ")  # Prompt to replay. I wouldn't...
    if replay == "y":
        new_game()
    else:
        print("Game ended")
        quit()


new_game()
