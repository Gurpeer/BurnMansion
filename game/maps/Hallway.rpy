default hallway_hall_loc = place("Hall Door", (639, 354), Jump('front_hall'), "maps/hallway/hall door.png")
default hallway_left_loc = place("Hall Left", (0, 118), Jump('hallway_hall_left'), "maps/hallway/left door.png")
default hallway_bathroom_loc = place("Hall Bathroom", (285, 243), Jump('bathroom'), "maps/hallway/bathroom door.png")
default hallway_office_loc = place("Hall Office", (1078, 42), Jump('office'), "maps/hallway/office door.png")


default main_hall = maps(
    "Hallway",
    [
        hallway_hall_loc,
        hallway_left_loc,
        hallway_bathroom_loc,
        hallway_office_loc,
        # office_firecamp_loc,
        # office_picture_loc,
        # office_arrow_loc,
    ]
    )

label main_hall:
    scene hallway bg
    show screen map(main_hall)
    pause

label hallway_hall_left:
    burn "Burn room still in progress. ."
    jump main_hall

# label office_weylon:
#     burn "How much would you pay for a Weylon?"
#     jump office

# label office_firecamp:
#     burn "You can burn a body in it."
#     jump office

# label office_picture:
#     burn "Ah, yessss, my great grand dad! he's for sale."
#     jump office




