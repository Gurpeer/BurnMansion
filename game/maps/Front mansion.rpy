default fmansion_guard_loc = place("Guard", (1048, 340), Jump('fmansion_guard'), "maps/front mansion/guard h.png")
default fmansion_guard1_loc = place("Guard 1", (503, 307), Jump('fmansion_guard1'), "maps/front mansion/guard1 h.png")
default fmansion_money_loc = place("Money", (397, 743), Jump('fmansion_money'), "maps/front mansion/money h.png")
default fmansion_door_loc = place("Money", (535, 0), Jump('front_hall'), "maps/front mansion/door.png")
default fmansion_exit_loc = place("Exit", (360, 960), Jump('fmansion_exit'), "maps/front mansion/exit stair.png")




default front_mansion = maps(
    "Front Mansion",
    [
        fmansion_door_loc,
        fmansion_guard_loc,
        fmansion_guard1_loc,
        fmansion_money_loc,
        fmansion_exit_loc,

    ]
    )

label front_mansion:
    scene outside mansion bg
    show screen map(front_mansion)
    pause

label fmansion_guard:
    burn "Sup dude. "
    jump front_mansion

label fmansion_guard1:
    burn "Howdy dude. "
    jump front_mansion

label fmansion_money:
    burn "I'm money, please take me. "
    jump front_mansion

label fmansion_exit:
    burn "Nope, not leaving yet"
    jump front_mansion

