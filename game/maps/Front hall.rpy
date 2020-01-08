default fhall_front_door_loc = place("Front door", (885, 533), Jump('front_mansion'), "maps/front hallway/front door.png")
default fhall_mindy_loc = place("Mindy", (141, 499), Jump('fhall_mindy'), "maps/front hallway/mindy.png")
default fhall_sword_loc = place("sword", (1364, 329), Jump('fhall_sword'), "maps/front hallway/sword.png")
default fhall_ldoor_loc = place("left door", (219, 63), Jump('fhall_ldoor'), "maps/front hallway/left door.png")
default fhall_rdoor_loc = place("right door", (1565, 0), Jump('fhall_rdoor'), "maps/front hallway/right door.png")
default fhall_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")

default front_hall_map = maps(
    "Office",
    [
        fhall_front_door_loc,
        fhall_mindy_loc,
        fhall_sword_loc,
        fhall_ldoor_loc,
        fhall_rdoor_loc,
        fhall_arrow_loc,

    ]
    )

label front_hall:
    scene main hall bg
    show screen map(front_hall_map)
    pause

label fhall_mindy:
    burn "Trigger first event dialogue."
    jump front_hall

label fhall_sword:
    burn "Hi I'm a sword, and I'm for sale. Thank you."
    jump front_hall

label fhall_ldoor:
    burn "Not available pop up box."
    jump front_hall

label fhall_rdoor:
    burn "Not available pop up box."
    jump front_hall



