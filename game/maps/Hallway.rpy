image hallway_lighting:
    "maps/hallway/lighting_screen.png" with dissolve
    .4
    "maps/hallway/lighting_screen3.png" with dissolve
    .9
    "maps/hallway/lighting_screen1.png" with dissolve
    2
   # pause .5
    repeat


image hallway_fire:
    "maps/hallway/fire1.png" with dissolve
    .25
    "maps/hallway/fire2.png" with dissolve
    .25
    "maps/hallway/fire3.png" with dissolve
    .25
    "maps/hallway/fire4.png" with dissolve
    .25
    repeat

transform weylon_flip_position:
    xalign 0.3
    ypos 0.65

default hallway_hall_loc = place("Hall Door", (587, 260), Jump('front_hall'), "maps/hallway/front door.png")
default hallway_left_loc = place("Hall Left", (0, 146), Jump('burn_room'), "maps/hallway/burn door.png")
default hallway_bathroom_loc = place("Hall Bathroom", (168, 201), Jump('bathroom'), "maps/hallway/bathroom door.png")
default hallway_office_loc = place("Hall Office", (1057, 117), Jump('office'), "maps/hallway/office door.png")
default hallway_allison_loc = place("Allison", (379, 299), Jump('hallway_allison'), "maps/hallway/allison.png")
default hallway_sword_loc = place("Sword", (816, 420), Jump('hallway_sword'), "maps/hallway/sword.png")
default hallway_armour_loc = place("Armour", (0, 339), Jump('hallway_doomarmor'), "maps/hallway/doom armor.png")
default hallway_shield_loc = place("Shield", (1458, 689), Jump('hallway_shield'), "maps/hallway/shield.png")
default hallway_hole_loc = place("Hole", (337, 510), Jump('hallway_rathole'), "maps/hallway/rat hole.png")
#default hallway_lighting_loc = place("lighting", (0, 0), None, "hallway_lighting")
default hallway_redgem_loc = place("Red_gem", (402, 42), Jump("hallway_redgem"), "maps/hallway/red_gem.png")


default main_hall_map = maps(
    "Hallway",
    [
        "hallway_lighting",
        "hallway_fire",
        hallway_hall_loc,
        hallway_left_loc,
        hallway_bathroom_loc,
        hallway_office_loc,
        hallway_allison_loc,
        hallway_sword_loc,
        hallway_hole_loc,
        hallway_redgem_loc,
        hallway_armour_loc,
        hallway_shield_loc,
       # hallway_lighting_loc,
    ]
    )

label main_hall:
    scene hallway bg
   # show hallway_fire
    #show hallway_lighting
    show screen map(main_hall_map)
    pause
    jump main_hall

label hallway_rathole:
    if player.bags[0].exist(cat_instrument, 1) and ashley_story == 2:
        $ burns_face = "normal"
        $ burns_hands = "3"
        $ burns_holding = "nothing"
        show burn_base onlayer screens at left
        burn "I should try to use the instrument right here.."
        ". . ."
        $ burns_hands = "4"
        $ burns_holding = "instrument"
        burn "*Whistles hard*"
        burn ". . . ."
        burn ". . . . . . ."
        $ burns_face = "angry_t"
        burn "Why is he not showing up yet? !?!?"
        $ burns_face = "angry"
        burn ". . ."
        $ burns_holding = "nothing"
        $ burns_hands = "3"
        $ burns_face = "normal_t"
        burn "Been couple of minutes now..."
        $ burns_face = "normal"
        ". . hear some noise.. seem like something is coming out of a tiny hole..."
        show scratchy_base onlayer screens at right with dissolve
        scratchy "argh..... ewfim ewosiue"
        $ scratchy_face = "talk"
        scratchy "*meow* *mewowwwwwwwww*"
        $ scratchy_face = "look"
        $ burns_face = "normal_t"
        burn "... I can't understand what this buffy cat even saying... god dammit"
        burn "Listen here, cat"
        burn "I need you to reactivate the gas"
        $ burns_face = "normal"
        $ scratchy_face = "talk"
        scratchy "*MEWOWWEOW* mewow... meow. "
        $ burns_face = "normal_t"
        $ scratchy_face = "normal"
        burn ". . ?"
        burn "is that a yes or no ?"
        $ burns_face = "normal"
        $ scratchy_face = "talk"
        scratchy "Meow."
        $ burns_face = "normal_t"
        $ scratchy_face = "look"
        burn "I probaly need to call Weylon here"
        $ burns_hands = "phone"
        burn "*Calls Weylon*" 
        weylon "Yes ?"
        $ burns_face = "angry_t"
        burn "Get over here NOW !"
        $ burns_face = "normal"
        weylon "Ok, sir"
        $ burns_hands = "3"
        $ burns_face = "normal"
        show weylon normal onlayer screens at weylon_flip_position:
            xzoom -1
        weylon "Yes, you need somethin.."
        weylon "*Mew mewowow*"
        $ scratchy_face = "talk"
        scratchy "MEOWWOW"
        $ scratchy_face = "normal"
        weylon "Ah yes, I understand"
        weylon "Meow meeeow mee meow"
        $ scratchy_face = "look"
        scratchy "Meo e meeeeeeeow"
        $ scratchy_face = "normal"
        weylon "Well, that settles it."
        weylon "Sir, he will activate it, but it'll work next day."
        burn ". . . ."
        burn "*what did I just witness ?*"
        weylon "Sir ?"
        $ burns_face = "normal_t"
        burn "*AHEM*, ok"
        burn "You may leave Weylon and you too Scratchy... *I probably need to find some sort of tool to communicate with this Cat*"
        $ burns_face = "normal"
        hide scratchy_base onlayer screens at right
        hide weylon normal onlayer screens at weylon_flip_position
        burn ". . . ."
        $ burns_face = "normal_t"
        burn "Well, I should just stay away from that rat hole for now"
        $ burns_face = "normal"
        $ ashley_story += 1
        hide burn_base onlayer screens at left
        jump main_hall

    else:
        burn ". . . a hole ?" 
        jump main_hall

