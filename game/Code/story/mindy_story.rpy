
label mindy_event1:
    $ burns_face = "normal"
    $ mindy_face = "normal"
    # hide screen map
    # scene hallway bg_blur
  #  pause
    show burn_base onlayer over_screens at left with dissolve
    $ front_hall_map.rem(fhall_mindy_loc)
    $ front_hall_map.rem(fhall_smoke_loc)
    show mindy_base onlayer over_screens at right with dissolve

    $ burns_face = "normal_t"    
    burn "Hello, Mindy Simmons"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy "Hi, mr. burns"
    $ burns_face = "hmm"
    $ mindy_face = "normal"
    burn "You seem to be... taking it easy, as the youngsters say"
    burn "Do you not have anything to do?"
    $ burns_face = "normal_t"
    $ mindy_face = "confuset"
    mindy "Well, I'm not really sure what I should do. So I'll just sit around for now"
    $ burns_face = "hmm"
    $ mindy_face = "normal"
    burn "Aren't you a maid?! Go do some maid's work"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy "What do maid usually do ?"
    $ burns_face = "normal_t"
    $ mindy_face = "normal"
    burn "how am I supposed to know? I’ve never been one! That said, unlike the other two whom I… scouted, you applied to this job on your own free will. Why is that"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy ". . . after a time of unsuccessful freelancing , I kinda got short on money, and I don't want to be a burden to my relative so I was a little desperate."
    mindy "In the end, here I am working as a maid. Not sure what to work on though"
    $ burns_face = "normal_t"
    $ mindy_face = "angry1"
    burn "Oh, so you were a freelancer huh? Wait a minute, I remember you! You used to work at the town's nuclear power plant"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy "Well yeah"
    mindy "I used to, but not anymore"
    $ burns_face = "hmm"
    $ mindy_face = "angry1"
    burn "What happened ?"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy "You fired me, sir. . . Actually you fired everyone"
    $ mindy_face = "normal"
    $ burns_face = "smirkleft"
    pause
    $ burns_face = "normal_t"
    burn "Oh, uh. . . I did, huh"
    $ mindy_face = "normalt"
    mindy "Yep, you sure did mr. burns"
    $ mindy_face = "angry1"
    $ burns_face = "normal_t"
    burn ". . . .. . well, you just. . . enjoy your day then"
    $ mindy_face = "confuset"
    $ burns_face = "normal"
    mindy "Will do sir"
    $ mindy_face = "normal"

    hide burn_base onlayer over_screens at left with dissolve
    hide mindy_base onlayer over_screens at right with dissolve
    $ front_hall_map.discover(fhall_mindy_loc)
    $ front_hall_map.discover(fhall_smoke_loc)
    $ mindy_story += 1
    jump front_hall

