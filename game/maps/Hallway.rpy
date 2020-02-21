default hallway_hall_loc = place("Hall Door", (636, 350), Jump('front_hall'), "maps/hallway/hall door.png")
default hallway_left_loc = place("Hall Left", (0, 118), Jump('hallway_hall_left'), "maps/hallway/burn door.png")
default hallway_bathroom_loc = place("Hall Bathroom", (282, 239), Jump('bathroom'), "maps/hallway/bathroom door.png")
default hallway_office_loc = place("Hall Office", (1085, 49), Jump('office'), "maps/hallway/office door.png")
default hallway_allison_loc = place("Aliison", (978, 266), Jump('hallway_allison'), "maps/hallway/allison.png")
default hallway_sword_loc = place("Sword", (1603, 794), Jump('hallway_sword'), "maps/hallway/sword.png")
default hallway_armour_loc = place("Armour", (829, 402), Jump('hallway_pickup'), "maps/hallway/armour.png")
default hallway_ball_loc = place("Ball", (189, 461), Jump('hallway_pickup'), "maps/hallway/ball.png")
default hallway_shield_loc = place("Shield", (0, 655), Jump('hallway_pickup'), "maps/hallway/shield.png")

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
        hallway_ball_loc,
        hallway_shield_loc
    ]
    )

label main_hall:
    scene hallway bg
    show screen map(main_hall_map)
    pause

label hallway_pickup:
    burn "Pick me up please, and thank you"
    jump main_hall

label hallway_hall_left:
    burn "Burn room still in progress. ."
    jump main_hall

label hallway_allison:
    if allison_story == 0:
        jump allison_event1
    else:
        burn "I already talked to her.. need to find ways to make big money !"
    jump main_hall

label hallway_sword:
    burn "A default looking sword.. i could pick this up."
    jump main_hall


