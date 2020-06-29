default bathroom_door_loc = place("Door", (445, 244), Jump('main_hall'), "maps/bathroom/washroom door.png")
default bathroom_lock_loc = place("Lock", (1076, 622), Jump('bathroom_lock'), "maps/bathroom/washroom lock.png")
default bathroom_clay_loc = place("Clay", (315, 394), Jump('bathroom_clay'), "maps/bathroom/washroom clay_guy.png")
default bathroom_ashley_loc = place("Ashley", (766, 346), Jump('bathroom_ashley'), "maps/bathroom/washroom ashley.png")


default bathroom_map = maps(
    "Bathroom",
    [
        bathroom_door_loc,
        bathroom_lock_loc,
        bathroom_clay_loc,
        bathroom_ashley_loc,

    ]
    )

label bathroom:
    scene washroom bg
    show screen map(bathroom_map)
    pause
    jump bathroom

label bathroom_lock:
    burn "looks like a lock."
    jump bathroom

label bathroom_clay:
    burn "Please take me."
    jump bathroom

label bathroom_ashley:
    burn "Triggers first event scene dialogue."
    jump bathroom



