# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define Marco = Character("Marco")
define Florante = Character("Florante")
define Aladin = Character("Aladin")
define Liyon = Character("liyon")

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0


image Dark_Forest = "images/Talata_1-4/Dark_Forest.jpg"
image Classroom_flashback = "images/Talata_1-4/classroom_flashback.jpg"

image Neutral_Florante = im.FactorScale("images/Talata_1-4/Neutral_Florante.jpg", 0.5)
image Suprised_Florante = im.FactorScale("images/Talata_1-4/Suprised_Florante.jpg", 0.5)

image Florante_tied = im.FactorScale("images/Talata_1-4/florante_tied.jpg", 0.57)
image Florante_tied_Flipped = im.Flip(im.FactorScale("images/Talata_1-4/florante_tied.jpg", 0.75), horizontal="True")

image Neutral_Aladin = im.FactorScale("images/Talata_1-4/Neutral_Aladin.jpg", 0.5)
image Neutral_Aladin_Flipped = im.Flip(im.FactorScale("images/Talata_1-4/Neutral_Aladin.jpg", 0.5), horizontal="True")

image Suprised_Aladin = im.FactorScale("images/Talata_1-4/Suprised_Aladin.jpg", 0.5)
image Suprised_Aladin_Flipped = im.Flip(im.FactorScale("images/Talata_1-4/Suprised_Aladin.jpg", 0.5), horizontal="True")

define audio.lion_roar = "audio/Talata_1-4/565309__animadierer__lion-roar-snarl-growl-at013601.mp3"
define audio.sword_clash = "audio/Talata_1-4/440069__ethanchase7744__sword-block-combo.wav"
define audio.flash_back = "audio/Talata_1-4/Flashback.mp3"





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

    Marco "Ang dilim dito sa gubat at may naririnig akong malakas na iyak. Doon galing ang iyak na iyon."

    Florante "(Umiiyak)"

    show Florante_tied at right

    Marco "Anong pangalan mo at bakit nakatali ka sa puno ng Higera."

    Florante "Ako si Florante, anak ng isang prinsesa at ng isang tagapag-payong maharlika,
    at tinali ako ng mga kalaban ko dito sa puno ng Higera."

    Marco "Bakit ka umiiyak?"

    Florante  "Dahil nawala sa akin ang aking ama na si Duke Briseo at ninakawan ako."

    Marco "Nawalan ka ng ama at ninakawan ka? Ano ang ninakawan sa iyo?"

    Florante "Ang aking mahal na si Laura. Ang tao na gumawa nito ay ang aking kalaban na si Konde Adolfo."

    show Neutral_Aladin_Flipped at left

    Aladin "Dito pala ang pinanggagalingan ng malakas na iyak."

    Marco "S-sino ka?"

    Aladin "Ako si Aladin. Ako ay isang moro galing sa Persya."

    play sound lion_roar

    Liyon "(ungol)"

    Marco "M-may dalawang liyon nakarinig ‘rin sa iyo at mukhang nagugutom sila"

    hide Florante_tied at moveoutright

    hide Neutral_Aladin_Flipped

    show Neutral_Aladin_Flipped:
        left
        linear 1.0
        right
        "Suprised_Aladin"

    Aladin "(Humahanda para sa laban)"

    Aladin "Wag kayo mag alala, ako ang bahala dito"

    stop sound

    play sound sword_clash

    Aladin "(Mga ingay ng labanan)"

    stop sound

    hide Neutral_Aladin_Flipped

    Marco "Kung hindi dahil sa iyo si Florante ay kinain na ng mga leon pero mukhang nawalan ng malay itong si Florante."

    show Neutral_Aladin at right

    Aladin "Sige, ako na ang bahala kay Florante hanggang sa manumbalik ang lakas niya."

    hide Neutral_Aladin

    Florante "(gumigising)"

    show Suprised_Florante at right

    Florante "A-ano ang nangyari sa akin at bakit mayroong isang moro dito!?"

    show Neutral_Aladin_Flipped at left

    Aladin "Ako si Aladin at ako ang nagligtas sa iyo mula sa mga leon."

    Florante "Ah, ganoon ba? Maraming salamat. Pero hindi ako makapaniwala na isang moro ang nagligtas sa akin."

    hide Neutral_Aladin_Flipped

    Marco "Bakit?"

    hide Suprised_Florante

    show Neutral_Florante at right

    Florante "Dahil ang mga Kristiyano at Moro ay dapat na magkaaway."

    Florante "Hindi narin ito ang unang pagkakataon na malapit na akong mamatay."

    Florante "Noong bata pa ako, mayroon isang malaking uwak na nagtangkang dumagit sa batong hiyas na nasa aking dibdib."

    Florante "Kung hindi dahil sa aking pinsan na si Menalipo, mamatay na sana ako."

    Marco "Ganon ba? Ano pa ang nangyari noong bata ka pa."

    play sound flash_back

    Florante "(sinusubukang alalahanin)"

    show Classroom_flashback with fade

    stop sound

    Florante "Sa edad na 11, pinadala ako ng aking mga magulang na sina Duke Briseo at Prinsesa Floresca sa Atenas, Gresya."

    Florante "Ang dahilan ay upang makapag-aral sa ilalim ng kilalang guro na si Antenor.
    At doon ko na nakilala ang aking kalaban na si Adolfo."

    Florante "Si Adolfo ay mula din sa aking bayan dati siya ay ang pinakamatalinong mag-aaral sa paaralan noong panahon niya."

    Florante "Pero anim na taon pa lang at nalampasan ko na siya sa kakayahan, kagalingan at katalinuhan."

    Marco "Ano ang naging reaksyon ni Adolfo?"

    Florante "Dahil sa katanyagan at pagkilala na nakuha ko,
    hindi ikinatuwa ni Adolfo."




    # This ends the game.

    return
