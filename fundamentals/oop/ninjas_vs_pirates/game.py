from classes.ninja import Character
from classes.ninja import Ninja
from classes.ninja import Pirate

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")


print("Welcome to Ninjas vs. Pirates!\n")

choose = input("Please choose a character: press <n> for Ninja press <p> for Pirate. press <q> to Quit\n")

is_running = True

while is_running == True:
    if michelangelo.health <= 0 or jack_sparrow.health <= 0:
        is_running = False
    if choose == 'q':
        is_running = False
    
    elif choose == 'n':
        first_move = input("Your move! press <a> to attack press <m> to meditate.\n")

    elif choose =='p':
        first_move = input("Your move! press <a> to attack press <r> to drink rum.\n")

    if choose == "n" and first_move == "a":
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
        michelangelo.show_stats()
    elif choose == "n" and first_move == "m":
        michelangelo.meditate()
        jack_sparrow.show_stats()
        michelangelo.show_stats()
    elif choose == "p" and first_move == "a":
        jack_sparrow.attack(michelangelo)
        jack_sparrow.show_stats()
        michelangelo.show_stats()
    elif choose == "p" and first_move == "r":
        jack_sparrow.drink_rum()
        jack_sparrow.show_stats()
        michelangelo.show_stats()

print("GAME OVER")

