import random
import time
import json
import os
import sys
from tkinter import *
path_to_tycoon = r'C:\Users\blood\PycharmProjects\conditionalstatement\tycoon'
existing_players = [file.split('.')[0] for file in os.listdir(path_to_tycoon) if file.endswith('.json')]
automatic_spin_triggered = 0
mod = Tk()

mode_infinite_money = 0
mode_infinite_spin = 0

def restart_game():
    global your_money, score,spin_left, cost, shop_cost, upgrade,upgrade_stats, ordinary_ore, uncommon_ore, epic_ore, legendary_ore, mythical_ore, common_pet, uncommon_pet, epic_pet, legendary_pet, mythical_pet,unknown_pet, secret_pet,rebirth_cost, rebirth_count, pet_cost, automatic_spin_triggered
    your_money = 0
    score = 0
    spin_left = 3
    cost = 100
    shop_cost = 100
    upgrade = 100
    upgrade_stats = 0
    ordinary_ore = 0
    uncommon_ore = 0
    epic_ore = 0
    legendary_ore = 0
    mythical_ore = 0
    common_pet = 0
    uncommon_pet = 0
    epic_pet = 0
    legendary_pet = 0
    mythical_pet = 0
    unknown_pet = 0
    secret_pet = 0
    rebirth_cost = 15600
    rebirth_count = 0
    pet_cost = 1500
    automatic_spin_triggered = 0

