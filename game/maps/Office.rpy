image bird_move:
    "maps/office/office_bird.png"
    xpos 800 yalign .2
    linear 7 xpos renpy.random.randint(280,315) yalign .2
    pause 2
    xpos 800 yalign .2
    linear 7 xpos renpy.random.randint(235,338) yalign .3
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
default office_ashley_loc = place("Ashley", (570, 601), Jump('office_ashley'), "maps/office/ashley office fig.png")
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
    if ashley_story == 12:
        $ office_map.discover(office_ashley_loc)
        $ ashley_story += 1


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
            $ burns_face = "normal_t"
            burn "Weylon, I need some.... couple of help here"
            $ burns_face = "normal"
            weylon "Yes, what do you need sir ?"
            $ burns_face = "hmm"
            burn "Well.. Ashley has some kind of issue with her pride of women rights and I don't really know what she needs"
            $ burns_face = "normal"
            weylon "Women right ?"
            $ burns_face = "laugh"
            burn "... she asked to be a CEO and got rejected. HAHAHAHA"
            $ burns_face = "normal"
            weylon "Oh, I see the problem"
            weylon "Sir, how about you offer her a position here at the desk?"
            $ burns_face = "angry_t"
            burn "WHAT? That is out of questions ! "
            $ burns_face = "angry"
            weylon "Well, I think it's a brilliant plan sir, you could trick her into thinking she is a official manager but isn't. Have her hunt for woman from the street as a job while pretending to act as a Manager"
            $ burns_face = "hmm"
            burn "hmpt !...... WELL...... I guess you are right.. ha"
            $ burns_face = "normal_t"
            burn "But how will I... you know. Do unusual things with her.."
            $ burns_face = "normal"
            weylon "You could have her meet a condition before she can get her offer"
            $ burns_face = "normal_t"
            burn ".. hmm I like the sound of that, keep going"
            $ burns_face = "normal"
            weylon "Have her do your activites that you desire, you know the little pleasure of immeasurable proportions"
            $ burns_face = "laugh"
            burn "HA, you know what I want, WAIT. Why do you know this.. ?"
            $ burns_face = "normal"
            weylon "Hm.. welll. . . . *ahem* SIR, as I was saying, make her meet your condition. However if she show some sort of resistent and tries to do something like calling the cops, I have your back on that."
            weylon "We can lockdown the mansion and she wouldn't be able to call the police. Gass her out, and have her in your chamber if you have unlocked it already"
            weylon "However, there is a slight problem.."
            burn "? . ."
            weylon "The gas isn't turned on properly"
            weylon "We need to call in Scratchy to activate it so I can trigger the gass with my remote"
            $ burns_face = "hmm"
            burn "Wait, Scratchy?... you mean the pychopath looking cat with MUSCLE"
            $ burns_face = "normal"
            weylon "Yes, he lives in this mansion, just hiding in some sneaky location"
           # weylon "But, we can call him out and get him to activate the gas"
            $ burns_face = "normal_t"
            burn "Where can I find this cat ?"
            $ burns_face = "normal"
            weylon "You need a special instrument to call him"
            $ burns_face = "normal"
            weylon "But, I do not know where the instrument is. You probably will have to find it"
            burn "*.... I could probably ask around to see if they have seen it or not*"
            # burn ".... ok, where exactly is this instrument tool ?"
            # $ burns_face = "normal"
            # weylon "There is this seller that has the instrument which you can buy"
            # weylon "You can ask me anytime when you want to call the Seller over"
            # $ burns_face = "normal_t"
            $ burns_face = "normal_t"
            burn "Okay anyways"
            burn "I like this, be sure you make no mistake Weylon"
            $ burns_face = "normal"
            weylon "Yes, sir."
            $ burns_face = "normal_t"
            burn "Now, I shall do my deeds"
            $ seller_call = True
            $ ashley_story += 1
            jump  office_weylon

        "Ashley" if ashley_story == 9:
            $ burns_face = "normal_t"
            burn "Weylon, I was able to punish her"
            $ burns_face = "normal"
            weylon "That's great, sir"
            weylon "But did you get to pester her? sir"
            $ burns_face = "hmm"
            ". . ."
            $ burns_hands = "4"
            burn ". . . no"
            burn "I didn't have enough balls or dominance over her yet, so I just told her to get back to work"
            $ burns_hands = "3"
            burn "But, how would I seal the deal 100 percent & have her back to the Chamber, where I can do my tangling"
            $ burns_face = "normal"
            weylon "Well sir, remember the offer you made her ?"
            $ burns_face = "normal_t"
            burn "? . . what offer"
            $ burns_face = "normal"
            weylon "Sir, you offered her Manager role "
            $ burns_face = "hmm"
            burn "Ahhhh . .  yes, but wasn't that all just an act ?"
            $ burns_face = "normal"
            weylon "It was, but you can still offer her the role, but in return to she must keep visitng you in the chamber whenever you ask her to and punish her even more"
            $ burns_face = "normal_t"
            burn "That's right, that's a brilliant plan"
            $ burns_face = "laugh"
            pause
            $ burns_face = "normal"
            weylon "But before, you offer her sir. You need to get her a business outfit"
            weylon "And the rest, I'll teach her"
            $ burns_face = "hmm"
            burn "A business outfit? . . Does the seller guy sell fashion ?"
            $ burns_face = "normal"
            weylon "From what I remember, I'm pretty sure he does sells clothes. You probably might have to ask him about it"
            $ burns_face = "normal_t"
            burn "Ok"
            jump office_weylon

        "Scratchy Instrument" if player.bags[0].exist(cat_instrument, 1) and ashley_story == 2:
            burn "I have the instrument.. how do I call him ?"
            weylon "I'm not sure sir . . . there is a specfic place to call him"
            burn "*Useles...*"
            $ burns_face = "angry_t"
            burn "USELESS !!"
            $ burns_face = "normal"
            burn "*ahem..*"
            jump office_weylon

        "Firecamp" if office_firecamp_key == True:
            burn "I remember this firecamp would open easily"
            burn "Why isn't it openeing properly?"
            weylon "Sir, I added a lock to it, so you would need a key to open it"
            burn "When did I ever need A KEY!?!?"
            weylon "Sir, people were able to go in and out whenever they wanted"
            weylon "and.  . ."
            burn ". . . . actually you know what"
            burn "Just give me the key"
            weylon "Sure, here you go"
            show key_item_frame
            "You obtained a key !"
            pause
            $ player.got(office_key, 1)
            $ office_firecamp_key = False
            hide key_item_frame

        "Call the Seller" if seller_call == True:
            burn "Call him now to my room"
            weylon "Right away !"
            $ seller_npc = True
            jump office_weylon

        "Chamber door" if check_door == True:
            $ burns_face = "hmm"
            burn "WEYLON !"
            $ burns_face = "angry"
            weylon "Yes ? do you need something sir ?"
            $ burns_face = "normal_t"
            burn "Why don't I remember the thing in the chamber entrance ?"
            $ burns_face = "normal"
            weylon "What thing. .? sir"
            $ burns_face = "normal_t"
            burn "THE THING WEYLON"
            $ burns_face = "normal"
            weylon "I'm sorry, but. . I do .n"
            $ burns_face = "angry_t"
            burn "Weylon, don't make me go furious. I'm talking about the thing on the door that I can't seem to remember"
            $ burns_face = "angry"
            weylon "*...the thing on the door ?.... OH right, now I see*"
            weylon "Sir, you mean your genius idea on the door that you seem to forgot about ?"
            $ burns_face = "normal_t"
            burn "Yes"
            $ burns_face = "normal"
            weylon "*...* You wanted to make three different shape which were diamonds. You need diamonds pieces to open the door"
            $ burns_face = "normal_t"
            burn "Oh yes, now I remember"
            burn "Remind me what diamond I'm looking for.. again? . ."
            $ burns_face = "normal"
            weylon "The red, green and blue diamond"
            $ burns_face = "normal_t"
            burn "AHH yes , that's right. "
            jump office_weylon

        # "Burn Sinister Head test":
        #     $ burns_accessory = "sinister"
        #     burn "..."
        #     weylon "*laughs*"
        #     $ burns_face = "normal_t"
        #     burn "wut"
        #     $ burns_face = "normal"
        #     weylon "U got a sinister on your head . "
        #     $ burns_face = "normal_t"
        #     burn "What....the"
        #     $ burns_face = "angry"
        #     burn "*wipes it off*"
        #     $ burns_face = "normal"
        #     $ burns_accessory = "none"
        #     $ burns_face = "normal_t"
        #     burn "ahem"
            
        "Nothing, weylon":
            jump office_weylon 
        "Leave":
            jump office


