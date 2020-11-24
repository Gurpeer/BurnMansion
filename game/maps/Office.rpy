image bird_move:
    "maps/office/office_bird.png"
    xpos 800 yalign .2
    linear 8 xpos renpy.random.randint(280,315) yalign .2
    pause 2
    xpos 800 yalign .2
    linear 8 xpos renpy.random.randint(235,338) yalign .3
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
    show weylon_base at right
    $ burns_face = "normal"
    show burn_base at left
    menu:
        # "Ashley" if ashley_story == 1:
        #     $ burns_face = "normal_t"
        #     burn "Weylon, I need some.... couple of help here"
        #     $ burns_face = "normal"
        #     weylon "Yes, what do you need sir ?"
        #     $ burns_face = "hmm"
        #     burn "Well.. Ashley has some kind of issue with her pride of women rights and I don't really know what she needs"
        #     $ burns_face = "normal"
        #     weylon "Women right ?"
        #     $ burns_face = "laugh"
        #     burn "... she asked to be a CEO and got rejected. HAHAHAHA"
        #     $ burns_face = "normal"
        #     weylon "Oh, I see the problem"
        #     weylon "Sir, how about you offer her a position here at the desk?"
        #     $ burns_face = "angry_t"
        #     burn "WHAT? That is out of questions ! "
        #     $ burns_face = "angry"
        #     weylon "Well, I think it's a brilliant plan sir, you could trick her into thinking she is a official manager but isn't. Have her hunt for woman from the street as a job while pretending to act as a Manager"
        #     $ burns_face = "hmm"
        #     burn "hmpt !...... WELL...... I guess you are right.. ha"
        #     $ burns_face = "normal_t"
        #     burn "But how will I... you know. Do unusual things with her.."
        #     $ burns_face = "normal"
        #     weylon "You could have her meet a condition before she can get her offer"
        #     $ burns_face = "normal_t"
        #     burn ".. hmm I like the sound of that, keep going"
        #     $ burns_face = "normal"
        #     weylon "Have her do your activites that you desire, you know the little pleasure of immeasurable proportions"
        #     $ burns_face = "laugh"
        #     burn "HA, you know what I want, WAIT. Why do you know this.. ?"
        #     $ burns_face = "normal"
        #     weylon "Hm.. welll. . . . *ahem* SIR, as I was saying, make her meet your condition. However if she show some sort of resistent and tries to do something like calling the cops, I have your back on that."
        #     weylon "We can lockdown the mansion and she wouldn't be able to call the police. Gass her out, and have her in your chamber if you have unlocked it already"
        #     weylon "However, there is a slight problem.."
        #     burn "? . ."
        #     weylon "The gas isn't turned on properly"
        #     weylon "We need to call in Scratchy to activate it so I can trigger the gass with my remote"
        #     $ burns_face = "hmm"
        #     burn "Wait, Scratchy?... you mean the pychopath looking cat with MUSCLE"
        #     $ burns_face = "normal"
        #     weylon "Yes, he lives in this mansion, just hiding in some sneaky location"
        #    # weylon "But, we can call him out and get him to activate the gas"
        #     $ burns_face = "normal_t"
        #     burn "Where can I find this cat ?"
        #     $ burns_face = "normal"
        #     weylon "You need a special instrument to call him"
        #     $ burns_face = "normal"
        #     weylon "But, I do not know where the instrument is. You probably will have to find it"
        #     burn "*.... I could probably ask around to see if they have seen it or not*"
        #     # burn ".... ok, where exactly is this instrument tool ?"
        #     # $ burns_face = "normal"
        #     # weylon "There is this seller that has the instrument which you can buy"
        #     # weylon "You can ask me anytime when you want to call the Seller over"
        #     # $ burns_face = "normal_t"
        #     $ burns_face = "normal_t"
        #     burn "Okay anyways"
        #     burn "I like this, be sure you make no mistake Weylon"
        #     $ burns_face = "normal"
        #     weylon "Yes, sir."
        #     $ burns_face = "normal_t"
        #     burn "Now, I shall do my deeds"
        #     $ seller_call = True
        #     $ ashley_story += 1
        #     jump  office_weylon

        # "Ashley" if ashley_story == 9:
        #     $ burns_face = "normal_t"
        #     burn "Weylon, I was able to punish her"
        #     $ burns_face = "normal"
        #     weylon "That's great, sir"
        #     weylon "But did you get to pester her? sir"
        #     $ burns_face = "hmm"
        #     ". . ."
        #     $ burns_hands = "4"
        #     burn ". . . no"
        #     burn "I didn't have enough balls or dominance over her yet, so I just told her to get back to work"
        #     $ burns_hands = "3"
        #     burn "But, how would I seal the deal 100 percent & have her back to the Chamber, where I can do my tangling"
        #     $ burns_face = "normal"
        #     weylon "Well sir, remember the offer you made her ?"
        #     $ burns_face = "normal_t"
        #     burn "? . . what offer"
        #     $ burns_face = "normal"
        #     weylon "Sir, you offered her Manager role "
        #     $ burns_face = "hmm"
        #     burn "Ahhhh . .  yes, but wasn't that all just an act ?"
        #     $ burns_face = "normal"
        #     weylon "It was, but you can still offer her the role, but in return to she must keep visitng you in the chamber whenever you ask her to and punish her even more"
        #     $ burns_face = "normal_t"
        #     burn "That's right, that's a brilliant plan"
        #     $ burns_face = "laugh"
        #     pause
        #     $ burns_face = "normal"
        #     weylon "But before, you offer her sir. You need to get her a business outfit"
        #     weylon "And the rest, I'll teach her"
        #     $ burns_face = "hmm"
        #     burn "A business outfit? . . Does the seller guy sell fashion ?"
        #     $ burns_face = "normal"
        #     weylon "From what I remember, I'm pretty sure he does sells clothes. You probably might have to ask him about it"
        #     $ burns_face = "normal_t"
        #     burn "Ok"
        #     jump office_weylon

        # "Scratchy Instrument" if player.bags[0].exist(cat_instrument, 1) and ashley_story == 2:
        #     burn "I have the instrument.. how do I call him ?"
        #     weylon "I'm not sure sir . . . there is a specfic place to call him"
        #     burn "*Useles...*"
        #     $ burns_face = "angry_t"
        #     burn "USELESS !!"
        #     $ burns_face = "normal"
        #     burn "*ahem..*"
        #     jump office_weylon

        # "Firecamp" if office_firecamp_key == True:
        #     $ burns_face = "normal_t"
        #     burn "I remember this firecamp would open easily"
        #     burn "Why isn't it openeing properly?"
        #     $ burns_face = "normal"
        #     weylon "Sir, I added a lock to it, so you would need a key to open it"
        #     $ burns_face = "angry_t"
        #     burn "When did I ever need A KEY!?!?"
        #     $ burns_face = "angry"
        #     weylon "Sir, people were able to go in and out whenever they wanted"
        #     weylon "and.  . ."
        #     $ burns_face = "normal_t"
        #     burn ". . . . actually you know what"
        #     burn "Just give me the key"
        #     $ burns_face = "normal"
        #     weylon "Sure, here you go"
        #     show key_item_frame
        #     "You obtained a key !"
        #     pause
        #     $ player.got(office_key, 1)
        #     $ office_firecamp_key = False
        #     hide key_item_frame

        # "Call the Seller" if seller_call == True:
        #     burn "Call him now to my room"
        #     weylon "Right away !"
        #     $ seller_npc = True
        #     jump office_weylon

        # "Chamber door" if check_door == True:
        #     $ burns_face = "hmm"
        #     burn "WEYLON !"
        #     $ burns_face = "angry"
        #     weylon "Yes ? do you need something sir ?"
        #     $ burns_face = "normal_t"
        #     burn "Why don't I remember the thing in the chamber entrance ?"
        #     $ burns_face = "normal"
        #     weylon "What thing. .? sir"
        #     $ burns_face = "normal_t"
        #     burn "THE THING WEYLON"
        #     $ burns_face = "normal"
        #     weylon "I'm sorry, but. . I do .n"
        #     $ burns_face = "angry_t"
        #     burn "Weylon, don't make me go furious. I'm talking about the thing on the door that I can't seem to remember"
        #     $ burns_face = "angry"
        #     weylon "*...the thing on the door ?.... OH right, now I see*"
        #     weylon "Sir, you mean your genius idea on the door that you seem to forgot about ?"
        #     $ burns_face = "normal_t"
        #     burn "Yes"
        #     $ burns_face = "normal"
        #     weylon "*...* You wanted to make three different shape which were diamonds. You need diamonds pieces to open the door"
        #     $ burns_face = "normal_t"
        #     burn "Oh yes, now I remember"
        #     burn "Remind me what diamond I'm looking for.. again? . ."
        #     $ burns_face = "normal"
        #     weylon "The red, green and blue diamond"
        #     $ burns_face = "normal_t"
        #     burn "AHH yes , that's right. "
        #     jump office_weylon

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
        play music "audio/Melancholia.mp3"
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
        "Compliment her outfit" if ashley_dominance < 3:
            $ burns_face = "normal_t"
            burn "The outfit suits you"
            $ renpy.notify("Gained one dominance point")
            $ ashley_dominance += 1
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "thank you, sir."
            ashley "I always dreamed of feeling like a CEO in suit, and this just fits the taste"
            $ burns_face = "hmm"
            $ ashley_face = "normal"
            burn "Good good, and what else ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "... and your condition... of course sir."
            $ burns_face = "smirkleft"
            burn "*That's right, keep that in mind. The soon to be my bit... lady*"
            pause
            $ burns_face = "smirkright"
            $ ashley_face = "confuse"
            burn "Very very good *hahahaaaaaaaaa*"
            $ burns_face = "normal_t"
            burn "Anyways, I'm glad the suit fits you"
            $ burns_face = "angry"
            burn "*because that suit costed me 100 BUCKS . . . if it didn't fit her well, that seller will get dropped like the yes men in my own hand. . .*"
            $ burns_face = "normal"
            jump office_ashley

        "Talk" if allison_story == 1:
            $ burns_face = "normal_t"
            burn "Has Weylon talk to you yet ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Yes....told me just what I need to do for my role"
            $ burns_face = "hmm"
            $ ashley_face = "normal"
            burn "Oh really ? and what exactly is your role here, Miss . Ashley"
            $ burns_face = "normal"
            $ ashley_face = "confuset"
            ashley ". . . to find woman . ."
            $ burns_face = "hmm"
            $ ashley_face = "confuse"
            burn "and ?"
            $ burns_face = "normal"
            $ ashley_face = "confuset"
            ashley "and to . ."
            $ burns_face = "normal_t"
            $ ashley_face = "confuse"
            burn "Ashley"
            $ burns_face = "normal"
            $ ashley_face = "confuset"
            ashley "Yes ?"
            $ burns_face = "normal_t"
            $ ashley_face = "confuse"
            burn "Can you stop stuttering like every few seconds, is this what a Manager should be like? I feel like I should remov.."
            $ burns_face = "smirkright"
            $ ashley_face = "normalt"
            ashley "WAIT, wait"
            ashley "*ahem* let me redo"
            ashley "I was order to find woman and maniplulate them to live in this most glorious mansion"
            ashley "Make them pay the unimginable amount of rent, and suck their money dry"
            $ burns_face = "normal_t"
            $ ashley_face = "normal"
            burn "Glorious ? Oh, stop it. Now this is the manager vibe I was looking for"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Yes, sir"
            $ burns_face = "hmm"
            $ ashley_face = "normal"
            burn "Now, you got any idea on who's the next target ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Absolutely, sir. Luckly I found someone who needs a place to stay"
            $ burns_face = "smirkleft"
            $ ashley_face = "confuse"
            burn "Oh ? *evil smirk with exictement*"
            pause
            $ burns_face = "normal_t"
            burn "Who is it ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Are you fimiliar with Lisa Homer ?"
            $ burns_face = "hmm"
            $ ashley_face = "normal"
            burn "Ahh yes, the Homer's family *LISA? FOR REAL? oh.... man I can't wait to*"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "That's right, we can get her"
            burn "*Dammit Ashley, can't you let me finish my line*"
            ashley "Allison is close friend with her since they both go to College together"
            ashley "Sir, you should talk to Allison & pursuade her to invite Lisa here"
            $ burns_face = "normal"
            $ ashley_face = "normal"
            burn "*How the hell Im I going to... wait wait Allison? . . I was going to offer her big money. *"
            $ burns_face = "normal_t"
            $ ashley_face = "normal"
            burn "This is not my resposibility here, remember? IT IS YOU that need to bring LISA here"
            $ burns_face = "normal"
            $ ashley_face = "angryt"
            ashley "SIR !"
            $ burns_face = "normal_t"
            $ ashley_face = "confuse"
            burn ". . ."
            $ burns_face = "hmm"
            $ ashley_face = "normal"
            burn "..... did you just raise your voice again?"
            $ burns_face = "normal"
            $ ashley_face = "confuset"
            ashley "No..no... I mean sir. What I wanted to say is that, you need to pursuade her"
            $ burns_face = "smirkleft"
            $ ashley_face = "normal"
            burn "*You need to be punished... with that voice....anyways*"
            $ burns_face = "normal_t"
            $ ashley_face = "normal"
            burn "Pursuade her how ?"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "I just saw this red book laying right here, and I think it was called Massage Spa 101? "
            $ ashley_face = "confuse"
            burn ". . . ."
            $ burns_face = "angry_t"
            burn "What does this have anything to do with PURSUADING HER ?!!?!?"
            $ burns_face = "angry"
            $ ashley_face = "normal"
            ashley "sir.. Why don't you offer her to massage ?"
            burn "*I feel like I'm about to burst... relax. I should just breath in & out... RELAX*"
            ashley " . . . ."
            burn ". . . ."
            ashley ". . . ."
            $ burns_face = "normal_t"
            $ ashley_face = "normal"
            burn "You know what, I'll do it my way. *Useless woman...do you not realize my brilliant mind? I got this*"
            $ burns_face = "normal"
            $ ashley_face = "normalt"
            ashley "Whatever you say sir, I'm sure it'll work out *Useless ugly old man, you realize she likes massaging right?....*"
            $ burns_face = "normal"
            $ ashley_face = "normal"
            burn "*... big money.. where will I make big money ....*"
            $ allison_story += 1
            jump office_ashley


        "Punishment":
            $ burns_face = "smirkright"
            pause
            $ burns_face = "normal_t"
            burn "You know what time is is, Ashley"
            $ ashley_face = "confuse"
            ashley "? . ."
            burn "Time for your punishment"
            $ ashley_face = "confuset"
            $ progress_bar = 0
            ashley ". . . yes, sir..."
            play music "audio/Melancholia.mp3"
            jump chamber_ashley_scene

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
