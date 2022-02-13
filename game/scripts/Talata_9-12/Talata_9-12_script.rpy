define Florante = Character("Florante")
define Aladin = Character("Aladin")
define Adolfo = Character("Adolfo")
define Unknown = Character("Unknown")
define Flerida = Character("Flerida")
define Apl = Character("Apl")
define Marco = Character("Marco")
define Laura = Character("Laura")

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

image Dark_Forest = "images/Talata_1-4/Dark_Forest.jpg"
image Market:
    zoom .75
    "images/Talata_9-12/Market.jpg"

image Bazaar:
    zoom .70
    "images/Talata_9-12/Bazaar.jpg"


image BlackScreen:
    "images/Talata_9-12/Black_screen.jpg"

image Aladin_Suprised =  im.FactorScale("images/Talata_9-12/aladin_surprised.jpg", 0.5)
image Aladin_Suprised_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/aladin_surprised.jpg", 0.5), horizontal="True")

image Aladin_Neutral = im.FactorScale("images/Talata_9-12/Aladin_Neutral.jpg", 0.5)
image Aladin_Neutral_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Aladin_Neutral.jpg", 0.5), horizontal="True")

image Florante_Neutral = im.FactorScale("images/Talata_9-12/Neutral_Florante.jpg", 0.5)
image Florante_Neutral_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Neutral_Florante.jpg", 0.5), horizontal="True")

image Florante_Suprised = im.FactorScale("images/Talata_9-12/Suprised_Florante.jpg", 0.5)
image Florante_Suprised_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Suprised_Florante.jpg", 0.5), horizontal="True")

image Laura_Neutral = im.FactorScale("images/Talata_9-12/Neutral_Laura.jpg", 0.55)
image Laura_Neutral_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Neutral_Laura.jpg", 0.6), horizontal="True")

image Laura_Suprised = im.FactorScale("images/Talata_9-12/Suprised_Laura.jpg", 0.55)
image Laura_Suprised_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Suprised_Laura.jpg", 0.55), horizontal="True")

image Adolfo_Angry = im.FactorScale("images/Talata_9-12/Angry_Adolfo.jpg", 0.5)
image Adolfo_Angry_Reversed = im.Flip(im.FactorScale("images/Talata_9-12/Angry_Adolfo.jpg", 0.5), horizontal="True")