#    burn "How much would you pay for a Weylon?"
    jump office

label office_firecamp:
    
    if player.bags[0].exist( office_key, 1):
        burn "There we go, there was a key right next to it"
        burn "*Inserts the key*"
        $ player.drop(office_key, 1)
        $ office_firecamp_open = True
    #    $ renpy.notify("Key was used")
        jump chamber_entrance

    elif office_firecamp_open == True:
        play music "audio/Melancholia.mp3"
        jump chamber_entrance

    else:
        burn "You can burn a body in it."
        burn "Wait a minute. . ."
        burn "Why can't I open the door ? I can easily go in and out.... maybe . ."
        burn "Weylon.... he might know"
        $ office_firecamp_key = True
        jump office
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

label office_ashley:
    hide screen map
    $ ashley_clothe = "suit"
    $ ashley_face = "normal"
    $ ashley_arms = "2"
    scene office blur
    show ashley_base at right
    $ burns_face = "normal"
    show burn_base at left
    menu:
        "Outfit":
            $ burns_face = "normal_t"
            burn "How'd you like your new outfit ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Looks great, sir."
            ashley "I always dreamed of feeling like a CEO in suit, and this just fits the taste"
            $ burn_face = "hmm"
            $ ashley_face = "normal"
            burn "Good good, and what else ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "... and your condition... of course sir."
            $ burns_face = "laugh"
            $ ashley_face = "confuse"
            burn "Very very good *hahahaaaaaaaaa*"
            $ burns_face = "normal_t"
            burn "Anyways, I'll see you around"
            jump office_ashley

        "Leave":
            jump office

label office_fossil:
    burn "My very own expensive Fossil"
    burn "It's pure and beautiful, just look at its NOSE it possess"
    burn "Too expensive for me to risk and sell this.. maybe I'll leave it alone for now . ."
    jump office

label office_football:
    burn "Ahh HA, a signed football"
    burn "This will definitly sell me some good price !"

    show football_item_frame onlayer over_screens
    "A signed football !"
    hide football_item_frame onlayer over_screens
    $ office_map.rem(office_football_loc)
    $ player.got(signed_ball, 1)
    jump office

label office_book:
    burn "... useless"
    jump office
