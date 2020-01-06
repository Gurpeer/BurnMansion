default hallway_hall_loc = place("Hall Door", (639, 354), Jump('front_hall'), "maps/hallway/hall door.png")
default hallway_left_loc = place("Hall Left", (0, 118), Jump('hallway_hall_left'), "maps/hallway/left door.png")
default hallway_bathroom_loc = place("Hall Bathroom", (285, 243), Jump('bathroom'), "maps/hallway/bathroom door.png")
default hallway_office_loc = place("Hall Office", (1078, 42), Jump('office'), "maps/hallway/office door.png")
default hallway_allison_loc = place("Aliison", (978, 266), Jump('hallway_allison'), "maps/hallway/allison n.png")

default main_hall_map = maps(
    "Hallway",
    [
        hallway_hall_loc,
        hallway_left_loc,
        hallway_bathroom_loc,
        hallway_office_loc,
        hallway_allison_loc,
    ]
    )

label main_hall:
    scene hallway bg
    show screen map(main_hall_map)
    pause

label hallway_hall_left:
    burn "Burn room still in progress. ."
    jump main_hall

label hallway_allison:
    burn "Trigger first event."
    jump main_hall