label Talata_9_through_12_script:

    scene Dark_Forest

    show Aladin_Suprised_Reversed at left

    Aladin "Naasan na ako…?"
    Aladin "Nakatakas na ako sa aking kaharian pero…"
    Aladin "Ang nakikita ko lang ay mga puno sa ibabaw pa ng mga puno"

    hide Aladin_Suprised

    Unknown "*soft noises*"

    show Aladin_Neutral_Reversed at left

    Aladin "…"
    Unknown "*audible cries*"
    Aladin "Parang mayroon akong naririnig na iyak"
    Unknown "*Loud cries*"
    Aladin "Sino ang dahilan sa lakas na iyak na ito?"
    Aladin "Kelangan ata niya ng tulong."

    hide Aladin_Neutral_Reversed

    show BlackScreen

    Apl "Sandali nga lang ang kwento"
    Apl "Kaso, saan nanggaling si Aladin at papaano siya nakarating sa gubat?"
    Apl "Mayroon akong narinig na kwento sa isang babae na siya’y nakatakas mula sa isang kaharian at sa kanyang sanang pagpapakasal."
    Apl "…"
    Apl "Palalim nang palalim ang kwento na ito."
    Apl "Hindi lamang tungkol kay Florante ang kwento na ‘to"
    Apl "Bawat isa sa mga tauhan ay may sariling buhay na nagbibigay daan para magsama-sama ang pinagmamahal nila."
    Apl "Tulad sa mga minamahal nina Florante at Aladin…"
    Apl "Si Laura, ang minamahal ni Florante at anak ni Haring Linceo"
    Apl "At ang babae na minamahal ni Aladin…anak ni Sultan Ali-Adab…"
    Apl "Si Flerida"

    scene Market

    Unknown "Hoy!"
    Unknown "Bakit mo minamaliitan ang isang babae!?"
    Unknown "May problema ka ba?"
    Unknown "Alis, lumayas ka na."

    Unknown "Ayos ka lang ba?"
    Unknown "Hindi ka ba nasaktan ng lalaki na nag aalipusta sa iyo?"

    show Laura_Neutral at right
    Laura "…"
    Unknown "Kung nasaktan ka… papakainin ko sa ka niya ang mga salita niya sa’yo."
    Laura "Ah, ayos lang ho ako"
    Unknown "…"
    Unknown "Halika, lumayo pa tayo sa kanya."

    scene Bazaar

    show Laura_Neutral at right

    Laura "Salamat ho"
    Laura "Hindi ko ho alam ang magagawa ko sa sitwasyon ko na iyon kung hindi ikaw tumulong sa akin"
    Unknown "Walang anuman"
    Laura "A-ano ho ang pangalan ninyo?"
    Flerida "Ako po si Flerida…"
    Laura "Flerida…"
    Laura "A-anak ni Sultan Ali-Adab!?"
    Flerida "Opo"
    Flerida "Ikaw, ano po ang iyong pangalan?"
    Laura "Ah, ako ho si Laura, anak ni Haring Linceo"
    Flerida "Si Haring Linceo!?…mukhang tayong dalawa ay nakatadhana ng magkita."

    show BlackScreen

    Apl "Pagkatapos sinagip ni Flerida si Laura"
    Apl "Matagal silang nag usap tungkol sa bawat isa"
    Apl "Tungkol sa kanilang kasintahan, relasyon nila kay Konde Adolfo, at iba pa."
    Apl "Kaso, hindi tumagal ang kanilang kasayahan dahil sa pagtagumpay ni Adolfo"
    Apl "Nahakop niya ang trono ng Albanya kung saan napilitang maging reyna si Laura."
    Apl "Ngunit…mayroong bumaliktad sa buhay ni Adolfo"
    Apl "At si Menandro, ang namumuno ng isang hukbo, ang dahilan sa pagkalupig kay Adolfo"
    Apl "Dahil roon, napatakas si Adolfo na tangay si Laura bihag patungo sa kagubatan -> held Laura as captive"

    scene Dark_Forest

    show Aladin_Neutral_Reversed at left

    Aladin "Mayroon kayo naririnig?"

    show Florante_Neutral at right

    Florante "Dahan-dahan ka lang Aladin, baka isa pa itong leon"

    hide Florante_Neutral

    hide Aladin_Neutral_Reversed

    show Florante_Suprised at right

    Florante "Adolfo!"


    show Aladin_Suprised_Reversed at left


    Aladin "Adolfo!?"

    hide Florante_Suprised

    show Laura_Suprised at right

    Laura "Florante!~"

    #show Laura

    hide Aladin_Suprised_Reversed

    hide Laura_Suprised

    #show Adolfo

    show Adolfo_Angry_Reversed at left

    Adolfo "Florante!?"

    show Florante_Suprised at right

    #show Laura

    Florante "Laura!"

    hide Adolfo_Angry_Reversed

    show Laura_Suprised_Reversed at left

    hide Florante_Suprised
    Marco "Marco!~"

    hide Laura_Suprised_Reversed

    show Florante_Suprised_Reversed at left


    Florante "A-ano ginagawa mo dito Adolfo at bakit kasama mo si Laura!?"

    #show Adolfo

    show Adolfo_Angry at right

    Adolfo "Nandito ako para tapusin ko ang dapat kong tinapos mula simula pa…"
    Adolfo "At ‘yon ay patayin ka!"

    show BlackScreen

    Apl "pagkatapos ng kanilang laban…"
    Apl "Nabatid nina Florante at Aladin ang kanilang pawang tapat sa kanila."

    #show future crowning

    Apl "Bumalik si Florante at Laura sa Albanya kung saan naging hari at reyna na sila"
    Apl "At tangi sa roon…"
    Apl "Nagbalik naman sina Aladin at Flerida sa Persya kung saan naging sultan si Aladin sapagkat sa pagkamatay ng kaniyan ama."
    Apl "Namuhay na muli ng mapayapa at matiwasay and dalawang kaharian."
    Apl "Dito nagtatapos ang kwentong Florante at Laura."
