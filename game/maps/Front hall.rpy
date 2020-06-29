image mindy_smoke:
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

default fhall_front_door_loc = place("Front door", (889, 594), Jump('front_mansion'), "maps/front hallway/front door.png")
default fhall_mindy_loc = place("Mindy", (141, 499), Jump('fhall_mindy'), "maps/front hallway/mindy.png")
default fhall_entrance = place("entrance", (1075, 469), Jump('fhall_entrance'), "maps/front hallway/middle_entrance.png")
default fhall_ldoor_loc = place("left door", (237, 106), Jump('fhall_ldoor'), "maps/front hallway/left door.png")
default fhall_rdoor_loc = place("right door", (1543, 119), Jump('fhall_rdoor'), "maps/front hallway/right door.png")
default fhall_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")
default fhall_smoke_loc = place("smoke", (155, 510), None, "mindy_smoke")

default front_hall_map = maps(
    "Front Hall",
    [
        fhall_front_door_loc,
        fhall_mindy_loc,
        fhall_entrance,
        fhall_ldoor_loc,
        fhall_rdoor_loc,
        fhall_arrow_loc,
        fhall_smoke_loc,
    ]
    )

label front_hall:
    scene main hall bg
    show screen map(front_hall_map)
    pause
    jump front_hall

label fhall_mindy:
    burn "Trigger first event dialogue."
    jump front_hall

label fhall_entrance:
    burn "Hi I'm entrance, cool. Not available yet"
    jump front_hall

label fhall_ldoor:
    burn "Not available pop up box."
    jump front_hall

label fhall_rdoor:
    burn "Not available pop up box."
    jump front_hall



