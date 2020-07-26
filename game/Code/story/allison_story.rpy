
label allison_event1:
    hide screen map
    scene hallway bg_blur
    pause
    show burn_base at left with dissolve
    $ burns_face = "normal"
    $ allison_face = "sleepy"
    $ burns_hands = "3"
    show allison_base at right with dissolve
    pause
    $ burns_face = "hmm"
    burn "Good day Allison Taylor"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "Oh hi there Mr. Burn"
    allison "Need something ?"
    $ burns_face = "normal_t"
    $ allison_face = "normal"
    burn "Not in particular, but I was wondering"
    burn "If you would be up for, ah . .. "
    burn "a little chat ?"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "Sure I guess"
    allison "What do you want to talk about ?"
    $ allison_face = "normal"
    $ burns_face = "hmm"
    $ burns_hands = "1"
    burn "Well, I was just wondering what made you start working here in the first place"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "sir, you grabbed me on the road and pulled me into your van"
    $ allison_face = "angry"
    pause
    $ allison_face = "angryt"
   # show allison angry at right
    allison "and then you brought me here and had me sign the contract without any explanations"
    $ allison_face = "angry"
    $ burns_face = "normal_t"
    $ burns_hands = "3"
    burn "oh, oh right. I guess I did huh"
    $ burns_face = "laugh"
    $ allison_face = "suprise"
   # show allison surprise at right
    burn "Hahahaaa"
    pause
    $ allison_face = "normalt"
    $ burns_face = "normal"
    #show allison normal at right
    allison "It's fine sir, I don't hold grudges"
    $ burns_face = "normal_t"
    burn "Well in that case, why don’t you tell me what you’re doing before working here?"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "I just finished my college class for the day and I planned to go to lisa’s house to work on our project"
    allison "Aah, she must be worried sick right now"
    $ allison_face = "normal"
    $ burns_face = "normal_t"
    burn "oh I.. I see ! W-well, why don't you get back to work now? I'm sorry for interrupting you."
    $ burns_face = "normal"
    "*Not Sorry*"
    $ allison_face = "normalt"
    allison "Of course, no problem"
    $ allison_face = "normal"
    hide allison_base with dissolve
    show burn_base at center with dissolve
    burn ". . . ."
    $ burns_hands = "phone"
    "Calls Weylon"
    $ burns_face = "angry_t"
    burn "Weylon, I want you to take out all missing person announcement in town"
    burn "Especially under the name of Allison taylor. Now"
    weylon "Of course sir, right away"
    $ burns_face = "angry"
    $ burns_hands = "3"
    burn "*ahem*"
    burn "Can't wait to peste......"
    burn "*BE CAREFUL, she is right there..... jeez*"
   # $ bathroom_map.discover(bathroom_s_candle_loc)
    $ allison_story += 1
    jump main_hall

