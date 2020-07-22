# image bird_move:
#     "maps/office/office_bird.png"
#     xpos 800 yalign .2
#     linear 4 xpos renpy.random.randint(240,315) yalign .2
#     pause 2
#     xpos 800 yalign .2
#     linear 4 xpos renpy.random.randint(260,353) yalign .3
#     pause 2
#     repeat


# image office_fire:
#     "maps/office/fire1.png" with dissolve
#     .3
#     "maps/office/fire2.png" with dissolve
#     .3
#     "maps/office/fire3.png" with dissolve
#     .3
#     "maps/office/fire4.png" with dissolve
#     .3
#     "maps/office/fire5.png" with dissolve
#     .3
#     repeat

default chamber_entrance_door_loc = place("Locked Door", (602, 192), Jump('chamber_entrance_door'), "location/chamber entrance/chamber entrance door.png")
default chamber_entrance_exit_loc = place("Exit entrance", (755, 1047), Jump('office'), "location/chamber entrance/chamber exit.png")

# default office_fire_loc = place("fire", (0, 0), None, "office_fire")

default chamber_entrance_map = maps(
    "Chamber entrance",
    [
    #    "chamber insert",
        # "office_sky",
        # "bird_move",
        # "office_sky_wood",
        chamber_entrance_door_loc,
        "chamber insert",
        chamber_entrance_exit_loc,


    ]
    )


label chamber_entrance:
    scene chamber entrance bg
    show screen map(chamber_entrance_map)
    pause
    jump chamber_entrance



label chamber_entrance_door:
    jump chamber

# label office_football:
#     burn "Ahh HA, a signed football"
#     burn "This will definitly sell me some good price !"
#     $ office_map.rem(office_football_loc)
#     jump office