def auto_spin():
    global your_money, spin_left, score,random_number
    money_earn = 0
    if spin_left > 1:
        while spin_left > 1:
            if upgrade_stats == 1:
                random_number = random.randint(100, 200)
                save_player_data(player_data)
            elif upgrade_stats == 2:
                random_number = random.randint(200, 300)
                save_player_data(player_data)
            elif upgrade_stats == 3:
                random_number = random.randint(300, 400)
                save_player_data(player_data)
            elif upgrade_stats == 4:
                random_number = random.randint(400, 500)
                save_player_data(player_data)
            elif upgrade_stats == 5:
                random_number = random.randint(500, 600)
                save_player_data(player_data)
            elif upgrade_stats == 6:
                random_number = random.randint(600, 700)
                save_player_data(player_data)
            elif upgrade_stats == 7:
                random_number = random.randint(700, 800)
                save_player_data(player_data)
            elif upgrade_stats == 8:
                random_number = random.randint(800, 900)
                save_player_data(player_data)
            elif upgrade_stats == 9:
                random_number = random.randint(900, 1000)
                save_player_data(player_data)
            elif upgrade_stats == 10:
                random_number = random.randint(1000, 1100)
                save_player_data(player_data)
            elif upgrade_stats == 11:
                random_number = random.randint(1100, 1200)
                save_player_data(player_data)
            elif upgrade_stats == 12:
                random_number = random.randint(1200, 1300)
                save_player_data(player_data)
            elif upgrade_stats == 13:
                random_number = random.randint(1300, 1400)
                save_player_data(player_data)
            elif upgrade_stats == 14:
                random_number = random.randint(1500, 1600)
                save_player_data(player_data)
            elif upgrade_stats == 15:
                random_number = random.randint(1600, 1700)
                save_player_data(player_data)
            elif upgrade_stats == 16:
                random_number = random.randint(1700, 1800)
                save_player_data(player_data)
            elif upgrade_stats == 17:
                random_number = random.randint(1800, 1900)
                save_player_data(player_data)
            elif upgrade_stats == 18:
                random_number = random.randint(1900, 2000)
                save_player_data(player_data)
            elif upgrade_stats == 22:
                random_number = random.randint(2500, 2700)
                save_player_data(player_data)
            elif upgrade_stats == 24:
                random_number = random.randint(3000, 4000)
                save_player_data(player_data)
            elif upgrade_stats == 26:
                random_number = random.randint(5000, 6000)
                save_player_data(player_data)
            elif upgrade_stats == 28:
                random_number = random.randint(7000, 8000)
                save_player_data(player_data)
            elif upgrade_stats == 30:
                random_number = random.randint(10000, 15000)
                save_player_data(player_data)
            elif upgrade_stats == 35:
                random_number = random.randint(30000, 50000)
                save_player_data(player_data)
            elif upgrade_stats == 40:
                random_number = random.randint(55000, 80000)
                save_player_data(player_data)
            elif upgrade_stats == 50:
                random_number = random.randint(80000, 150000)
                random_number += random.randint(50000, 80000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats == 70:
                random_number = random.randint(200000, 500000)
                random_number += random.randint(100000, 550000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats == 90:
                random_number = random.randint(500000, 1000000)
                random_number += random.randint(900000, 1200000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats >= 100:
                random_number = random.randint(50000000, 100000000)
                random_number += random.randint(90000000, 999999999)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            else:
                random_number = random.randint(0, 100)
                your_money += random_number
                money_earn += random_number
                spin_left -= 1
                score += 1

            print_colored_text(f"\nYou've Got: {random_number}!", current_color)
            time.sleep(1)
    elif spin_left == 0:
        ask_auto = str(input("Are you sure you want to use auto spin even you have 1 spin left?").lower())
        if ask_auto == 'yes':
            while spin_left == 1:
                if upgrade_stats == 1:
                    random_number = random.randint(100, 200)
                    save_player_data(player_data)
                elif upgrade_stats == 2:
                    random_number = random.randint(200, 300)
                    save_player_data(player_data)
                elif upgrade_stats == 3:
                    random_number = random.randint(300, 400)
                    save_player_data(player_data)
                elif upgrade_stats == 4:
                    random_number = random.randint(400, 500)
                    save_player_data(player_data)
                elif upgrade_stats == 5:
                    random_number = random.randint(500, 600)
                    save_player_data(player_data)
                elif upgrade_stats == 6:
                    random_number = random.randint(600, 700)
                    save_player_data(player_data)
                elif upgrade_stats == 7:
                    random_number = random.randint(700, 800)
                    save_player_data(player_data)
                elif upgrade_stats == 8:
                    random_number = random.randint(800, 900)
                    save_player_data(player_data)
                elif upgrade_stats == 9:
                    random_number = random.randint(900, 1000)
                    save_player_data(player_data)
                elif upgrade_stats == 10:
                    random_number = random.randint(1000, 1100)
                    save_player_data(player_data)
                elif upgrade_stats == 11:
                    random_number = random.randint(1100, 1200)
                    save_player_data(player_data)
                elif upgrade_stats == 12:
                    random_number = random.randint(1200, 1300)
                    save_player_data(player_data)
                elif upgrade_stats == 13:
                    random_number = random.randint(1300, 1400)
                    save_player_data(player_data)
                elif upgrade_stats == 14:
                    random_number = random.randint(1500, 1600)
                    save_player_data(player_data)
                elif upgrade_stats == 15:
                    random_number = random.randint(1600, 1700)
                    save_player_data(player_data)
                elif upgrade_stats == 16:
                    random_number = random.randint(1700, 1800)
                    save_player_data(player_data)
                elif upgrade_stats == 17:
                    random_number = random.randint(1800, 1900)
                    save_player_data(player_data)
                elif upgrade_stats == 18:
                    random_number = random.randint(1900, 2000)
                    save_player_data(player_data)
                elif upgrade_stats == 22:
                    random_number = random.randint(2500, 2700)
                    save_player_data(player_data)
                elif upgrade_stats == 24:
                    random_number = random.randint(3000, 4000)
                    save_player_data(player_data)
                elif upgrade_stats == 26:
                    random_number = random.randint(5000, 6000)
                    save_player_data(player_data)
                elif upgrade_stats == 28:
                    random_number = random.randint(7000, 8000)
                    save_player_data(player_data)
                elif upgrade_stats == 30:
                    random_number = random.randint(10000, 15000)
                    save_player_data(player_data)
                elif upgrade_stats == 35:
                    random_number = random.randint(30000, 50000)
                    save_player_data(player_data)
                elif upgrade_stats == 40:
                    random_number = random.randint(55000, 80000)
                    save_player_data(player_data)
                elif upgrade_stats == 50:
                    random_number = random.randint(80000, 150000)
                    random_number += random.randint(50000, 80000)
                    print(f"{random_number} bonus!")
                    save_player_data(player_data)
                elif upgrade_stats == 70:
                    random_number = random.randint(200000, 500000)
                    random_number += random.randint(100000, 550000)
                    print(f"{random_number} bonus!")
                    save_player_data(player_data)
                elif upgrade_stats == 90:
                    random_number = random.randint(500000, 1000000)
                    random_number += random.randint(900000, 1200000)
                    print(f"{random_number} bonus!")
                    save_player_data(player_data)
                elif upgrade_stats >= 100:
                    random_number = random.randint(50000000, 100000000)
                    random_number += random.randint(90000000, 999999999)
                    print(f"{random_number} bonus!")
                    save_player_data(player_data)
        elif ask_auto == 'no':
            print("OKAY!")

    print_colored_text(f"\nAuto Spin completed! Total money earned: {money_earn}", current_color)
    save_player_data(player_data)

def trade_all_ores():
    global your_money, ordinary_ore, uncommon_ore, epic_ore, legendary_ore, mythical_ore

    total_ores = ordinary_ore + uncommon_ore + epic_ore + legendary_ore + mythical_ore
    total_money_earned = total_ores * cost

    your_money += total_money_earned
    print_colored_text(f"You traded all your ores for {total_money_earned} money!", current_color)

    # Reset ore counts
    ordinary_ore = 0
    uncommon_ore = 0
    epic_ore = 0
    legendary_ore = 0
    mythical_ore = 0
    save_player_data(player_data)

def handle_keyboard_interrupt():
    print("\nExiting the game.")
    sys.exit()


#color
BLUE = "\033[94m"
DEFAULT = "\033[0m"
GREEN = '\033[92m'
RED = "\033[91m"
ORANGE = "\033[33m"
YELLOW = "\033[93m"
VIOLET = "\033[95m"
BLACK = "\033[30m"

def save_player_data(player_data):
    player_data['automatic_spin'] = automatic_spin_triggered
    with open(f'{player_data["name"]}.json', 'w') as f:
        json.dump(player_data, f)

def load_player_data(player_name):
    try:
        with open(f'{player_name}.json', 'r') as f:
            player_data = json.load(f)
            return player_data
    except FileNotFoundError:
        return {
            'name': player_name,
            'your_money': 0,
            'score': 0,
            'spin_left': 3,
            'cost': 100,
            'shop_cost': 100,
            'upgrade': 200,
            'upgrade_stats': 0,
            'ordinary_ore': 0,
            'uncommon_ore': 0,
            'epic_ore': 0,
            'legendary_ore': 0,
            'mythical_ore': 0,
            'probability': {
                "ordinary_ore_probability": 60,
                "uncommon_ore_probability": 40,
                "epic_ore_probability": 20,
                "legendary_ore_probability": 5,
                "mythical_ore_probability": 1
            },
            'common_pet': 0,
            'uncommon_pet': 0,
            'epic_pet': 0,
            'legendary_pet': 0,
            'mythical_pet': 0,
            'unknown_pet': 0,
            'secret_pet': 0,
            'pet_cost': 1500,
            'pet_triggered': 1,
            'cheat_triggered': 0,
            'rebirth_count': 0,
            'money_multiplier': 1.2,
            'upgrade_cost_multiplier': 1.5,
            'rebirth_cost': 15600,
            'automatic_spin': 0
        }
def print_colored_text(text, color):
    colors = {
        'blue': BLUE,
        'default': DEFAULT,
        'green': GREEN,
        'red': RED,
        'orange': ORANGE,
        'yellow': YELLOW,
        'violet': VIOLET
    }
    print(f"{colors.get(color, colors['default'])}{text}\033[0m")
current_color = 'default'

player_name = input("Enter your username: ")
player_data = load_player_data(player_name)

print("Searching your name")

time.sleep(2)
if player_name not in existing_players:
    print("File name not found")
else:
    print("File Name found!")

time.sleep(1)
print("Initializing Game...")
time.sleep(5)
print("Loading Please wait...")
time.sleep(2)

def loading_process():
    print("Loading...", end="", flush=True)
    for i in range(101):
        time.sleep(0.05)
        print("\rProgress: {}%".format(i), end="", flush=True)
    time.sleep(2)
    print("\nLoading completed!")

loading_process()

if player_name in existing_players:
    time.sleep(3)
    print("Progress Loaded!")
    time.sleep(3)
else:
    time.sleep(3)
    print("Game Loaded!")
    time.sleep(3)
print('\n\nwelcome to randomizer!'
      '\nGame made by: Kiryo'
      '\ntype help if you dont know how to play!                                                                                                                    Game version: v1.0.1')
print("type whats new to see the recent update (only 0.7.1)")
#VARIABLE

spin_left = 3
your_money = 0
cost = 100
score = 0
shop_cost = 100
#upgrade
upgrade = 200
upgrade_stats = 0
#ore
ordinary_ore = 0
uncommon_ore = 0
epic_ore = 0
legendary_ore = 0
mythical_ore = 0
#ore chance
probability ={
    "ordinary_ore_probability": 60,
    "uncommon_ore_probability": 40,
    "epic_ore_probability": 20,
    "legendary_ore_probability": 5,
    "mythical_ore_probability": 1
}
assert sum(probability.values()) == 126
#other
triggered = 0
instruction = 0
#Chance Pets#
common_pet_probability = 10
uncommon_pet_probability = 6
epic_pet_probability = 3
legendary_pet_probability = 1
mythical_pet_probability = 0.5
unknown_pet_probability = 0.2
secret_pet_probability = 0.01
#pets owned#
common_pet = 0
uncommon_pet = 0
epic_pet = 0
legendary_pet = 0
mythical_pet = 0
unknown_pet = 0
secret_pet = 0
#current
common_pet_probability = int(common_pet_probability)
uncommon_pet_probability = int(uncommon_pet_probability)
epic_pet_probability = int(epic_pet_probability)
legendary_pet_probability = int(legendary_pet_probability)
mythical_pet_probability = int(mythical_pet_probability)
unknown_pet_probability = int(unknown_pet_probability)
secret_pet_probability = int(secret_pet_probability)
#pet cost#
pet_cost = 1500
#this variable can track the pet bonuses
pet_triggered = 1
#dangerous command#
cheat_triggered = 0
#rebirth system
rebirth_count = 0
money_multiplier = 1.2  # Adjust as needed
upgrade_cost_multiplier = 1.5
rebirth_cost = 15600

#current bonuses pet
current_pet_common = 300
current_pet_uncommon = 500
current_pet_epic = 900
current_pet_legendary = 1500
current_pet_mythical = 2500
current_pet_unknown = 4000
current_pet_secret = 5700
if player_name not in existing_players:
    print(f"\n\nWelcome! {player_name}. The new user!")
    player_data = {
        'name': player_name,
        'your_money': 0,
        'score': 0,
        'spin_left': 3,
        'cost': 100,
        'shop_cost': 100,
        'upgrade': 200,
        'upgrade_stats': 0,
        'ordinary_ore': 0,
        'uncommon_ore': 0,
        'epic_ore': 0,
        'legendary_ore': 0,
        'mythical_ore': 0,
        'probability': {
            "ordinary_ore_probability": 60,
            "uncommon_ore_probability": 40,
            "epic_ore_probability": 20,
            "legendary_ore_probability": 5,
            "mythical_ore_probability": 1
        },
        'common_pet': 0,
        'uncommon_pet': 0,
        'epic_pet': 0,
        'legendary_pet': 0,
        'mythical_pet': 0,
        'unknown_pet': 0,
        'secret_pet': 0,
        'pet_cost': 1500,
        'pet_triggered': 1,
        'cheat_triggered': 0,
        'rebirth_count': 0,
        'money_multiplier': 1.2,
        'upgrade_cost_multiplier': 1.5,
        'rebirth_cost': 15600,
        'automatic_spin': 0
    }
else:
    print(f"\n\nWelcome back, {player_name}!")
    player_data = load_player_data(player_name)


while True:
    print(f"your current money is: {player_data['your_money']}")
    print(f"Your current score is: {player_data['score']}")
    print(f"You have {player_data['spin_left']} spins left.")
    print(f"The cost of a spin is: {player_data['cost']}")
    print(f"The cost of a pet is: {player_data['pet_cost']}")
    print(f"Your current upgrade stats is: {player_data['upgrade_stats']}")
    print(f"Your current rebirth cost is: {player_data['rebirth_cost']}")
    automatic_spin_triggered = player_data.get('automatic_spin', 0) # Line 272
    # Restore the player's game state
    your_money = player_data['your_money']
    score = player_data['score']
    spin_left = player_data['spin_left']
    cost = player_data['cost']
    shop_cost = player_data['shop_cost']
    upgrade = player_data['upgrade']
    upgrade_stats = player_data['upgrade_stats']
    ordinary_ore = player_data['ordinary_ore']
    uncommon_ore = player_data['uncommon_ore']
    epic_ore = player_data['epic_ore']
    legendary_ore = player_data['legendary_ore']
    mythical_ore = player_data['mythical_ore']
    probability = player_data['probability']
    common_pet = player_data['common_pet']
    uncommon_pet = player_data['uncommon_pet']
    epic_pet = player_data['epic_pet']
    legendary_pet = player_data['legendary_pet']
    mythical_pet = player_data['mythical_pet']
    unknown_pet = player_data['unknown_pet']
    secret_pet = player_data['secret_pet']
    pet_cost = player_data['pet_cost']
    pet_triggered = player_data['pet_triggered']
    cheat_triggered = player_data['cheat_triggered']
    rebirth_count = player_data['rebirth_count']
    money_multiplier = player_data['money_multiplier']
    upgrade_cost_multiplier = player_data['upgrade_cost_multiplier']
    rebirth_cost = player_data['rebirth_cost']
    save_player_data(player_data)
    # list
    occurrences = (
            ['Common Pet'] * common_pet_probability +
            ['Uncommon Pet'] * uncommon_pet_probability +
            ['Epic Pet'] * epic_pet_probability +
            ['Legendary Pet'] * legendary_pet_probability +
            ['Mythical Pet'] * mythical_pet_probability +
            ['Unknown Pet'] * unknown_pet_probability +
            ['Secret Pet'] * secret_pet_probability
    )

    while True:
        player_data['your_money'] = your_money
        player_data['score'] = score
        player_data['spin_left'] = spin_left
        player_data['cost'] = cost
        player_data['shop_cost'] = shop_cost
        player_data['upgrade'] = upgrade
        player_data['upgrade_stats'] = upgrade_stats
        player_data['ordinary_ore'] = ordinary_ore
        player_data['uncommon_ore'] = uncommon_ore
        player_data['epic_ore'] = epic_ore
        player_data['legendary_ore'] = legendary_ore
        player_data['mythical_ore'] = mythical_ore
        player_data['probability'] = probability
        player_data['common_pet'] = common_pet
        player_data['uncommon_pet'] = uncommon_pet
        player_data['epic_pet'] = epic_pet
        player_data['legendary_pet'] = legendary_pet
        player_data['mythical_pet'] = mythical_pet
        player_data['unknown_pet'] = unknown_pet
        player_data['secret_pet'] = secret_pet
        player_data['pet_cost'] = pet_cost
        player_data['pet_triggered'] = pet_triggered
        player_data['cheat_triggered'] = cheat_triggered
        player_data['rebirth_count'] = rebirth_count
        player_data['money_multiplier'] = money_multiplier
        player_data['upgrade_cost_multiplier'] = upgrade_cost_multiplier
        player_data['rebirth_cost'] = rebirth_cost
        player_data['automatic_spin'] = automatic_spin_triggered
        save_player_data(player_data)
        time.sleep(1)
        print_colored_text("\nyou have: " + str(your_money) + " money left and " + str(spin_left) + " spin left", current_color)
        time.sleep(0.7)
        print_colored_text("Do you wish to spin?", current_color)

        f_answer = str(input("Yes or No?: ").lower())
        save_player_data(player_data)
        if f_answer in ["trade", "upgrade", "help", "balance", "pet", "bag", "shop", "check score"]:
            pet_triggered = 0
            save_player_data(player_data)
        else:
            pet_triggered = 1
            save_player_data(player_data)
        if f_answer.lower() == "yes":
            save_player_data(player_data)
            if upgrade_stats == 1:
                random_number = random.randint(100, 200)
                save_player_data(player_data)
            elif upgrade_stats == 2:
                random_number = random.randint(200, 300)
                save_player_data(player_data)
            elif upgrade_stats == 3:
                random_number = random.randint(300, 400)
                save_player_data(player_data)
            elif upgrade_stats == 4:
                random_number = random.randint(400, 500)
                save_player_data(player_data)
            elif upgrade_stats == 5:
                random_number = random.randint(500, 600)
                save_player_data(player_data)
            elif upgrade_stats == 6:
                random_number = random.randint(600, 700)
                save_player_data(player_data)
            elif upgrade_stats == 7:
                random_number = random.randint(700, 800)
                save_player_data(player_data)
            elif upgrade_stats == 8:
                random_number = random.randint(800, 900)
                save_player_data(player_data)
            elif upgrade_stats == 9:
                random_number = random.randint(900, 1000)
                save_player_data(player_data)
            elif upgrade_stats == 10:
                random_number = random.randint(1000, 1100)
                save_player_data(player_data)
            elif upgrade_stats == 11:
                random_number = random.randint(1100, 1200)
                save_player_data(player_data)
            elif upgrade_stats == 12:
                random_number = random.randint(1200, 1300)
                save_player_data(player_data)
            elif upgrade_stats == 13:
                random_number = random.randint(1300, 1400)
                save_player_data(player_data)
            elif upgrade_stats == 14:
                random_number = random.randint(1500, 1600)
                save_player_data(player_data)
            elif upgrade_stats == 15:
                random_number = random.randint(1600, 1700)
                save_player_data(player_data)
            elif upgrade_stats == 16:
                random_number = random.randint(1700, 1800)
                save_player_data(player_data)
            elif upgrade_stats == 17:
                random_number = random.randint(1800, 1900)
                save_player_data(player_data)
            elif upgrade_stats == 18:
                random_number = random.randint(1900, 2000)
                save_player_data(player_data)
            elif upgrade_stats == 22:
                random_number = random.randint(2500, 2700)
                save_player_data(player_data)
            elif upgrade_stats == 24:
                random_number = random.randint(3000, 4000)
                save_player_data(player_data)
            elif upgrade_stats == 26:
                random_number = random.randint(5000, 6000)
                save_player_data(player_data)
            elif upgrade_stats == 28:
                random_number = random.randint(7000, 8000)
                save_player_data(player_data)
            elif upgrade_stats == 30:
                random_number = random.randint(10000, 15000)
                save_player_data(player_data)
            elif upgrade_stats == 35:
                random_number = random.randint(30000, 50000)
                save_player_data(player_data)
            elif upgrade_stats == 40:
                random_number = random.randint(55000, 80000)
                save_player_data(player_data)
            elif upgrade_stats == 50:
                random_number = random.randint(80000, 150000)
                random_number += random.randint(50000, 80000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats == 70:
                random_number = random.randint(200000, 500000)
                random_number += random.randint(100000, 550000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats == 90:
                random_number = random.randint(500000, 1000000)
                random_number += random.randint(900000, 1200000)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            elif upgrade_stats >= 100:
                random_number = random.randint(50000000, 100000000)
                random_number += random.randint(90000000, 999999999)
                print(f"{random_number} bonus!")
                save_player_data(player_data)
            else:
                random_number = random.randint(0, 100)
            your_money += random_number
            print_colored_text("\nYou've Got: " + str(random_number) + "!", current_color)
            spin_left -=1
            score += 1
            save_player_data(player_data)
            if triggered == 1:
                triggered = 0
                save_player_data(player_data)
                if triggered == 0:
                    save_player_data(player_data)
                    # chance
                    random_probability = random.randint(1, 100)
                    if random_probability <= probability['ordinary_ore_probability']:
                        print_colored_text("You got ordinary ore!", current_color)
                        ordinary_ore += 1
                        save_player_data(player_data)
                    elif random_probability <= probability["ordinary_ore_probability"] + probability[
                        "uncommon_ore_probability"]:
                        print_colored_text("You got uncommon ore!", current_color)
                        uncommon_ore += 1
                        save_player_data(player_data)
                    elif random_probability <= probability["ordinary_ore_probability"] + probability[
                        "uncommon_ore_probability"] + probability["epic_ore_probability"]:
                        print(VIOLET + "Woah! Congratulations on obtaining an epic ore!"+ DEFAULT)
                        epic_ore += 1
                        save_player_data(player_data)
                    elif random_probability <= probability["ordinary_ore_probability"] + probability[
                        "uncommon_ore_probability"] + probability["epic_ore_probability"] + probability[
                        "legendary_ore_probability"]:
                        print(ORANGE + "WOAH! CONGRATULATIONS ON GETTING A LEGENDARY ORE! How lucky!"+ DEFAULT)
                        legendary_ore += 1
                        save_player_data(player_data)
                    else:
                        print(RED +"OH MY GOD! YOU JUST GOT A MYTHICAL ITEM!"+ DEFAULT)
                        print(RED +"You Obtained a Mystical Mythical Ore! How lucky!"+ DEFAULT)
                        mythical_ore += 1
                        save_player_data(player_data)
            elif triggered == 0:
                random_probability = random.randint(1, 100)
                save_player_data(player_data)
                if random_probability <= probability['ordinary_ore_probability']:
                    print_colored_text("You got ordinary ore!", current_color)
                    ordinary_ore += 1
                    save_player_data(player_data)
                elif random_probability <= probability["ordinary_ore_probability"] + probability[
                    "uncommon_ore_probability"]:
                    print_colored_text("You got uncommon ore!", current_color)
                    uncommon_ore += 1
                    save_player_data(player_data)
                elif random_probability <= probability["ordinary_ore_probability"] + probability[
                    "uncommon_ore_probability"] + probability["epic_ore_probability"]:
                    print("Woah! Congratulations on obtaining an epic ore!")
                    epic_ore += 1
                    save_player_data(player_data)
                elif random_probability <= probability["ordinary_ore_probability"] + probability[
                    "uncommon_ore_probability"] + probability["epic_ore_probability"] + probability[
                    "legendary_ore_probability"]:
                    print("WOAH! CONGRATULATIONS ON GETTING A LEGENDARY ORE! How lucky!")
                    legendary_ore += 1
                    save_player_data(player_data)
                else:
                    print("OH MY GOD! YOU JUST GOT A MYTHICAL ITEM!")
                    print("You Obtained a Mystical Mythical Ore! How lucky!")
                    mythical_ore += 1
                    save_player_data(player_data)
            if pet_triggered == 1:
                if common_pet == 1:
                    your_money = your_money + current_pet_common
                    print_colored_text("You Received " + str(current_pet_common) + " from common pet", current_color)
                    save_player_data(player_data)

                elif common_pet >= 2:
                    your_money = your_money + (current_pet_common * 2)
                    print_colored_text("You Received " + str(current_pet_common * 2) + " from common pet", current_color)
                    save_player_data(player_data)

                if uncommon_pet == 1:
                    print_colored_text("You Received " + str(current_pet_uncommon) + " from uncommon pet", current_color)
                    your_money = your_money + current_pet_uncommon
                    save_player_data(player_data)

                elif uncommon_pet == 2:
                    print_colored_text("You Received " + str(current_pet_uncommon * 2) + " from uncommon pet", current_color)
                    your_money = your_money + (current_pet_uncommon * 2)
                    save_player_data(player_data)
                elif uncommon_pet >= 3:
                    print_colored_text("You Received " + str(current_pet_uncommon * 2) + " from uncommon pet", current_color)
                    your_money = your_money + (current_pet_uncommon*3)
                    save_player_data(player_data)

                if epic_pet == 1:
                    print_colored_text("You Received " + str(current_pet_epic) + " from epic pet", current_color)
                    your_money = your_money + current_pet_uncommon
                    save_player_data(player_data)

                elif epic_pet == 2:
                    print_colored_text("You Received " + str(current_pet_epic * 2) + " from epic pet", current_color)
                    your_money = your_money + (current_pet_epic * 2)
                    save_player_data(player_data)
                elif epic_pet >= 3:
                    print_colored_text("You Received " + str(current_pet_epic * 2) + " from epic pet", current_color)
                    your_money = your_money + (current_pet_epic * 3)
                    save_player_data(player_data)

                if legendary_pet == 1:
                    print_colored_text("You Received " + str(current_pet_legendary) + " from legendary pet", current_color)
                    your_money = your_money + current_pet_legendary
                    save_player_data(player_data)

                elif legendary_pet == 2:
                    print_colored_text("You Received " + str(current_pet_legendary * 2) + " from legendary pet",
                                       current_color)
                    your_money = your_money + (current_pet_legendary * 2)
                    save_player_data(player_data)
                elif legendary_pet == 3:
                    print_colored_text("You Received " + str(current_pet_legendary * 2) + " from legendary pet",
                                       current_color)
                    your_money = your_money + (current_pet_legendary * 3)
                    save_player_data(player_data)
                elif legendary_pet >= 4:
                    print_colored_text("You Received " + str(current_pet_legendary) + " from legendary pet",
                                       current_color)
                    your_money = your_money + (current_pet_legendary * 4)
                    save_player_data(player_data)

                if mythical_pet == 1:
                    print_colored_text("You Received " + str(current_pet_mythical) + " from mythical pet",
                                       current_color)
                    your_money = your_money + current_pet_mythical
                    save_player_data(player_data)
                elif mythical_pet == 2:
                    print_colored_text("You Received " + str(current_pet_mythical) + " from mythical pet",
                                       current_color)
                    your_money = your_money + (current_pet_mythical * 2)
                    save_player_data(player_data)
                elif mythical_pet == 3:
                    print_colored_text("You Received " + str(current_pet_mythical) + " from mythical pet",
                                       current_color)
                    your_money = your_money + (current_pet_mythical * 3)
                    save_player_data(player_data)

                elif mythical_pet >= 4:
                    print_colored_text("You Received " + str(current_pet_mythical) + " from mythical pet",
                                       current_color)
                    your_money = your_money + (current_pet_mythical * 4)
                    save_player_data(player_data)

                if unknown_pet == 1:
                    print_colored_text("You Received " + str(current_pet_unknown) + " from unknown pet",
                                       current_color)
                    your_money = your_money + current_pet_unknown
                    save_player_data(player_data)
                elif uncommon_pet == 2:
                    print_colored_text("You Received " + str(current_pet_unknown) + " from unknown pet",
                                       current_color)
                    your_money = your_money + (current_pet_unknown * 2)
                    save_player_data(player_data)
                elif unknown_pet == 3:
                    print_colored_text("You Received " + str(current_pet_unknown) + " from unknown pet",
                                       current_color)
                    your_money = your_money + (current_pet_unknown * 3)
                    save_player_data(player_data)
                elif unknown_pet == 4:
                    print_colored_text("You Received " + str(current_pet_unknown) + " from unknown pet",
                                       current_color)
                    your_money = your_money + (current_pet_unknown * 4)
                    save_player_data(player_data)
                elif unknown_pet >= 5:
                    print_colored_text("You Received " + str(current_pet_unknown) + " from unknown pet",
                                       current_color)
                    your_money = your_money + (current_pet_unknown * 5)
                    save_player_data(player_data)
                if secret_pet == 1:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + current_pet_secret
                    save_player_data(player_data)
                elif uncommon_pet == 2:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret*2)
                    save_player_data(player_data)

                elif secret_pet == 3:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret * 3)
                    save_player_data(player_data)
                elif secret_pet == 4:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret * 4)
                    save_player_data(player_data)
                elif secret_pet == 5:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret * 5)
                    save_player_data(player_data)
                elif secret_pet == 6:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret * 6)
                    save_player_data(player_data)
                elif secret_pet >= 7:
                    print_colored_text("You Received " + str(current_pet_secret) + " from secret pet",
                                       current_color)
                    your_money = your_money + (current_pet_secret * 7)
                    save_player_data(player_data)

        elif f_answer.lower() == "check balance":
            print_colored_text("\ndo you wish to check your balance?", current_color)
            balance_check = str(input("Yes or No?: "))
            save_player_data(player_data)
            if balance_check.lower() == "yes":
                print_colored_text("your balance is: " + str(your_money), current_color)
                save_player_data(player_data)
                time.sleep(2)
                continue
        elif f_answer.lower() == "upgrade":
            print_colored_text("do you want to upgrade?", current_color)
            print_colored_text("Cost: " + str(upgrade), current_color)
            answer4 = str(input("yes or no?: "))
            save_player_data(player_data)
            if answer4.lower() == "yes":
                if your_money < upgrade:
                    print_colored_text("you're out of money...", current_color)
                    save_player_data(player_data)
                    continue
                elif your_money >= upgrade:
                    print_colored_text("upgrade successfully!", current_color)
                    your_money = your_money - upgrade
                    upgrade *= 4
                    upgrade_stats +=1
                    save_player_data(player_data)
                    continue
            elif answer4.lower() == "no":
                save_player_data(player_data)
                time.sleep(1)
                continue
        elif f_answer == "trade":
            triggered = 1
            answer5 = str(input("Do you want to enter the trade shop?: "))
            save_player_data(player_data)
            if answer5.lower() == "yes":
                print_colored_text("\nWelcome to Ore shop! How can i help you?"
                                   "\ntype 'all' to trade all your ores", current_color)
                print_colored_text("A. Ordinary Ore ($300)"
                      "\nB. Uncommon Ore ($700)"
                      "\nC. Epic Ore ($1200)"
                      "\nD. Legendary Ore ($1900)"
                      "\nE. Mythical Ore ($3500)", current_color)
                answer6 = str(input("Choose: ")).lower()
                save_player_data(player_data)
                if answer6 == "a":
                    if ordinary_ore >= 1:
                        ordinary_ore -= 1
                        your_money += 300
                        print_colored_text("Thank you for trading!", current_color)
                        save_player_data(player_data)
                    elif ordinary_ore <= 0:
                        print_colored_text("sorry, you dont have ordinary ore", current_color)
                        save_player_data(player_data)
                elif answer6 == "b":
                    if uncommon_ore >= 1:
                        uncommon_ore -= 1
                        your_money += 700
                        print_colored_text("Thank you for trading!", current_color)
                        save_player_data(player_data)
                    elif uncommon_ore <= 0:
                        print_colored_text("sorry, you dont have uncommon ore", current_color)
                        save_player_data(player_data)
                elif answer6 == "c":
                    if epic_ore >= 1:
                        epic_ore -= 1
                        your_money += 1200
                        print_colored_text("Thank you for trading!", current_color)
                        save_player_data(player_data)
                    elif epic_ore <= 0:
                        print_colored_text("sorry, you dont have epic ore", current_color)
                        save_player_data(player_data)
                elif answer6 == "d":
                    if legendary_ore >= 1:
                        legendary_ore -= 1
                        your_money += 1900
                        print_colored_text("Thank you for trading!", current_color)
                        save_player_data(player_data)
                    elif legendary_ore <= 0:
                        print_colored_text("sorry, you dont have legendary ore", current_color)
                        save_player_data(player_data)
                elif answer6 == "e":
                    if mythical_ore >= 1:
                        mythical_ore -= 1
                        your_money += 3500
                        print_colored_text("Thank you for trading!", current_color)
                        save_player_data(player_data)
                    elif mythical_ore <= 0:
                        print_colored_text("sorry, you dont have uncommon ore", current_color)
                        save_player_data(player_data)
                elif answer6 == "all":
                    trade_all_ores()

        elif f_answer.lower() == "check balance":
            print_colored_text("\ndo you wish to check your balance?", current_color)
            balance_check = str(input("Yes or No?: "))
            save_player_data(player_data)
            if balance_check.lower() == "yes":
                print_colored_text("your balance is: " + str(your_money), current_color)
                save_player_data(player_data)
                time.sleep(2)
        elif f_answer.lower() == "upgrade":
            triggered = 0
            if upgrade_stats == 10:
                print_colored_text("do you want to upgrade?", current_color)
                save_player_data(player_data)
                answer4 = str(input("Cost: " + str(upgrade)))
                if answer4.lower() == "yes":
                    if your_money <= upgrade:
                        print_colored_text("you're out of money...", current_color)
                        save_player_data(player_data)
                    elif your_money >= upgrade:
                        print_colored_text("upgrade successfully!",current_color)
                        your_money = your_money - upgrade
                        upgrade *= 4
                        upgrade_stats += 1
                        save_player_data(player_data)
                elif answer4.lower() == "no":
                    save_player_data(player_data)
                    time.sleep(1)
            elif upgrade_stats == 25:
                print_colored_text("do you want to upgrade?", current_color)
                answer4 = str(input("Cost: " + str(upgrade)))
                save_player_data(player_data)
                if answer4.lower() == "yes":
                    save_player_data(player_data)
                    if your_money <= upgrade:
                        print_colored_text("you're out of money...", current_color)
                        save_player_data(player_data)
                    elif your_money >= upgrade:
                        print_colored_text("upgrade successfully!", current_color)
                        your_money = your_money - upgrade
                        upgrade *= 8
                        upgrade_stats += 1
                        save_player_data(player_data)
                elif answer4.lower() == "no":
                    save_player_data(player_data)
                    time.sleep(1)
            elif upgrade_stats == 50:
                print_colored_text("do you want to upgrade?", current_color)
                answer4 = str(input("Cost: " + str(upgrade)))
                save_player_data(player_data)
                if answer4.lower() == "yes":
                    save_player_data(player_data)
                    if your_money <= upgrade:
                        print_colored_text("you're out of money...", current_color)
                        save_player_data(player_data)
                    elif your_money >= upgrade:
                        print_colored_text("upgrade successfully!", current_color)
                        your_money = your_money - upgrade
                        upgrade *= 10
                        upgrade_stats += 1
                        save_player_data(player_data)
                elif answer4.lower() == "no":
                    save_player_data(player_data)
                    time.sleep(1)
            elif upgrade_stats == 100:
                print_colored_text("do you want to upgrade?", current_color)
                answer4 = str(input("Cost: " + str(upgrade)))
                save_player_data(player_data)
                if answer4.lower() == "yes":
                    save_player_data(player_data)
                    if your_money <= upgrade:
                        print_colored_text("you're out of money...", current_color)
                        save_player_data(player_data)
                    elif your_money >= upgrade:
                        print_colored_text("upgrade successfully!", current_color)
                        your_money = your_money - upgrade
                        upgrade *= 15
                        upgrade_stats += 1
                        save_player_data(player_data)
                elif answer4.lower() == "no":
                    save_player_data(player_data)
                    time.sleep(1)
            else:
                print_colored_text("do you want to upgrade?", current_color)
                answer4 = str(input("Cost: " + str(upgrade)))
                if answer4.lower() == "yes":
                    save_player_data(player_data)
                    if your_money < upgrade:
                        print_colored_text("you're out of money...", current_color)
                        save_player_data(player_data)
                    elif your_money >= upgrade:
                        print_colored_text("upgrade successfully!", current_color)
                        your_money = your_money - upgrade
                        upgrade *= 1.5
                        upgrade_stats += 1
                        save_player_data(player_data)
                elif answer4.lower() == "no":
                    time.sleep(1)
                    save_player_data(player_data)
        elif f_answer.lower() == "help":
            triggered = 1
            if instruction == 0:
                print_colored_text("\n\nINSTRUCTIONS: "
                      "\nin this game you just need to type 'Yes' or 'No' to spin an get money!."
                      "\nif you're out of spin. you can buy more spin to get more money!"
                      "\nupgrade more! for more commands/help"
                      "\nType 'next' to see all commands! Type 'exit' to go back to game!", current_color)
                save_player_data(player_data)
                answer7 = str(input("Your Answer: "))
                if answer7.lower() == "next":
                    save_player_data(player_data)
                    instruction += 1
                    if instruction == 1:
                        print_colored_text("All Commands/Help"
                              "\n1. trade - to trade our ore you've got to get more money!"
                              "\n2. upgrade - to upgrade your stats and gain more money"
                              "\n3. help - to see instruction and commands"
                              "\n4. balance - to check what's your money left!"
                              "\n5. Pet - to hatch pet!"
                              "\n6. bag - to check your current ore"
                              "\n7. shop - to buy some discounted spin!"
                              "\n8. check score - to see what's your latest score as of now"
                              "\n9. rebirth - to earned more money!"
                              "\n10. color - to change your color"
                              "\n11. save - to save your progress manually!"
                              "\n12. reset - to reset your progress back to 0", current_color)
                        exit_help = str(input("exit? (Yes): "))
                        save_player_data(player_data)
                        if exit_help.lower() == "yes":
                            instruction = 0
                            save_player_data(player_data)
                elif answer7.lower() == "exit":
                    instruction = 0
                    save_player_data(player_data)
        elif f_answer.lower() == "shop":
            triggered = 1
            shop_discount_ten_spin = (shop_cost + 1000) * 0.2
            shop_discount_twenty_spin = (shop_cost + 2000) * 0.4
            shop_spin_cost = shop_cost + 4000
            shop_spin_cost_five = shop_cost + (4000 * 5)
            shop_spin_cost_ten = shop_cost + (4000 * 10)
            print_colored_text("\nWelcome to Shop! Buy any item below!"
                  "\nA. Buy 10x Spin! ($" + str(shop_discount_ten_spin) + ")(20% off!)"
                                                                          "\nB. Buy 20x Spin! ($" + str(shop_discount_twenty_spin) + ")(40% off!) (BEST OFFER!)"
                                                                                                                                     "\nC. Auto spin ($65,500)", current_color)
            buy_item = str(input("Your choice (pick number or exit): "))
            save_player_data(player_data)
            if buy_item.lower() == "a":
                save_player_data(player_data)
                answer8 = str(input("you sure you want to buy 10x spin?: "))
                if answer8 == "yes":
                    if your_money >= shop_discount_ten_spin:
                        your_money = your_money - shop_discount_ten_spin
                        shop_cost *= 12
                        spin_left += 10
                        save_player_data(player_data)
                        print_colored_text("Successfully purchased!", current_color)
                    elif your_money < shop_discount_ten_spin:
                        print_colored_text("insufficient amount of money: ", current_color)
                        save_player_data(player_data)
                else:
                    save_player_data(player_data)
                    continue
            elif buy_item.lower() == "b":
                answer9 = str(input("you sure you want to buy 20x spin?: "))
                if answer9 == "yes":
                    if your_money >= shop_discount_twenty_spin:
                        your_money = your_money - shop_discount_twenty_spin
                        shop_cost *= 17
                        spin_left += 20
                        print_colored_text("Successfully purchased!", current_color)
                        save_player_data(player_data)
                    elif your_money < shop_discount_twenty_spin:
                        print_colored_text("insufficient amount of money", current_color)
                        save_player_data(player_data)
                else:
                    continue
            elif buy_item.lower() == "c":
                answer10 = str(input("Would you like to buy Auto spin?: "))
                if answer10 == "yes":
                    if your_money >= 65500:
                        your_money -= 65500
                        print("Succefully purchased!")
                        automatic_spin_triggered = 1
                    elif your_money < 65500:
                        print("insufficient amount of money!")
                elif answer10 == 'no':
                    continue
            elif buy_item.lower() == "exit":
                save_player_data(player_data)
                continue
                # -------------------------------------------------------------------------------------------
        elif f_answer == "pet":
            triggered = 1
            pet_answer = str(input("Do you want to enter pet?: "))
            if pet_answer.lower() == "yes":
                print_colored_text("\nWelcome To Pet Shop! Do you wish to buy pets", current_color)
                print_colored_text(f"Cost: {pet_cost} (buy/exit)"
                      "\nPet cost 3.5x every purchase",current_color)
                save_player_data(player_data)
                pet_hatch_exit = str(input("Your Choice: "))
                if pet_hatch_exit == "buy":
                    if your_money >= pet_cost:
                        random_chance = random.random()
                        save_player_data(player_data)
                        if random_chance <= common_pet_probability / (common_pet_probability + uncommon_pet_probability):
                            print_colored_text("You got common pet!", current_color)
                            your_money = your_money - pet_cost
                            common_pet += 1
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        elif random_chance <= (common_pet_probability + uncommon_pet_probability) / (common_pet_probability + uncommon_pet_probability + epic_pet_probability):
                            print_colored_text("You got uncommon pet!", current_color)
                            uncommon_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        elif random_chance <= (common_pet_probability + uncommon_pet_probability + epic_pet_probability) / (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability):
                            print_colored_text("You got epic pet! wow!", current_color)
                            epic_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        elif random_chance <= (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability) / (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability + mythical_pet_probability):
                            print_colored_text("You got legendary pet! Awesome! Congrats", current_color)
                            uncommon_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        elif random_chance <= (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability + mythical_pet_probability) / (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability + mythical_pet_probability + unknown_pet_probability):
                            print_colored_text("OMG! You got mythical pet! VERY LUCKY", current_color)
                            mythical_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        elif random_chance <= (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability + mythical_pet_probability + unknown_pet_probability) / (common_pet_probability + uncommon_pet_probability + epic_pet_probability + legendary_pet_probability + mythical_pet_probability + unknown_pet_probability + secret_pet_probability):
                            print_colored_text("You got unknown pet! how?? who's this unknown?", current_color)
                            unknown_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                        else:
                            print_colored_text("You got secret pet! OMG. YOU'RE VERY LUCKY! CONGRATULATIONS!", current_color)
                            secret_pet += 1
                            your_money = your_money - pet_cost
                            pet_cost *= 3.5
                            save_player_data(player_data)
                    elif your_money < pet_cost:
                        print("insufficient amount of money")
                        save_player_data(player_data)
        elif f_answer == "stats":
            print(f"current score: {score}") #input all the stats needed
            cost = 100
            shop_cost = 100
            upgrade = 100
            upgrade_stats = 0
            rebirth_cost = 15600
            rebirth_count = 0
            pet_cost = 1500

            
        elif f_answer == "check score":
            triggered = 1
            check_score = str(input("Do you wish to check score?: "))
            if check_score.lower() == "yes":
                save_player_data(player_data)
                print_colored_text(f"Your Score: {score}", current_color)
            elif check_score.lower() == "no":
                save_player_data(player_data)
                continue
        #this can triggered the pet bonuses every spin and disabled the bonuses when entering any
        if (common_pet >= 1) or (uncommon_pet >= 1) or (epic_pet >= 1) or (legendary_pet >= 1) or (mythical_pet >= 1) or (uncommon_pet >= 1) or (secret_pet >= 1):
            pet_triggered = 1
            save_player_data(player_data)
            # Spin
        if spin_left <= 0:
            while spin_left == 0:
                pet_triggered = 1
                print_colored_text(f"You're out of spin. Do you wish to buy 3 more?", current_color)
                print_colored_text(f"3 spin cost: " + str(cost), current_color)
                answer = str(input("Yes or No?: "))
                if answer.lower() == "yes":
                    if your_money < cost:
                        print_colored_text("you're out of money", current_color)
                        time.sleep(1)
                        save_player_data(player_data)
                        if 0 <= score <= 50:
                            print_colored_text("Congratulation! You scored: " + str(score), current_color)
                            restart_game()
                            exit()
                        elif 51 <= score <= 120:
                            print_colored_text("WOW! you scored: " + str(score) + "! Congrats!", current_color)
                            restart_game()
                            exit()
                        elif 121 <= score <= 300:
                            print_colored_text("OMG! you scored: " + str(score) + "! How?",current_color)
                            restart_game()
                            exit()
                        elif 301 <= score <= 600:
                            print_colored_text("HOW????? YOU'RE GOD! you've scored: " + str(score) + "!", current_color)
                            restart_game()
                            exit()
                        elif 601 <= score <= 1000:
                            print_colored_text("impossible.... you've scored: " + str(score) + "! HOW!?!?!?!", current_color)
                            restart_game()
                            exit()
                        elif score >= 1001:
                            print_colored_text("YOUR CHEATING!", current_color)
                            restart_game()
                            exit()
                    elif your_money >= cost:
                        print_colored_text(f"You've Purchased a 3 spin!", current_color)
                        your_money = your_money - cost
                        spin_left = 3
                        cost *= 2.5
                        print_colored_text("the cost has increased! latest cost: " + str(cost), current_color)
                        save_player_data(player_data)
                        break
                elif answer.lower() == "no":
                    if 0 <= score <= 50:
                        print_colored_text("Congratulation! You scored: " + str(score), current_color)
                        restart_game()
                        exit()
                    elif 51 <= score <= 120:
                        print_colored_text("WOW! you scored: " + str(score) + "! Congrats!", current_color)
                        restart_game()
                        exit()
                    elif 121 <= score <= 300:
                        print_colored_text("OMG! you scored: " + str(score) + "! How?", current_color)
                        restart_game()
                        exit()
                    elif 301 <= score <= 600:
                        print_colored_text("HOW????? YOU'RE GOD! you've scored: " + str(score) + "!", current_color)
                        restart_game()
                        exit()
                    elif 601 <= score <= 1000:
                        print_colored_text("impossible.... you've scored: " + str(score) + "! HOW!?!?!?!", current_color)
                        restart_game()
                        exit()
                    elif score >= 1001:
                        print_colored_text("YOUR CHEATING!", current_color)
                        restart_game()
                        exit()
                else:
                    print_colored_text("Invalid input. Please type 'Yes' or 'No'", current_color)
        if upgrade_stats == 10:
            print_colored_text("You have entered the beginning...", current_color)
            save_player_data(player_data)
        elif upgrade_stats == 25:
            print_colored_text("You have entered the hard phase...", current_color)
            save_player_data(player_data)
        elif upgrade_stats == 50:
            print(RED + "You have entered the Insane phase..." + DEFAULT)
            print(YELLOW + "You Have Unlocked the Bonus money!" + DEFAULT)
            save_player_data(player_data)
        elif upgrade_stats == 100:
            print(BLACK +"You have entered the Impossible phase... Goodluck!" + DEFAULT)
            save_player_data(player_data)
        elif upgrade_stats == 200:
            print_colored_text("You have entered to... DsGsadfgsdfgsfgags.... becareful it's almost impossible...", current_color)
            save_player_data(player_data)
            print("You've reached maximum level of stats! if you still upgrade more, it's to you. it wont add your stats")
        elif f_answer == "bag":
            triggered = 1
            bag_qst = str(input("\nWould you like to see your inventory?(Yes/No): "))
            if bag_qst.lower() == "yes":
                print_colored_text(f"Ordinary Ore = {ordinary_ore}", current_color)
                print_colored_text(f"Uncommon Ore = {uncommon_ore}", current_color)
                print_colored_text(f"Epic Ore = {epic_ore}", current_color)
                print_colored_text(f"Legendary Ore = {legendary_ore}", current_color)
                print_colored_text(f"Mythical Ore = {mythical_ore}",current_color)
                bag_return = str(input("type exit to return game: "))
                save_player_data(player_data)
                if bag_return.lower() == "exit":
                    save_player_data(player_data)
                    continue
        elif f_answer == "check pet":
            pet_triggered = 0
            triggered = 1
            check_pet = str(input("Do you want to check your pet?: "))
            if check_pet.lower() == 'yes':
                print_colored_text(f"Common Pet = {common_pet}", current_color)
                print_colored_text(f"Uncommon Pet = {uncommon_pet}", current_color)
                print_colored_text(f"Epic Pet = {epic_pet}", current_color)
                print_colored_text(f"Legendary Pet = {legendary_pet}", current_color)
                print_colored_text(f"Mythical Pet = {mythical_pet}", current_color)
                print_colored_text(f"Unknown Pet = {unknown_pet}", current_color)
                print_colored_text(f"Secret Pet = {secret_pet}", current_color)
                exit_check_pet = str(input("Type exit to return to the game: "))
                save_player_data(player_data)
                if exit_check_pet == "yes":
                    continue
            elif check_pet.lower() == "no":
                save_player_data(player_data)
                continue
        elif f_answer == "cheat":
            cheat = str(input("You're Entering the dangerous command! would you like to continue?: "))
            if cheat == "yes":
                print_colored_text("Cheat has been activated", current_color)
                cheat_triggered = 1
                save_player_data(player_data)
            elif cheat == "no":
                print_colored_text("The game has been secure!", current_color)
                save_player_data(player_data)
                continue
        elif f_answer == "secret help":
            print_colored_text("welcome to secret help command..."
                  "\nSecret Command helps you to win game automatically by cheating."
                  "\nTo start using cheat. type cheat in the middle of game!", current_color)
            exit_secret_help = str(input("Type exit to go back to game: "))
            if exit_secret_help == "exit":
                save_player_data(player_data)
                continue
        elif f_answer == "whats new":
            print_colored_text("What's new?"
                  "\nv0.7.1 - added secret and refix commands"
                  "\nv0.7.2 - pet probability fix and bug fix"
                  "\nv0.7.3 - renew intro section"
                  "\nv0.7.4 - added new in upgrade stats"
                  "\nv0.7.5 - added whats new command"
                  "\nv0.7.6 - fixed bug and added rebirth!"
                  "\nv0.7.7 - re-fixed and fixed bug"
                  "\nv0.7.8 - updated whats new and fixed more bugs"
                  "\nv0.7.9 - updated intro section"
                  "\nv0.8.0 - fixed bug"
                  "\nv0.8.1 - updated new score!"
                  "\nv0.8.2 - Rebirth Added!"
                  "\nv0.8.3 - updated rebirth cost"
                  "\nv0.8.4 - probability updated!"
                  "\nv0.8.5 - Bug Fixed"
                  "\nv0.8.6 - Login added!"
                  "\nv0.8.7 - Login Fixed and progress updated!"
                  "\nv0.8.8 - Color added!"
                  "\nv0.8.9 - input color fixed!"
                  "\nv0.9.0 - pet bonuses updated"
                               "\nv0.9.1 - reset has added! to reset your progress!"
                               "\nv0.9.2 - New Loading Progress!"
                               "\nv0.9.3 - New Menu and better look!"
                               "\nv0.9.4 - priced increased! Difficulty increased!"
                               "\nv0.9.5 - added spin capacity!"
                               "\nv0.9.6 - capacity bug fixed!"
                               "\nv0.9.7 - stats updated! added more stats"
                               "\nv0.9.8 - trade ore! you can trade all ore's in one go!"
                               "\nv0.9.9 - New auto spin added!"
                               "\nv1.0.0 - Bug Fixed and money update!", current_color)
            exit_whats_new = str(input("type exit to return back to game: "))
            if exit_whats_new == "exit":
                save_player_data(player_data)
                continue
        if cheat_triggered == 1:
            if f_answer == "custom gold":
                custom_gold = int(input("input any amount of gold: "))
                your_money = custom_gold
                print("Gold Has Change")
                save_player_data(player_data)
            elif f_answer == "custom spin":
                custom_spin = int(input("Input any amount of spin: "))
                spin_left = custom_spin
                print("Spin Has Change")
                save_player_data(player_data)
            elif f_answer == "custom ore":
                custom_ore = int(input("Select ore"
                                       "\n1. ordinary ore"
                                       "\n2. uncommon ore"
                                       "\n3. epic ore"
                                       "\n4. legendary ore "
                                       "\n5. mythical ore"))
                if custom_ore == 1:
                    custom_ore_ordinary = int(input("Input any amount: "))
                    ordinary_ore = custom_ore_ordinary
                    print("Ore Has Changed")
                    save_player_data(player_data)
                elif custom_ore == 2:
                    custom_ore_uncommon = int(input("Input any amount: "))
                    uncommon_ore = custom_ore_uncommon
                    print("Ore Has Changed")
                    save_player_data(player_data)
                elif custom_ore == 3:
                    custom_ore_epic = int(input("Input any amount "))
                    epic_ore = custom_ore_epic
                    print("Ore Has Changed")
                    save_player_data(player_data)
                elif custom_ore == 4:
                    custom_ore_legendary = int(input("Input any amount: "))
                    legendary_ore = custom_ore_legendary
                    print("Ore Has Changed")
                    save_player_data(player_data)
                elif custom_ore == 5:
                    custom_ore_mythical = int(input("Input any amount: "))
                    mythical_ore = custom_ore_mythical
                    print("Ore Has Changed")
                    save_player_data(player_data)
            elif f_answer == "custom pet":
                custom_pet = str(input("Input what type of pet"))
                if custom_pet == "common pet":
                    custom_pet_common = int(input("Input any amount: "))
                    common_pet = custom_pet_common
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "uncommon pet":
                    custom_pet_uncommon = int(input("Input any amount: "))
                    uncommon_pet = custom_pet_uncommon
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "epic pet":
                    custom_pet_epic = int(input("Input any amount: "))
                    epic_pet += custom_pet_epic
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "legendary pet":
                    custom_pet_legendary = int(input("Input any amount: "))
                    legendary_pet = custom_pet_legendary
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "mythical pet":
                    custom_pet_mythical = int(input("Input any amount: "))
                    mythical_pet = custom_pet_mythical
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "unknown pet":
                    custom_pet_unknown = int(input("Input any amount: "))
                    unknown_pet = custom_pet_unknown
                    print("Pet Has Changed")
                    save_player_data(player_data)
                elif custom_pet == "secret pet":
                    custom_pet_secret = int(input("Input any amount: "))
                    secret_pet = custom_pet_secret
                    print("Pet Has Changed")
                    save_player_data(player_data)
            elif f_answer == "custom stats":
                custom_stats = int(input("Input any amount: "))
                upgrade_stats = custom_stats
                print("Stats Has Changed")
                save_player_data(player_data)
        if f_answer.lower() == "rebirth":
            print_colored_text("Do you want to rebirth?", current_color)
            print_colored_text(f"Rebirth Cost: {rebirth_cost}", current_color)
            answer_rebirth = str(input("Yes or No?: "))
            if answer_rebirth == "yes":
                if your_money >= rebirth_cost:
                    your_money -= rebirth_cost
                    rebirth_count += 1
                    print_colored_text(f"Congratulations! You have been reborn. Rebirth Count: {rebirth_count}", current_color)
                    money_multiplier *= 1.2
                    upgrade_cost_multiplier *= 1.5
                    upgrade = int(upgrade * upgrade_cost_multiplier)
                    your_money = int(your_money + (your_money * money_multiplier))
                    cost = int(cost * upgrade_cost_multiplier)
                    rebirth_cost *= 3
                    score = 0
                    spin_left = 3
                    upgrade_stats = 0
                    ordinary_ore = 0
                    uncommon_ore = 0
                    epic_ore = 0
                    legendary_ore = 0
                    mythical_ore = 0
                    triggered = 0
                    pet_triggered = 1
                    common_pet = 0
                    uncommon_pet = 0
                    epic_pet = 0
                    legendary_pet = 0
                    mythical_pet = 0
                    unknown_pet = 0
                    secret_pet = 0
                    latest_number_spin = 0
                    rebirth_cost *= 2
                    print_colored_text(
                        f"You have a fresh start with rebirth bonuses! Money Multiplier: {money_multiplier}, Upgrade Cost Multiplier: {upgrade_cost_multiplier}", current_color)
                    save_player_data(player_data)
                elif your_money < rebirth_cost:
                    print_colored_text("insufficient amount of money", current_color)
                    continue
        else:
            time.sleep(1)

        if f_answer == "save":
            save_game = str(input("Would you like to save you game?: ")).lower()
            if save_game == "yes":
                print_colored_text(f"the game has saved! player name: {player_name}", current_color)
                save_player_data(player_data)
            else:
                continue
        if f_answer == "auto":
            spin_auto_qt = str(input("would you like to spin automatically?: "))
            if spin_auto_qt == 'yes':
                if automatic_spin_triggered == 1:
                    auto_spin()
                elif automatic_spin_triggered == 0:
                    print("You dont have auto spin. Please purchase in the store!")
            elif spin_auto_qt == 'no':
                save_player_data(player_data)
                continue

        if f_answer == "no":
            play_again = input("Are you sure you want to exit? (yes/no): ")
            if play_again == "no":
                continue
            elif play_again.lower() == "yes":
                print_colored_text("Thanks for playing!", current_color)
                with open(f'{player_name}.json', 'w') as f:
                    json.dump(player_data, f)
                exit()
            else:
                print_colored_text("Sorry, I didn't understand that. Please answer 'yes' or 'no'.", current_color)
        if spin_left == 0 and your_money < cost:
            print("you're out of money! the game is closed!")
            time.sleep(2)
            print("Resetting your progress!")
            time.sleep(2)
            print("Resetting...")
            time.sleep(5)
            print(f"The Progress has been reset! Name: {player_name}")
            restart_game()
        if f_answer == "color":
            print("What color would you like to change?")
            change_color = str(input("(blue, default, green, red, orange, yellow, violet): ")).lower()
            print_colored_text("Color has changed!", change_color)
            current_color = change_color
        if f_answer == "reset":
            reset_confirmation = str(input("Are you sure you want to reset your progress? (Yes or No): ").lower())
            if reset_confirmation == "yes":
                restart_game()
                player_data = load_player_data(player_name)

                print("Progress has been reset.")
                continue
            else:
                print("Reset aborted.")
                continue