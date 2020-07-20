image bird_move:
    "maps/office/office_bird.png"
    xpos 800 yalign .2
    linear 4 xpos renpy.random.randint(240,315) yalign .2
    pause 2
    xpos 800 yalign .2
    linear 4 xpos renpy.random.randint(260,353) yalign .3
    pause 2
    repeat


image office_fire:
    "maps/office/fire1.png" with dissolve
    .3
    "maps/office/fire2.png" with dissolve
    .3
    "maps/office/fire3.png" with dissolve
    .3
    "maps/office/fire4.png" with dissolve
    .3
    "maps/office/fire5.png" with dissolve
    .3
    repeat

default office_desk_loc = place("Desk", (421, 679), Jump('office_desk'), "maps/office/desk.png")
default office_weylon_loc = place("Weylon", (890, 620), Jump('office_weylon'), "maps/office/weylon.png")
default office_firecamp_loc = place("Fire Camp", (1395, 723), Jump('office_firecamp'), "maps/office/fireplace.png")
default office_picture_loc = place("Picture", (1352, 0), Jump('office_picture'), "maps/office/picture.png")
default office_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")
default office_fossil_loc = place("Fossil_fish", (1362, 533), Jump('office_fossil'), "maps/office/office_fossil.png")
default office_headhorn_loc = place("head_horn", (975, 202), Jump('office_horn'), "maps/office/office_horn_head.png")
default office_football_loc = place("football", (30, 928), Jump('office_football'), "maps/office/burn_office_football.png")
default office_book_loc = place("book", (76, 863), Jump('office_book'), "maps/office/office_book.png")
default office_fire_loc = place("fire", (0, 0), None, "office_fire")

default office_map = maps(
    "Office",
    [
        office_desk_loc,
        office_weylon_loc,
        office_firecamp_loc,
        office_picture_loc,
        office_arrow_loc,
        office_football_loc,
        office_headhorn_loc,
        office_fossil_loc,
        office_book_loc,
        office_fire_loc,


    ]
    )

label office:
    scene office bg
    show office_sky
    show bird_move
    show office_sky_wood
   # show office_fire
    show screen map(office_map)
    pause
    jump office

label office_desk:
    burn "This desk isn't for sale."
    jump office

label office_weylon:
    burn "How much would you pay for a Weylon?"
    jump office

label office_firecamp:
    burn "You can burn a body in it."
    burn "Wait a minute. . ."
    burn "There is something in here... why don't I remember what this is?... seem to be a entrance to somewhere in here"
    jump office

label office_picture:
    burn "Ah, yessss, my great grand dad! he's too expensive to sell yet"
    burn "I think I'll hold off for a while, there is still plenty of items around the mansion to sell"
    jump office

label office_horn:
    burn "Hmmm"
    burn "That's one scary looking horn"
    burn "I remember killing this beast with my own gun"
    burn "It took quite amount of HIT to take him down for good. . and get him crafted by the best craftman"
    burn "Might come back to pick it up later"
    burn "... but.. hold up. Why is his eyes red?"
    burn "I'm probably just hallucinating"
    jump office

label office_fossil:
    burn "My very own expensive Fossil"
    burn "It's pure and beautiful, just look at its NOSE it possess"
    burn "Too expensive for me to risk and sell this.. maybe I'll leave it alone for now . ."
    jump office

label office_football:
    burn "Ahh HA, a signed football"
    burn "This will definitly sell me some good price !"
    burn "Take this item plz, KIA."
    jump office

label office_book:
    burn "... useless"
    jump office
