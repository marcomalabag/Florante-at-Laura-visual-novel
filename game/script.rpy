# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



label start:

    menu:
        "Talata 1 - 4":
            jump Talata_1_through_4_script

        "Talata 5 - 8":
            jump Talata_5_through_8_script

        "Talata 9 - 12":
            jump Talata_9_through_12_script


    # This ends the game.
    return
