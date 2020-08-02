image bathroom_air:
    "maps/bathroom/air.png" with dissolve
    .9
    "maps/bathroom/air2.png" with dissolve
    .8
    "maps/bathroom/air3.png" with dissolve
    .9
    repeat    


default bathroom_door_loc = place("Door", (859, 519), Jump('main_hall'), "maps/bathroom/washroom door.png")
default bathroom_lock_loc = place("Lock", (704, 210), Jump('bathroom_lock'), "maps/bathroom/washroom lock.png")
# default bathroom_clay_loc = place("Clay", (315, 394), Jump('bathroom_clay'), "maps/bathroom/washroom clay_guy.png")
default bathroom_ashley_loc = place("Ashley", (954, 710), Jump('bathroom_ashley'), "maps/bathroom/washroom ashley.png")
default bathroom_s_candle_loc = place("s_candle", (1746, 444), Jump('bathroom_s_candle'), "maps/bathroom/s_candle.png")
default bathroom_towel_loc = place("Towel", (1055, 476), Jump('bathroom_towel'), "maps/bathroom/towel.png")
default bathroom_greengem_loc = place("Green_gem", (165, 250), Jump('bathroom_greengem'), "maps/bathroom/green_gem.png")
default bathroom_bathtub_loc = place("Bathtub", (1281, 839), Jump('bathroom_bathtub'), "maps/bathroom/washroom_tub.png")

default bathroom_map = maps(
    "Bathroom",
    [
        "bathroom_air",
        bathroom_door_loc,
        bathroom_lock_loc,
        bathroom_greengem_loc,
        bathroom_s_candle_loc,
        bathroom_towel_loc,
        bathroom_bathtub_loc,
        # bathroom_clay_loc,
        bathroom_ashley_loc,

    ]
    )

label bathroom:
    if ashley_story == 3:
        $ bathroom_map.rem(bathroom_ashley_loc)
        $ ashley_story += 1
    if ashley_story == 8:
        $ bathroom_map.discover(bathroom_ashley_loc)
        $ ashley_story += 1     

    scene washroom bg
   # show bathroom_air
    show screen map(bathroom_map)
    pause
    jump bathroom

label bathroom_lock:
    if player.bags[0].exist(ladder_home, 1):
        hide screen map  
        scene bathroom_lockstorage_bg
        burn "AH ha, there we go, finally up here"
        burn "Seems like I have no use to unlock this for now"
        burn "There's other things I need to finish first"
        burn "... I just notice the piece is also missing... *sign*"
        burn "Entering the password would be useless without the piece"
        jump bathroom
    else:
        burn "looks like a lock and... I can't even get up there"
        burn "Might need to find a ladder or some kind to reach it"
        jump bathroom

label bathroom_clay:
    burn "Please take me."
    jump bathroom

label bathroom_s_candle:
    burn "A s candle"
    burn "I smell great price with this !"
    jump bathroom

label bathroom_towel:
    burn " . . . ."
    burn "Doesn't look pricey ..."
    burn "Nope"
    jump bathroom

label bathroom_greengem:
    burn "A green looking gem"
    show greengem_item_frame onlayer over_screens
    "Obtained a green diamond"
    hide greengem_item_frame onlayer over_screens
    $ bathroom_map.rem(bathroom_greengem_loc)
    $ player.got(green_gem, 1)
    jump bathroom

label bathroom_bathtub:
    burn "Ah, yes. The relaxation that water has"
    burn "But, not in the mood for this"
    jump bathroom

label bathroom_ashley:
    if ashley_story == 0:
        $ bathroom_map.rem(bathroom_ashley_loc)
        jump ashley_event1
        
    if ashley_story == 1:
        burn "Should talk to Weylon about her, don't exactly know what to do with her"
        jump bathroom
    # if chamber_access == False and ashley_story == 2:
    #     burn "I have not unlocked the Chamber yet to execute my brilliant plan and it's better I talk to her next day"
    #     jump bathroom
    if ashley_story == 9:
        burn "Should probably talk to Weylon again"
        burn "Need to get her back to the chamber again"
        jump bathroom

    if player.bags[0].exist(ashley_business_suit, 1):
        jump give_ashley_business_suit
    else:
        burn "Talk to her later, not now"
    #    burn "Triggers first event scene dialogue."
        jump bathroom