label hallway_doomarmor:
    burn "This armor...."
    burn "They said it was called Doom Armour?"
    burn "I have no clue who Doom is. . .  I just brought it from the most luxury merchandise"
    burn "I'll just take this armor and sell it, I see no use of it. . . . ."
    show doomarmor_item_frame onlayer over_screens
    "Doom Armour !"
    hide doomarmor_item_frame onlayer over_screens
    $ main_hall_map.rem(hallway_armour_loc)
    $ player.got(doom_armor, 1)

    jump main_hall

label hallway_shield:
    burn "Nothing too special about this shield"
    burn "Looks sellable, and worth a decent price"
    burn "But this thing is heavy.... how will I pick this up?"
    burn "Might have to find something or someone to help lift this big shield "
    jump main_hall

# label hallway_hall_left:
#     burn "Burn room still in progress. ."
#     jump main_hall

label hallway_redgem:
    burn "A red looking gem"
    if player.bags[0].exist(ladder_home, 1): 
        show redgem_item_frame onlayer over_screens
        "Obtained a red diamond"
        hide redgem_item_frame onlayer over_screens
        $ main_hall_map.rem(hallway_redgem_loc)
        $ player.got(red_gem, 1)
        jump main_hall
    else:
        burn "That's too high for me to grab"
        burn "Going to need some sort of ladder or something to reach it"
        jump main_hall

label hallway_allison:
    if ashley_story == 10 and ashley_waist == 0:
        jump ask_allison_ashley_waist

    if allison_story == 0:
        $ main_hall_map.rem(hallway_allison_loc)
        jump allison_event1
    else:
        burn "I already talked to her.. need to find ways to make big money !"

    if ask_instrument == 1:
        $ main_hall_map.rem(hallway_allison_loc)
        show burn_base onlayer screens at left with dissolve
        $ burns_face = "normal"
        $ burns_hands = "3"
        show allison_base onlayer screens at right with dissolve
        $ burns_face = "normal_t"
        burn "Hello Allison"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison "Hello, sir"
        $ burns_face = "hmm"
        $ allison_face = "normal"
        burn "I heard you like Music ?"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison "Yes I do !"
        allison "Hold on, how you know I'm into music ?"
        $ burns_face = "normal_t"
        $ allison_face = "normal"
        burn "Well, like I said. I just heard . . nothing else "
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison ". . ."
        allison "What's my favorite instrument ?"
        $ burns_face = "normal_t"
        $ allison_face = "normal"
        burn ". . . uhm flute ?"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison "No . . It's sexaphone"
        allison "The pure and the beaut. ."
        $ burns_face = "normal"
        $ allison_face = "normal"
        burn "*oh boy, I don't want to listen to this little fuzzy stories on beauty about instrument...*"
        $ burns_face = "hmm"
        burn "Look here, Allison. I'm not here to listen to your god d... wonderful story, I'm in a hurry here"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison "Then. . . what exactly are you here for then? hmpt"
        $ burns_face = "normal_t"
        $ allison_face = "normal"
        burn "Looking for this missing instrument piece that can call Scratchy"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison ". . . the pyscho looking cat? really"
        $ burns_face = "normal_t"
        $ allison_face = "normal"
        burn "Yes the pyscho looking cat, Miss. Allison"
        $ burns_face = "normal"
        $ allison_face = "angry"
        pause
        $ allison_face = "normalt"
        allison "He is really dangerous you know... he"
        $ burns_face = "hmm"
        $ allison_face = "confuse"
        burn "ALLISON, I'm asking a question here"
        $ burns_face = "angry"
        $ allison_face = "confuset"
        allison "Oh, yes. Sorry, I just.."
        $ burns_face = "angry_t"
        $ allison_face = "confuse"
        burn "Answer the question, just stop blabbering. Getting on my nerve already !"
        $ burns_face = "angry"
        $ allison_face = "confuset"
        allison "Sir, from what I remember. I gave it away to this mystery mask man in a white suit"
        $ burns_face = "smirkleft"
        $ allison_face = "confuse"
        burn "*.. this whole time, the seller had it... *"
        $ burns_face = "hmm"
        $ allison_face = "confuse"
        burn "Thanks, bye"
        $ burns_face = "normal"
        $ allison_face = "normalt"
        allison "Wait sir. .  I"
        burn "*NOPE*"
        $ ask_instrument += 1
        hide burn_base onlayer screens at left with dissolve
        hide allison_base onlayer screens at right with dissolve  
        $ main_hall_map.discover(hallway_allison_loc)
        jump main_hall     

    jump main_hall

label hallway_sword:
    burn "A default looking sword.. i could pick this up."
    show sword_item_frame onlayer over_screens
    "A default sword !"
    hide sword_item_frame onlayer over_screens
    $ main_hall_map.rem(hallway_sword_loc)
    $ player.got(default_sword, 1)
    jump main_hall


