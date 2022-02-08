define f = Character("Florante")
define d = Character("Adolfo")
define m = Character("Menandro")
define kinatawan = Character("Kinatawan ng Krotona")
define l = Character("Laura")
define e = Character("Emir")
define go = Character("General Osmalik")
define gm = Character("General Miramolin")
define db = Character("Duke Briseo")
define hl = Character("Haring Linceo")
define g = Character("Gerry")

transform left:
    xalign 0.0
    yalign 1.0

transform right:
    xalign 1.0
    yalign 1.0

image Duke_Briseo_Palace_Day:
    zoom 0.75
    "images/Talata_5-8/Duke_Briseo_Palace_Day.png"

image Happy_Florante = im.FactorScale("images/Talata_5-8/florante_happy.png", 0.5)
image Happy_Florante_Reversed = im.Flip(im.FactorScale("images/Talata_5-8/florante_happy.png", 0.5), horizontal="True")

image Sad_Florante = im.FactorScale("images/Talata_5-8/florante_sad.png", 0.5)
image Sad_Florante_Reversed = im.Flip(im.FactorScale("images/Talata_5-8/florante_sad.png", 0.5), horizontal="True")


label Talata_5_through_8_script:

    g "Ayan na! Magsisimula na ang dulaan!"

    a "Ikaw Floranteng mang-aagaw dapat sayo'y mamatay!"

    g "Saklolo! Papatayin ni Adolfo si Florante!"

    m "Ikaw Adolfo, anon'g nangyari sayo? Nasisiraan ka na ba ng ulo? Ang pag-sasadula'y iyong tinotoo, hindi mo kailangan gawin ito."

    g "Salamat at niligtas mo si Florante! Ano nga pala pangalan mo at sino ang nagtangkang patayin si Florante?"

    m "Ako si Menandro, matalik kong kaibigan si Florante. Nakilala ko siya dahil ang aking tiyuhin ay ang guro ni Florante."

    m "Ang nagtangka naman sa buhay ni Florante ay si Adolfo. Inggit siya kay Florante sapagkat nalampasan ni Florante ang kanyang kakayahan sa loob lamang ng anim na taon."

    show Sad_Florante at right

    g "Bakit Florante? Ano'ng nangyari?"

    f "Ang aking ina'y pumanaw na."

    f "Oh mahal kong ina! Bakit mo ako iniwan? Ako'y hindi mo nakasama ang matagal." 
    f "Ama, pupunta riya't ika'y aking dadamayan."

    f "Ako'y magpapaalam sa inyo't nagpapasalamat. Nagpapasalamat sa lahat-lahat."

    scene Duke_Briseo_Palace_Day

    show Happy_Florante_Reversed at left

    db "Anak, huwag kang mawalan ng pag-asa Tadhana'y hindi basta-basta. Nandito kami't susuporta. Magiging gabay at tagapg-aruga."

    g "Magandang araw po, ako po si Gerry isang estudyante na inaaral ang inyong kwento."

    db "Magandang araw din sa iyo Gerry, ako naman si Duke Briseo. Ama ni Florante tagapayo ni Haring Linceo."

    db "May sulat na dumating mula sa Krotona humihingi ng tulong na kalabanin ang mga taga Persya na may intensyong manakop sa Krotona."


    hl "Ako si Haring Lince na taga Krotona. Ako ay nagagalak na kayo'y makilala at ito ang aking anak na si Laura."

    f "Masaya ako't nakilala kita. Sana tayo'y magkakilala pa ng lubos at maging magkaibigan o higit pa."

    hl "Ngayo'y araw ng pakikipagdigma at si Florante ay makikipaglaban para sa bayan."

    f "Laura ika'y maghihintay. Babalik ako at ika'y babalikan."

    l "Pangako, FLorante, ika'y aking hihintayin."

    g "Ano na ba kayo ni Florante, Laura?"

    l "Siya na ay ang aking kasintahan at lubos akong nalulungkot na siya'y aalis ngunit ang kanyang pangako ay aasahan na tuparin."


    g "Florante, sino siya?"

    f "Siya si Heneral Osmalik, isang heneral ng Persia."

    g "Mabuti na lang magaling ka makipagdigmaan Florante, nanalo ka pagkatapos ng limang oras."

    f "Mabuti nga na ganoon. Dito muna tayo sa Krotona ng limang buwan bago tayo bumalik upang masigurado na wala na ulit mananakop."

    "Makalipas ang limang buwan pagkatapos ng digmaan"

    g "Sa wakas tayo'y makakauwi na ulit sa Albanya pagkatapos ng matagal na panahon."

    f "Mabuti nga at makakabalik na ako sa aking minamahal na si Laura."

    f "Oh Laurang aking iniibig, ako'y nagbalik, Korotona'y aming naibalik. Sa kabutihan ito'y manunumbalik."

    l "Mabuti't ika'y nasa mabuting kalagayan. Ako'y nag-alala sa iyo't lagi kang pinagdarasal."

    l "Ngunit ngayo'y ika'y nasa aking piling. Maluwag na ang aking kalooba't nabunutan ng tinik."

    "Makalipas ang panahon, naging magaling na heneral si Florante at pabalik siya muli sa Albanya."

    g "Matagal ka na ring nakikipag digmaan Florante, mabuti nakakabalik tayo na normal ang laha- Florante! Tignan mo ang ALbanya! Iba na ang watawat!"

    f "Iyon ay di hamak na watawat ng Persia! Kailangan natin mailigtas ang aking ama, si Haring Linceo, at si Laura!"

    "Nailigtas ni Florante ang kanyang mga gustong mailigtas kasama na rin si Adolfo at binigyan ng titulong 'Tagapagtanggol ng Albanya'"

    g "Sino nanaman ang kalaban mo ngayon?"

    f "Siya si Heneral Miramolin, isang kilalang mananakop mula sa Turkiya."

    "Si Florante ay nakatanggap ng sulat mula sa kanyang ama na nagsasabing kailangan niya bumalik sa Albanya."

    g "Paano na ang digmaan? Sino ang maiiwan para manguna?"

    f "Iniwan ko ang pamumuno kay Menandro, ang aking matalik na kaibigan."



    g "Sa wakas andito na ulit tayo sa ALbanya."

    "Maraming kawal ang dumating at itinali at binugbog si Florante pagkatapos ay idinala sa bilangguan."

    g "Sino ang makakagawa sayo nito?"

    f "Sigurado akong si Adolfo ang may pakana nito. Ang mga kawal na pumalibot sa atin ay di hamak na kawal ni Adolfo."

    "Makalipas ang dalawampu't walong araw."

    g "Mahigit dalawampung araw na tayong bilanggo dito Florante, klailangan na natin tumakas."

    f "Ang aking ama at ang hari ay walang awang pinatay ni Adolfo, magbabayad siya sa ginawa niya."

    "Itinali muli si Florante at idinala sa kagubatan at itinali sa punong Higera."