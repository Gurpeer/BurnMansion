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

default chamber_bed_loc = place("Bed", (1147, 501), Jump('chamber_bed'), "location/Chamber/chamber bed.png")
default chamber_door_loc = place("Door", (518, 317), Jump('chamber_entrance'), "location/Chamber/chamber door.png")
default chamber_picture_loc = place("Demon Titan", (1390, 120), Jump('chamber_titan'), "location/Chamber/chamber picture.png")
default chamber_dildo_loc = place("Dildo", (1284, 243), Jump('chamber_dildo'), "location/Chamber/dildo chamber.png")
default chamber_eye_blind_loc = place("Eye Blind", (944, 349), Jump('chamber_eyeblind'), "location/Chamber/eye patch chamber.png")
default chamber_perfume_loc = place("Unconscious Perfume", (1056, 484), Jump('chamber_perfume'), "location/Chamber/unconsious perfume.png")
default chamber_vibrator_loc = place("Vibrator", (1255, 261), Jump('chamber_vibrator'), "location/Chamber/vibrator chamber.png")
#default chamber_entrance_exit_loc = place("Exit entrance", (755, 1047), Jump('office'), "location/chamber entrance/chamber exit.png")

# default office_fire_loc = place("fire", (0, 0), None, "office_fire")

default chamber_map = maps(
    "Chamber",
    [
        # "office_sky",
        # "bird_move",
        # "office_sky_wood",
        chamber_bed_loc,
        chamber_door_loc,
        chamber_picture_loc,
        chamber_dildo_loc,
        chamber_eye_blind_loc,
        chamber_perfume_loc,
        chamber_vibrator_loc,
   #     chamber_entrance_exit_loc,


    ]
    )


label chamber:
    scene chamber bg
    show screen map(chamber_map)
    pause
    jump chamber

label chamber_vibrator:
    burn "Hmmm.... this could be handy in the future"
    jump chamber

label chamber_dildo:
    burn "pick up."
    jump chamber

label chamber_eyeblind:
    burn ".. what could I use this for. . ?"
    burn "*for Allison storyline.*"
    jump chamber

label chamber_perfume:
    burn "Pick up"
    jump chamber

label chamber_bed:
    burn "The very place where... I"
    burn "do some very unusual sexual activites"
    jump chamber

label chamber_titan:
    burn "The demon titan, this being was a giant and had cosmic power to obliterate any tiny planets or.. just with his hands"
    jump chamber

# label office_football:
#     burn "Ahh HA, a signed football"
#     burn "This will definitly sell me some good price !"
#     $ office_map.rem(office_football_loc)
#     jump office
