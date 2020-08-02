default fmansion_guard_loc = place("Guard", (1048, 310), Jump('fmansion_guard'), "maps/front mansion/guard_figure.png")
default fmansion_guard1_loc = place("Guard 1", (503, 307), NullAction(), "maps/front mansion/guard1.png")
default fmansion_ladder_loc = place("Ladder", (1296, 377), Jump('fmansion_ladder'), "maps/front mansion/ladder.png")
default fmansion_mailbox_loc = place("Mail", (334, 470), Jump('fmansion_mail'), "maps/front mansion/mailbox.png")
default fmansion_money_loc = place("Money", (401, 686), Jump('fmansion_money'), "maps/front mansion/outside mansion money.png")
default fmansion_door_loc = place("Door", (609, 283), Jump('front_hall'), "maps/front mansion/door.png")
default fmansion_bluegem_loc = place("BlueGem", (255,642), Jump("fmansion_bluegem"), "maps/front mansion/blue_gem.png")
default fmansion_exit_loc = place("Exit", (545, 966), Jump('fmansion_exit'), "maps/front mansion/exit stair.png")

transform jill_position:
    xalign 0.70
    ypos .6


default front_mansion_map = maps(
    "Front Mansion",
    [
        fmansion_door_loc,
        fmansion_money_loc,
        fmansion_ladder_loc,
        fmansion_mailbox_loc,
        fmansion_guard_loc,
        fmansion_guard1_loc,
        fmansion_bluegem_loc,
        fmansion_exit_loc,

    ]
    )

label front_mansion:
    scene outside mansion bg
    show screen map(front_mansion_map)
    pause
    jump front_mansion

label fmansion_guard:
    if guard_dialogue == 0:
        $ front_mansion_map.rem(fmansion_guard_loc)
        $ front_mansion_map.rem(fmansion_guard1_loc)
        show burn_base onlayer screens at left with dissolve
        show jack_base onlayer screens at right with dissolve
        show jill_base onlayer screens at jill_position with dissolve
        $ jack_face = "talk"
        jack "Howdy Sir"
        $ burns_face = "normal_t"
        $ jack_face = "normal"
        burn "Good day, both of you"
        $ burns_face = "normal_t"
        $ jill_face = "talk"
        jill "What are you thinkin boss ?"
        $ jill_face = "normal"
        burn "Thinking of something useful today"
        $ jack_face = "talk"
        $ burns_face = "normal"
        jack "Something useful sir ? Like what"
        $ burns_face = "normal_t"
        burn "cheap workforce with low wage, or fuel for the generator, keh keh keh"
        $ burns_face = "normal"
        jack "generator? We haven’t seen anything like that around here"
        $ jack_face = "talk"
        $ burns_face = "normal_t"
        burn "of course not, it’s underground. Maybe one day you’ll get to see it… as fuel that is. Hahaha"
        $ jack_face = "normal"
        $ burns_face = "normal"
        $ jill_face = "talk"
        jill "hey, thanks for the kind offer boss, but I think I’ll stay with guarding the door"
        $ jack_face = "talk"
        $ jill_face = "normal"
        $ burns_face = "normal"
        jack "Not like we're actual guards or something anyways"
        $ jack_face = "normal"
        $ jill_face = "normal"
        $ burns_face = "normal_t"
        burn "Of course not. Why would I waste my money on hiring real professionals? Just stay there and act like you care"
        $ jack_face = "talk"
        $ burns_face = "normal"
        jack "Yes sir, sounds easy enough"
        $ jack_face = "normal"
        $ burns_face = "normal_t"
        burn "Now, I must be off"
        $ jack_face = "talk"
        $ burns_face = "normal"
        jack "Good luck sir"
        $ jill_face = "talk"
        jill "See ya boss"
        $ jill_face = "normal"
        hide burn_base onlayer screens at left with dissolve
        hide jack_base onlayer screens at right with dissolve
        hide jill_base onlayer screens at jill_position with dissolve
        $ front_mansion_map.discover(fmansion_guard_loc)
        $ front_mansion_map.discover(fmansion_guard1_loc)
        $ guard_dialogue += 1
    else:
        jill "How is it goin sir"

    jump front_mansion

label fmansion_mail:
    if mail_ashley_business_suit == True:

        "There is a item in the mail"
        show ashley_business_outfit_item_frame onlayer screens
        "Obtained Ashley's Business Suit"
        hide ashley_business_outfit_item_frame onlayer screens
        $ player.got(ashley_business_suit, 1)        
        $ ashley_waist += 1
        $ mail_ashley_business_suit = False
        jump front_mansion

    burn "Nothing in the mailbox"
    jump front_mansion

label fmansion_ladder:
    burn "Ah ha, the ladder"
    show ladder_item_frame onlayer screens
    "Obtained a Ladder"
    hide ladder_item_frame onlayer screens
    $ front_mansion_map.rem(fmansion_ladder_loc)
    $ player.got(ladder_home, 1)
    jump front_mansion

label fmansion_bluegem:
    burn "A blue looking gem"
    show bluegem_item_frame onlayer screens
    "Obtained a blue diamond"
    hide bluegem_item_frame onlayer screens
    $ front_mansion_map.rem(fmansion_bluegem_loc)
    $ player.got(blue_gem, 1)
    jump front_mansion



# label fmansion_guard1:
#     burn "Howdy dude. "
#     jump front_mansion

label fmansion_money:
    "100 cash obtained"
    $ mr_burns.got_cash(100)
    $ front_mansion_map.rem(fmansion_money_loc)
    jump front_mansion

label fmansion_exit:
    burn "Nope, not leaving yet"
    jump front_mansion

