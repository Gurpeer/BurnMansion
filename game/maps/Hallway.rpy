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

default hallway_hall_loc = place("Hall Door", (587, 260), Jump('front_hall'), "maps/hallway/front door.png")
default hallway_left_loc = place("Hall Left", (0, 146), Jump('burn_room'), "maps/hallway/burn door.png")
default hallway_bathroom_loc = place("Hall Bathroom", (168, 201), Jump('bathroom'), "maps/hallway/bathroom door.png")
default hallway_office_loc = place("Hall Office", (1057, 117), Jump('office'), "maps/hallway/office door.png")
default hallway_allison_loc = place("Allison", (398, 291), Jump('hallway_allison'), "maps/hallway/allison.png")
default hallway_sword_loc = place("Sword", (816, 420), Jump('hallway_sword'), "maps/hallway/sword.png")
default hallway_armour_loc = place("Armour", (0, 339), Jump('hallway_doomarmor'), "maps/hallway/doom armor.png")
#default hallway_ball_loc = place("Ball", (189, 461), Jump('hallway_pickup'), "maps/hallway/ball.png")
default hallway_shield_loc = place("Shield", (1458, 689), Jump('hallway_shield'), "maps/hallway/shield.png")
default hallway_lighting_loc = place("lighting", (0, 0), None, "hallway_lighting")


default main_hall_map = maps(
    "Hallway",
    [
        hallway_hall_loc,
        hallway_left_loc,
        hallway_bathroom_loc,
        hallway_office_loc,
        hallway_allison_loc,
        hallway_sword_loc,
        hallway_armour_loc,
        hallway_shield_loc,
        hallway_lighting_loc,
    ]
    )

label main_hall:
    scene hallway bg
    show hallway_fire
    #show hallway_lighting
    show screen map(main_hall_map)
    pause
    jump main_hall

label hallway_doomarmor:
    burn "This armor...."
    burn "They said it was called doom armor?"
    burn "I have no clue who Doom is, and I just brough it from the most luxury merchandise"
    burn "I'll just take this armor and sell it, I see no use of it. . . . ."
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

label hallway_allison:
    if allison_story == 0:
        jump allison_event1
    else:
        burn "I already talked to her.. need to find ways to make big money !"
    jump main_hall

label hallway_sword:
    burn "A default looking sword.. i could pick this up."
    jump main_hall


