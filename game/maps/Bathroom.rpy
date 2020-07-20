image bathroom_air:
    "maps/bathroom/air.png" with dissolve
    .9
    "maps/bathroom/air2.png" with dissolve
    .8
    "maps/bathroom/air3.png" with dissolve
    .9
    repeat    


default bathroom_door_loc = place("Door", (859, 519), Jump('main_hall'), "maps/bathroom/washroom door.png")
default bathroom_lock_loc = place("Lock", (704, 210), Jump('bathroom_lock'), "maps/bathroom/washroom lock.png")
# default bathroom_clay_loc = place("Clay", (315, 394), Jump('bathroom_clay'), "maps/bathroom/washroom clay_guy.png")
default bathroom_ashley_loc = place("Ashley", (766, 346), Jump('bathroom_ashley'), "maps/bathroom/washroom ashley.png")
default bathroom_s_candle_loc = place("s_candle", (1746, 444), Jump('bathroom_s_candle'), "maps/bathroom/s_candle.png")
default bathroom_towel_loc = place("Towel", (1055, 476), Jump('bathroom_towel'), "maps/bathroom/towel.png")
default bathroom_bathtub_loc = place("Bathtub", (1281, 839), Jump('bathroom_bathtub'), "maps/bathroom/washroom_tub.png")


default bathroom_map = maps(
    "Bathroom",
    [
        bathroom_door_loc,
        bathroom_lock_loc,
        bathroom_s_candle_loc,
        bathroom_towel_loc,
        bathroom_bathtub_loc,
        # bathroom_clay_loc,
        # bathroom_ashley_loc,

    ]
    )

label bathroom:
    scene washroom bg
    show bathroom_air
    show screen map(bathroom_map)
    pause
    jump bathroom

label bathroom_lock:
    burn "looks like a lock and... I can't even get up there"
    burn "Might need to find a ladder or some kind to reach it"
    jump bathroom

label bathroom_clay:
    burn "Please take me."
    jump bathroom

label bathroom_s_candle:
    burn "A s candle"
    burn "I smell great price with this !"
    jump bathroom

label bathroom_towel:
    burn " . . . ."
    burn "Doesn't look pricey ..."
    burn "Nope"
    jump bathroom

label bathroom_bathtub:
    burn "Ah, yes. The relaxation that water has"
    burn "But, not in the mood for this"
    jump bathroom

# label bathroom_ashley:
#     burn "Triggers first event scene dialogue."
#     jump bathroom



