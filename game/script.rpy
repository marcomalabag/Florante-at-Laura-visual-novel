# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Narrator = Character("Narrator", who_color="#3adde0")

image Opening_Scene:
    zoom .75
    "Opening Scene.jpg"



label start:

    scene Opening_Scene

    Narrator "Kumusta!~"

    Narrator "Ako ay si Apl, ang tagapagsalaysay sa inyo ngayon."

    Narrator "Hindi lamang ako ang sasama sa inyo."

    Narrator "Sasamahin kayo nina Marco at Gerry sa pagsalaysay mula sa loob ng kwento."

    Narrator "Tayo ngayon ay magsamasama sa awit ng..."

    Narrator "Florante at Laura."

    Narrator "Handa na ba kayo sa isang pakikipagsapalaran?"

    menu:
        "Talata 1 - 4":
            jump Talata_1_through_4_script

        "Talata 5 - 8":
            jump Talata_5_through_8_script

        "Talata 9 - 12":
            jump Talata_9_through_12_script


    # This ends the game.
    return
