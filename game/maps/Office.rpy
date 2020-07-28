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
        "office_sky",
        "bird_move",
        "office_sky_wood",
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
    show screen map(office_map)
    pause
    jump office

label office_desk:
    burn "This desk isn't for sale."
    jump office

label office_weylon:
    hide screen map
    scene office blur
    show weylon normal at right
    $ burns_face = "normal"
    show burn_base at left
    menu:
        "Ashley" if ashley_story == 1:
            burn "Weylon, I need some.... couple of help here"
            weylon "Yes, what do you need sir ?"
            burn "Well.. Ashley has some kind of issue with her pride of women rights and I don't really know what she needs"
            weylon "Women right ?"
            burn "... she asked to be a CEO and got rejected. HAHAHAHA"
            weylon "Oh, I see the problem"
            weylon "Sir, how about you offer her a position here at the desk?"
            burn "WHAT? That is out of questions ! "
            weylon "Well, I think it's a brilliant plan sir, you could trick her into thinking she is a official manager but isn't. Have her hunt for woman from the street as a job while pretending to act as a Manager"
            burn "hmpt !...... WELL...... I guess you are right.. ha"
            burn "But how will I... you know. Do unusual things with her.."
            weylon "You could have her meet a condition before she can get her offer"
            burn ".. hmm I like the sound of that, keep going"
            weylon "Have her do your activites that you desire, you know the little pleasure of immeasurable proportions"
            burn "HA, you know what I want, WAIT. Why do you know this.. ?"
            weylon "Hm.. welll. . . . *ahem* SIR, as I was saying, make her meet your coniditon. However if she show some sort of resistent and tries to do something like calling the cops, I have your back on that."
            weylon "We can lockdown the mansion and she wouldn't be able to call the police and have her gass out, and have her in your chamber if you have unlocked it already"
            burn "I like this, be sure you make no mistake Weylon"
            weylon "Yes, sir."
            burn "Now, I shall do my deeds"
            $ ashley_story += 1
            jump  office_weylon

        "Chamber door" if check_door == True:
            burn "WEYLON !"
            weylon "Yes ? do you need something sir ?"
            burn "Why don't I remember the thing in the chamber entrance ?"
            weylon "What thing. .? sir"
            burn "THE THING WEYLON"
            weylon "I'm sorry, but. . I do .n"
            burn "Weylon, don't make me go furious. I'm talking about the thing on the door that I can't seem to remember"
            weylon "*...the thing on the door ?.... OH right, now I see*"
            weylon "Sir, you mean your genius idea on the door that you seem to forgot about ?"
            burn "Yes"
            weylon "*...* You wanted to make three different shape which were diamonds. You need diamonds pieces to open the door"
            burn "Oh yes, now I remember"
            burn "Remind me what diamond I'm looking for.. again? . ."
            weylon "The red, green and blue diamond"
            burn "AHH yes , that's right. "
            jump office_weylon

        "Burn Sinister Head test":
            $ burns_accessory = "sinister"
            burn "..."
            weylon "*laughs*"
            $ burns_face = "normal_t"
            burn "wut"
            $ burns_face = "normal"
            weylon "U got a sinister on your head . "
            $ burns_face = "normal_t"
            burn "What....the"
            $ burns_face = "angry"
            burn "*wipes it off*"
            $ burns_face = "normal"
            $ burns_accessory = "none"
            $ burns_face = "normal_t"
            burn "ahem"
            
        "Nothing, weylon":
            jump office_weylon 
        "Leave":
            jump office


#    burn "How much would you pay for a Weylon?"
    jump office

label office_firecamp:
    # burn "You can burn a body in it."
    # burn "Wait a minute. . ."
    # burn "There is something in here... why don't I remember what this is?... seem to be a entrance to somewhere in here"
    jump chamber_entrance
   # jump office

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
    $ office_map.rem(office_football_loc)
    jump office

label office_book:
    burn "... useless"
    jump office
