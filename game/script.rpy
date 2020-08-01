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

image weylon scared = ConditionSwitch(
    "_last_say_who == 'weylon'", "char/weylon/scared_t.png",
    "not _last_say_who == 'weylon'", "char/weylon/scared.png",
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


#chamber stuff
# default chamber_access = False
default check_door = False
default office_firecamp_key = False
default office_firecamp_open = False
default chamber_diamond_collected = False

## Seller NPC
default seller_call = False
default seller_npc = False

## Allison Event story
default allison_story = 0

## Ashley Event Story
default ashley_story = 0

## Guards
default guard_dialogue = 0


define burn = Character("Burn", color="#fe4911", who_outlines=[ (3, "#ffffff") ], image="burn", box_box_reverse = True, namebox_xalign=0.0)
define burn1 = Character("Burn", color="#fe4911", who_outlines=[ (3, "#ffffff") ], image="burn")
define yes_men = Character("Yes men")
define jack = Character("Jack", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="jack")
define jill = Character("Jill", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="jill")
define mindy = Character("Mindy", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="mindy")
define scratchy = Character("Scratchy", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="scrathy")
define ashley = Character("Ashley", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="ashley")
define allison = Character("Allison", color="#ff69b4", who_outlines=[ (3, "#ffffff") ], image="allison")
define seller = Character("Seller", color="#ffff", who_outlines=[ (3, "#ffffff") ], image="seller")
define weylon = Character("Weylon", color="#006400", who_outlines=[ (3, "#ffffff") ], image="weylon")

# default burns_face = "angry"
# default burns_hands = "1"
# default burns_holding = "cash"
# image burn = Composite((471,741),
#     (0,0), "char/burn/01/base 1.png",
#     (0,0), "char/burn/01/face [burns_face].png",
#     (0,0), "char/burn/01/hands [burns_hands].png",
#     (0,0), "char/burn/01/holding [burns_holding].png",
# )


# The game starts here.

label start:
    window hide
    stop music
   #  show burn_base at left
   #  $ burns_hands = "3"
   #  "sdsdsd"
   #  # $ burns_face = "normal"
   #  "sdsd"

   #  show ashley_base at center
   #  pause
   #  $ ashley_face = "normalt"
   #  ashley "Hi"
   #  ashley "...nope"
   #  $ ashley_face = "angryt"
   #  ashley "BYE test."
   #  $ ashley_face = "angry"


   #  show mindy_base at girl_pos1
   #  pause
   #  $ mindy_face = "normalt"
   #  mindy "Hi"
   #  mindy "Just testing my rigg : )"
   #  $ mindy_face = "normal"

   #  show allison_base at midright
   #  pause
   #  $ allison_face = "normalt"
   #  allison "Hi !"
   #  allison "Also, testing my rig"
   # # $ allison_bra = "none"
   #  $ allison_clothe = "none"
   #  $ allison_face = "sleepy"
   #  allison "OK, bye"
   #  pause
   #  $ allison_wear = "eyepatch"
   #  allison "Also.. my eyepatch too"

    scene black with dissolve
    pause .5

    jump story_1 

    return
