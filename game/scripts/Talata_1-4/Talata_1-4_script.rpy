# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define m = Character("Marco")
define f = Character("Florante")
define a = Character("Aladin")
define l = Character("liyon")

image Dark_Forest = "images/Talata_1-4/Dark_Forest.jpg"

image Neutral_Florante = im.FactorScale("images/Talata_1-4/Neutral_Florante.jpg", 0.5)
image Suprised_Florante = im.FactorScale("images/Talata_1-4/Suprised_Florante.jpg", 0.5)

image Neutral_Aladin = im.FactorScale("images/Talata_1-4/Neutral_Aladin.jpg", 0.5)

image Neutral_Aladin_Flipped = im.Flip("images/Talata_1-4/Neutral_Aladin.jpg", horizontal="True")

define audio.lion_roar = "audio/Talata_1-4/565309__animadierer__lion-roar-snarl-growl-at013601.mp3"



# The game starts here.
label Talata_1_through_4_script:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Dark_Forest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "Ang dilim dito sa gubat at may naririnig akong malakas na iyak. Doon galing ang iyak na iyon."

    f "(crying)"

    m "Anong pangalan mo at bakit nakatali ka sa puno ng Higera."

    f "Ako si Florante, anak ng isang prinsesa at ng isang tagapag-payong maharlika,
    at tinali ako ng mga kalaban ko dito sa puno ng Higera."

    m "Bakit ka umiiyak?"

    f  "Dahil nawala sa akin ang aking ama na si Duke Briseo at ninakawan ako."

    m "Nawalan ka ng ama at ninakawan ka? Ano ang ninakawan sa iyo?"

    f "Ang aking mahal na si Laura. Ang tao na gumawa nito ay ang aking kalaban na si Konde Adolfo."

    show Neutral_Aladin:
        xalign 1.0
        yalign 1.25

    a "Dito pala ang pinanggagalingan ng malakas na iyak."

    m "S-sino ka?"

    a "Ako si Aladin. Ako ay isang moro galing sa Persya."

    play sound lion_roar

    l "(growling)"

    m "M-may dalawang liyon nakarinig ‘rin sa iyo at mukhang nagugutom sila"

    a "Wag kayo mag alala, ako ang bahala dito"

    stop sound

    a "(Battle noises)"

    m "Kung hindi dahil sa iyo si Florante ay kinain na ng mga leon pero mukhang nawalan ng malay itong si Florante."

    a "Sige, ako na ang bahala kay Florante hanggang sa manumbalik ang lakas niya."

    hide Neutral_Aladin

    f "(wakes up)"

    show Suprised_Florante:
        xalign 1.0
        yalign 1.25

    f "A-ano ang nangyari sa akin at bakit mayroong isang moro dito!?"

    show Neutral_Aladin_Flipped:
        zoom .50
        xalign -0.05
        yalign 1.25

    a "Ako si Aladin at ako ang nagligtas sa iyo mula sa mga leon."

    f "Ah, ganoon ba? Maraming salamat. Pero hindi ako makapaniwala na isang moro ang nagligtas sa akin."

    hide Neutral_Aladin_Flipped

    m "Bakit?"

    hide Suprised_Florante

    show Neutral_Florante:
        xalign 1.0
        yalign 1.25

    f "Dahil ang mga Kristiyano at Moro ay dapat na magkaaway."

    f "Hindi narin ito ang unang pagkakataon na malapit na akong mamatay."

    f "Noong bata pa ako, mayroon isang malaking uwak na nagtangkang dumagit sa batong hiyas na nasa aking dibdib."

    f "Kung hindi dahil sa aking pinsan na si Menalipo, mamatay na sana ako."

    m "Ganon ba? Ano pa ang nangyari noong bata ka pa."

    f "Sa edad na 11, pinadala ako ng aking mga magulang na sina Duke Briseo at Prinsesa Floresca sa Atenas, Gresya."

    f "Ang dahilan ay upang makapag-aral sa ilalim ng kilalang guro na si Antenor.
    At doon ko na nakilala ang aking kalaban na si Adolfo."

    f "Si Adolfo ay mula din sa aking bayan dati siya ay ang pinakamatalinong mag-aaral sa paaralan noong panahon niya."

    f "Pero anim na taon pa lang at nalampasan ko na siya sa kakayahan, kagalingan at katalinuhan."

    m "Ano ang naging reaksyon ni Adolfo?"

    f "Dahil sa katanyagan at pagkilala na nakuha ko,
    hindi ikinatuwa ni Adolfo."




    # This ends the game.

    return
