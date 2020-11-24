# image burn_base normal = ConditionSwitch(
#     "_last_say_who == 'burn'", "char/burn/01/face normal_t.png",
#     "not _last_say_who == 'burn'", "char/burn/01/face normal.png",
#     )

image side burn = "char/burn/icon.png"



# image mindy normal = ConditionSwitch(
#     "_last_say_who == 'mindy'", "char/mindy/normal_t.png",
#     "not _last_say_who == 'mindy'", "char/mindy/normal.png",
#     )
image side mindy = "char/mindy/icon.png"

# image weylon normal = ConditionSwitch(
#     "_last_say_who == 'weylon'", "char/weylon/normal_t.png",
#     "not _last_say_who == 'weylon'", "char/weylon/normal.png",
#     )

# image weylon scared = ConditionSwitch(
#     "_last_say_who == 'weylon'", "char/weylon/scared_t.png",
#     "not _last_say_who == 'weylon'", "char/weylon/scared.png",
#     )


image side weylon = "char/weylon/icon.png"

# image ashley normal = ConditionSwitch(
#     "_last_say_who == 'ashley'", "char/ashley/normal_t.png",
#     "not _last_say_who == 'ashley'", "char/ashley/normal.png",
#     )
# image ashley angry = ConditionSwitch(
#     "_last_say_who == 'ashley'", "char/ashley/angry_t.png",
#     "not _last_say_who == 'ashley'", "char/ashley/angry.png",
#     )
# image side ashley = "char/ashley/icon.png"

# image allison normal = ConditionSwitch(
#     "_last_say_who == 'allison'", "char/allison/normal_t.png",
#     "not _last_say_who == 'allison'", "char/allison/normal.png",
#     )
# image allison angry = ConditionSwitch(
#     "_last_say_who == 'allison'", "char/allison/angry_t.png",
#     "not _last_say_who == 'allison'", "char/allison/angry.png",
#     )

image allison surprise = "char/allison/surprise.png"

image side allison = "char/allison/icon.png"

image gui_input_mc = "gui/mc_input_gui.png"

#chamber stuff
# default chamber_access = False
default check_door = False
default office_firecamp_key = False
default office_firecamp_open = False
default chamber_diamond_collected = False

## MC
default mc_name = "Roger"

## Seller NPC
default seller_call = False
default seller_npc = False


# Story P
default story_event = 0
# ## Allison Event story
# default allison_story = 0

# ## Mindy Event Story
# default mindy_story = 0

# ## Ashley Event Story
# default ashley_story = 0
# default ashley_dominance = 0
# default ask_instrument = 0
# default mail_ashley_business_suit = False
# default ashley_waist = 0
# default ashley_call_burn = "Sir"
# default left_leg_pain = 0
# default right_leg_pain = 0

# ## progress bar
# default progress_bar = 0

# ## Guards
# default guard_dialogue = 0

define burn = Character("MR BURN", color="#ffff", who_outlines=[ (3, "#000") ], box_box_reverse = True, namebox_xalign=0.0)
define burn1 = Character("Burn", color="#fe4911", who_outlines=[ (1, "#ffffff") ])

define yes_men = Character("YESMEN", color="#ffff", who_outlines=[ (3, "#000") ])

define yes_men1 = Character("YESMEN1", color="#ffff", who_outlines=[ (3, "#000") ])

define yes_men2 = Character("YESMEN2", color="#ffff", who_outlines=[ (3, "#000") ])

define yes_men3 = Character("YESMEN3", color="#ffff", who_outlines=[ (3, "#000") ])

define yes_men4 = Character("YESMEN4", color="#ffff", who_outlines=[ (3, "#000") ])

define larry = Character("LARRY", color="#ff4676", who_outlines=[ (3, "#000") ])

define mc = Character("[mc_name]", color="ff6600", who_outlines=[ (3, "#000") ])

define jack = Character("Jack", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define jill = Character("Jill", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define mindy = Character("Mindy", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define scratchy = Character("Scratchy", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define ashley = Character("Ashley", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define allison = Character("Allison", color="#ff69b4", who_outlines=[ (3, "#ffffff") ])
define seller = Character("Seller", color="#ffff", who_outlines=[ (3, "#ffffff") ])
define weylon = Character("SMITHERS", color="#ffff", who_outlines=[ (3, "#000") ])

define grace = Character("GRACE", color="#ffff", who_outlines=[ (3, "#000") ])

# default burns_face = "angry"
# default burns_hands = "1"
# default burns_holding = "cash"
# image burn = Composite((471,741),
#     (0,0), "char/burn/01/base 1.png",
#     (0,0), "char/burn/01/face [burns_face].png",
#     (0,0), "char/burn/01/hands [burns_hands].png",
#     (0,0), "char/burn/01/holding [burns_holding].png",
# )
screen mc_name_input():
  hbox:
    xalign .5
    yalign .56

    #text "{b}{color=#faebd7}Input:  {/color}{/b}"
    input:
      value VariableInputValue("mc_name", default=True, returnable=True)
      default "TYPE ME"
      color "#000000"
     # bold True
      size 80
      length 9

# The game starts here.

label start:
    window hide
    stop music

    scene black with dissolve
    pause .5

    scene office bg
    $ office_map.rem(office_weylon_loc)
    show screen map(office_map)
  #  show yes_men_burn_figure
    play music "audio/burn_jukebox.mp3"
    yes_men1 "{i}*Whispering*{/i} ...secret meeting of some sort?"
    yes_men2 "{i}*Muttering*{/i} ...not sure why we got called in for..."
    yes_men3 "{i}*Mumbling*{/i} ...some kinda announcement maybe, but..."
    yes_men4 "{i}*Bickering*{/i} ...no, I didn't eat the last donut, dammit, it was that fat-!"
    burn "Silence! Enough of your barely audible conjecturing!"
    yes_men ". . ."
    burn "very good.{p}Now then gentleman, I'm sure you pencil pushing sycophants are all terribly curious to know why I've assembled you together so urgently"
    yes_men "Yes sir, Mr Burns, sir."
    burn "Well, the real answer may take some lengthy explaining to do, but the gist of it is..."
    burn "I'm retiring"
    yes_men "{i}W-what?!{/i}"
    yes_men2 "B-but Mr. Burns, you're still at the peak of your career!"
    yes_men4 "The prime of your life!"
    yes_men1 "The cream of your crop!"
    burn "Yes, yes, my good looks and youthful vibrance may have fooled most of you men. And I do still feel I have {i}so{/i} much more cruel and unusual punishment to dispense"
    burn "...and I'll still be getting out the occasional releasing of the hounds not to worry..."
    burn "But the truth of the matter is, I'm getting old.{p}Only once you've hit over 130 birthdays do the twilight years of your life start to come into view..."
    $ office_map.rem(office_yes_men)
    jump story_1


    return
