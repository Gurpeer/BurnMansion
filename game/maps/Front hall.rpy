﻿image mindy_smoke:
    "char/mindy/smoke.png"
    pause 0.21
    "char/mindy/smoke1.png"
    pause 0.21
    "char/mindy/smoke2.png"
    pause 0.21
    "char/mindy/smoke3.png"
    pause 0.21
    "char/mindy/smoke5.png"
    pause 1.5
    repeat

default fhall_front_door_loc = place("Front door", (881, 531), Jump('front_mansion'), "maps/front hallway/front door.png")
default fhall_mindy_loc = place("Mindy", (141, 499), Jump('fhall_mindy'), "maps/front hallway/mindy.png")
#default fhall_entrance = place("entrance", (1075, 469), Jump('fhall_entrance'), "maps/front hallway/middle_entrance.png")
default fhall_ldoor_loc = place("left door", (217, 52), Jump('fhall_ldoor'), "maps/front hallway/left door.png")
default fhall_rdoor_loc = place("right door", (1546, 50), Jump('fhall_rdoor'), "maps/front hallway/right door.png")
default fhall_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")

default fhall_shield_loc = place("black shield", (1333, 95), Jump('fhall_black_shield'), "maps/front hallway/shield.png")

default fhall_demonpic_loc = place("Demon lord", (0, 106), Jump('fhall_demon'), "maps/front hallway/demon pic.png")

default fhall_queenpic_loc = place("Queen", (673, 479), Jump('fhall_queen'), "maps/front hallway/queen.png")

default ashley_sweep_loc = place("Ashley", (1183, 422), Jump('fhall_ashley'), "maps/front hallway/ashley_sweep.png")

default fhall_kingpic_loc = place("King", (501, 425), Jump('fhall_king'), "maps/front hallway/king pic.png")

default fhall_smoke_loc = place("smoke", (155, 510), None, "mindy_smoke")


default front_hall_map = maps(
    "Front Hall",
    [
        fhall_front_door_loc,
        fhall_mindy_loc,
     #   fhall_entrance,
        fhall_ldoor_loc,
        fhall_rdoor_loc,
        fhall_arrow_loc,
        fhall_smoke_loc,
        fhall_kingpic_loc,
        fhall_queenpic_loc,
        fhall_demonpic_loc,
        fhall_shield_loc,

    ]
    )

label front_hall:
    if ashley_story == 5:
        $ front_hall_map.discover(ashley_sweep_loc)
        $ ashley_story += 1

    scene main hall bg
    show screen map(front_hall_map)
    pause
    jump front_hall

label fhall_queen:
    burn "Most beautiful and evil queen with wisdom"
    jump front_hall

label fhall_demon:
    burn "The demon himself who inherited the powers from Hell"
    jump front_hall

label fhall_king:
    burn "Beside his beautiful queen, he was probably the dumbest king and yet manage to maintain his kingdom in his era"
    jump front_hall

label fhall_black_shield:
    burn "This looks sellable"
    burn "pick up."
    jump front_hall

label fhall_ashley:
    if chamber_diamond_collected == False and ashley_story < 5:
        burn "I probably haven't unlocked the chamber or I'm missing something"
        jump front_hall
    elif chamber_diamond_collected == True and ashley_story == 6:
        jump ashley_event2
    else:
        burn ". . . probably haven't unlocked the chamber or I'm missing something"
        jump front_hall

label fhall_mindy:
    burn "Trigger first event dialogue."
    jump front_hall

# label fhall_entrance:
#     burn "Hi I'm entrance, cool. Not available yet"
#     jump front_hall

label fhall_ldoor:
    burn "Not available pop up box."
    jump front_hall

label fhall_rdoor:
    burn "Not available pop up box."
    jump front_hall



