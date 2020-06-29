default fmansion_guard_loc = place("Guard", (1048, 310), Jump('fmansion_guard'), "maps/front mansion/guard_figure.png")
default fmansion_guard1_loc = place("Guard 1", (503, 307), Jump('fmansion_guard1'), "maps/front mansion/guard1.png")
default fmansion_money_loc = place("Money", (397, 743), Jump('fmansion_money'), "maps/front mansion/money.png")
default fmansion_door_loc = place("Door", (532, 0), Jump('front_hall'), "maps/front mansion/door.png")
default fmansion_exit_loc = place("Exit", (355, 958), Jump('fmansion_exit'), "maps/front mansion/exit stair.png")




default front_mansion_map = maps(
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
    show screen map(front_mansion_map)
    pause
    jump front_mansion

label fmansion_guard:
    burn "Sup dude. "
    jump front_mansion

label fmansion_guard1:
    burn "Howdy dude. "
    jump front_mansion

label fmansion_money:
    $ mr_burns.got_cash(300)
    $ front_mansion_map.rem(fmansion_money_loc)
    jump front_mansion

label fmansion_exit:
    burn "Nope, not leaving yet"
    jump front_mansion

