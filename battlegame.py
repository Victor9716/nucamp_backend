wizard = "Wizard"
elf = "Elf"
human = "Human"

# hp of thier character
wizard_hp = 70
elf_hp = 100
human_hp = 20

# damage of each character
wizard_damage = 150
elf_damage = 100
human_damage = 150

#for dragon
dragon_hp = 300
dragon_damage = 50

# Task 2: prompt player

# infinite loop for character selection
while  True:
    #show character options
    print("Choose your character:")
    print("1.",  wizard)
    print("2.",  elf)
    print("3.",  human)

# Get user input for character choice
    character = input("> ")
    if character == "1":
        my_hp = wizard_hp
        my_damage = wizard_damage
        break #Exit the loop after selecting wizard
    elif character == "2":
        my_hp = elf_hp
        my_damage = elf_damage
        break # Exit the loop after selecting elf.
    elif character == "3":
        my_hp = human_hp
        my_damage = human_damage
        break # Exit the loop after selecting human
    else:
        print("Unknown character, please try again.")

print("You chose", character)
print("Your HP:", my_hp)
print("Your Damage: ", my_damage)

# battle loop
while  True:
    # player attack dragon
    dragon_hp -= my_damage
    print("The", character, "damaged the Dragon")

    # check if dragon is defeated
    if dragon_hp <= 0:
        print("the dragon has lost the battle!")
        break
    my_hp -= dragon_damage
    print("The Dragon attacked you! Your HP", my_hp)
    # Check if player is dead
    if my_hp <= 0:
        print("you have been killed by the Dragon!")
        break
    print("Game Over!!")





    



