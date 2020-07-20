image fish_tank_move:
    "maps/burn room/fish_tank.png"
    xpos 1330 yalign .4
    xzoom 1.0
    linear 2 xpos renpy.random.randint(1300,1500) yalign .4
    xzoom -1.0
    linear 2 xpos renpy.random.randint(1295,1380) yalign .4
    xzoom 1.0
    linear 2 xpos renpy.random.randint(1200,1480) yalign .38
    xzoom -1.0
    linear 2 xpos renpy.random.randint(1205,1380) yalign .4
    # pause 2
    # xpos 1330 
    # linear 4 xpos renpy.random.randint(1200,1270) yalign .4

    repeat

image bubble_tank:
    "maps/burn room/bubble1.png" with dissolve
    .7
    "maps/burn room/bubble2.png" with dissolve
    .7
    "maps/burn room/bubble3.png" with dissolve
    .7
    "maps/burn room/bubble4.png" with dissolve
    .7
    pause .4
    repeat    



default burn_room_sword_loc = place("sword", (53, 484), Jump('burn_room_sword'), "maps/burn room/knight sword.png")
default burn_room_camera_loc = place("camera", (1419, 727), Jump('burn_room_camera'), "maps/burn room/camera.png")
default burn_room_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")
default burn_room_bed_loc = place("bed", (650, 558), Jump('burn_room_bed'), "maps/burn room/bed.png")
default burn_room_mask_loc = place("beard mask", (749, 402), Jump('burn_room_beardmask'), "maps/burn room/beard mask.png")
#default burn_room_sword_loc = place("fire", (0, 0), None, "office_fire")

default burn_room_map = maps(
    "Office",
    [
        burn_room_sword_loc,
        burn_room_camera_loc,
        burn_room_arrow_loc,
        burn_room_bed_loc,
        burn_room_mask_loc,
    ]
    )

label burn_room:
    scene burn room bg
    show water_tank
    show fish_tank_move
    show bubble_tank
    show water_frame
    show screen map(burn_room_map)
    pause
    jump burn_room

label burn_room_sword:
    burn "A knight sword, but it looks pretty heavy to carry.."
    jump burn_room

label burn_room_camera:
    burn "Oh yes, forgot I had a small sqaured camera"
    burn "If I have the sneaky advantage and timing to place this camera somewhere secretly..."
    burn "I could be watching a premium nudity .. HAHAHA HA!"
    burn "*coughh* *cough*.. ahh...."
    jump burn_room


label burn_room_bed:
    burn "Don't really feel sleepy yet"
    jump burn_room

label burn_room_beardmask:
    burn "This is definitly sellable"
    burn "Hell, this mask was a purchase from Zues himself"
    burn "Don't know why he was selling these kind of mask"
    burn "It probably had some sort of abilites or passive traits , but... I wore this and it does nothing..."
    jump burn_room