image burn_base normal = ConditionSwitch(
    "_last_say_who == 'burn'", "char/burn/01/face normal_t.png",
    "not _last_say_who == 'burn'", "char/burn/01/face normal.png",
    )

image side burn = "char/burn/icon.png"



image mindy normal = ConditionSwitch(
    "_last_say_who == 'mindy'", "char/mindy/normal_t.png",
    "not _last_say_who == 'mindy'", "char/mindy/normal.png",
    )
image side mindy = "char/mindy/icon.png"

image weylon normal = ConditionSwitch(
    "_last_say_who == 'weylon'", "char/weylon/normal_t.png",
    "not _last_say_who == 'weylon'", "char/weylon/normal.png",
    )

image weylon angry = ConditionSwitch(
    "_last_say_who == 'weylon'", "char/weylon/angry_t.png",
    "not _last_say_who == 'weylon'", "char/weylon/angry.png",
    )


image side weylon = "char/weylon/icon.png"

image ashley normal = ConditionSwitch(
    "_last_say_who == 'ashley'", "char/ashley/normal_t.png",
    "not _last_say_who == 'ashley'", "char/ashley/normal.png",
    )
image ashley angry = ConditionSwitch(
    "_last_say_who == 'ashley'", "char/ashley/angry_t.png",
    "not _last_say_who == 'ashley'", "char/ashley/angry.png",
    )
image side ashley = "char/ashley/icon.png"

image allison normal = ConditionSwitch(
    "_last_say_who == 'allison'", "char/allison/normal_t.png",
    "not _last_say_who == 'allison'", "char/allison/normal.png",
    )
image allison angry = ConditionSwitch(
    "_last_say_who == 'allison'", "char/allison/angry_t.png",
    "not _last_say_who == 'allison'", "char/allison/angry.png",
    )

image allison surprise = "char/allison/surprise.png"

image side allison = "char/allison/icon.png"



## Allison Event story
default allison_story = 0



define burn = Character("Burn", color="#fe4911", who_outlines=[ (3, "#ffffff") ], image="burn", box_box_reverse = True, namebox_xalign=0.0)
define burn1 = Character("Burn", color="#fe4911", who_outlines=[ (3, "#ffffff") ], image="burn")
define yes_men = Character("Yes men")
define mindy = Character("Mindy", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="mindy")
define ashley = Character("Ashley", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="ashley")
define allison = Character("Allison", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="allison")
define weylon = Character("Weylon", color="#006400", who_outlines=[ (3, "#ffffff") ], image="weylon")

# default burns_face = "angry"
# default burns_hands = "1"
# default burns_holding = "cash"
image burn = Composite((471,741),
    (0,0), "char/burn/01/base 1.png",
    (0,0), "char/burn/01/face [burns_face].png",
    (0,0), "char/burn/01/hands [burns_hands].png",
    (0,0), "char/burn/01/holding [burns_holding].png",
)


# The game starts here.

label start:
    window hide
    show burn at left
    "sdsdsd"
    $ burns_face = "normal"
    "sdsd"
    jump story_1

    return
