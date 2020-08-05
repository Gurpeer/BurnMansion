
label ashley_event1:
    # hide screen map
    # scene washroom blur
    # $ bathroom_map.rem(bathroom_ashley_loc)
    show burn_base onlayer screens at left with dissolve
    $ burns_face = "normal"
    $ burns_hands = "3"
    show ashley_base onlayer screens at right with dissolve
    ""   
    $ burns_face = "normal_t"
    burn "Hello there, ms. Ashley grant. How do you do today ?"
    $ ashley_face = "angryt"
    ashley "Leave me alone mr. burns. Don't you see I'm quite busy ? Damn this stain! Why do I have to clean the floor with a shampoo ?!"
    $ ashley_face = "angry"  
    $ burns_face = "normal_t"
    burn "Because that's the only thing I have in this house"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "don’t you have even a single stain removal ?"
    $ ashley_face = "confuse"  
    $ burns_face = "normal_t"
    burn "No"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "well mr. burns, I say you should get one"  
    $ burns_face = "angry"
    ""
    $ ashley_face = "normal" 
    $ burns_face = "angry_t"
    burn "and waste my money? Ridiculous! If you really need one, you get one yourself"
    $ burns_face = "angry"
    $ ashley_face = "angryt"  
    ashley ". . . argh ! Damn this stain! Oh well, since this is becoming quite the chore, I’m going to take a break. Now, might I ask you what business did you come here for?!"
    $ ashley_face = "angry"      
    $ burns_face = "normal_t"
    burn "oh, nothing much per se. I was only wishing to have a little chat. To get to . . . know my employees a little better, heheh"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "hmm . . are you trying to hit on me mr. burns"
    $ ashley_face = "normal"  
    $ burns_face = "hmm"
    burn "hah! That is the most outrageous idea I have heard all day, and you might be on to something. Just not as pleasant as you might think"
    $ ashley_face = "normalt"  
    $ burns_face = "normal" 
    ashley "ookaay. . . to be honest you’re creeping me out, so let’s get this over with. What do you want to know?"
    $ ashley_face = "normal"  
    $ burns_face = "hmm"
    burn "for one thing, what were you doing before working here. I heard you were a babysitter?"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "not anymore. No one seems to trust me much these days. Really, nobody trust anyone as much anymore. So I went and work in the kitchen of a fast food restaurant at the edges of town. Awful meals, awful service, awful price, awful awful awful! They don’t even care about my rights as a woman"
    $ ashley_face = "normal"  
    $ burns_face = "normal_t"  
    burn "your rights as a woman? Like what ?"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "Well, I demanded that they made me CEO and I got fired"
    $ ashley_face = "normal"  
    $ burns_face = "normal"
    burn "...."
    $ ashley_face = "angryt"  
    ashley "don’t you think that’s ridiculous? Women have the potential and abilities just as much as men does! That means I’m as good of a CEO candidate as those men. But no, I’m stuck here working as a maid! The most stereotypical work a woman can have"
    $ ashley_face = "angry"  
    $ burns_face = "normal_t"  
    burn "huh, well... I guess you’re just not cut out for it then, Haha!"
    $ burns_face = "laugh"
    ""
    $ burns_face = "normal"
    $ ashley_face = "normalt"  
    ashley "oh, I’m cut out to be a CEO alright, those men just don’t see things the same way I do"
    $ ashley_face = "normal"   
    $ burns_face = "normal_t" 
    burn "I see. Well, I’ll be off now. Oh, and ms. grant, I recommend seeing a therapist. It might help with your condition, haahaa"
    $ ashley_face = "angryt"   
    $ burns_face = "laugh"    
    ashley "Screw you old man"
    ashley "*It seems I gotten adjusted to this lifestyle after a while, since nothing bad has really happened. Seems like Burn isn't really the dominate guy at all, just need to find opportunity to catch him make any moves on me*"
    ""
    hide burn_base onlayer screens with dissolve
    ""
    $ ashley_face = "confuse"
    "*burns leaves and Ashley continued cleaning the floor, realizing her break time was wasted talking to Burn*"
    $ ashley_face = "normal"
    hide ashley_base onlayer screens with dissolve
    $ bathroom_map.discover(bathroom_ashley_loc)
    $ ashley_story += 1
    jump bathroom


label ashley_event2:
    hide screen map
    scene main hall blur
    $ burns_face = "normal"
    $ burns_hands = "3"
    $ burns_accessory = "sinister"
    show burn_base at left with dissolve
    show ashley_base at right with dissolve
    pause
    $ burns_face = "normal_t"
    burn "We meet again, ms. Ashley Grant"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "Yes. Much to my dismay"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "oh, don't be like that. I came to make an offer you can't refuse"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "I shouldn't take an offer from a decrepit old man with evil looking eyes and 'sinister' written on his forehead"
    $ ashley_face = "normal"
    $ burns_face = "hmm"
    burn "Hah, a wonderful play on metaphorical words ms. Grant"
    burn "I must commend you"
    $ ashley_face = "confuset"
    $ burns_face = "normal"
    ashley "No, I mean seriously, someone wrote a sinister on your forehead"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "What?!"
    "burns found a reflective surface and saw that Ashley was right"
    $ ashley_face = "normal"
    $ burns_face = "angry_t"
    burn "WEYLOON! That bastard, when did he put this thing"
    $ burns_face = "angry"
    "*He rubs off the sinsister from his head very quickly*"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    $ burns_accessory = "none"
    ashley "Also, you smell like taco"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "Don't be rude, that's just my yesterday's breakfest"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "eugh"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "Well? Are you interested or not ?"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley ". . . . I'm all ears"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "Right. You see, last time you talked about how you wanted a good and proper job with good pay. Well, I can offer you just that!”"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "Sounds real fishy, but what kind of work are you talking about?"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "I offer you the job of being the manager of this mansion"
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "Seriously? That’s huge. Wait, do mansions really need managers"
    $ ashley_face = "normal"
    $ burns_face = "normal_t"
    burn "Of course they do, and you can be one with just one condition."
    $ ashley_face = "normalt"
    $ burns_face = "normal"
    ashley "What is it?"
    $ ashley_face = "normal"
    $ burns_face = "hmm"
    burn "Well, all you have to do is participate in a little activity. One that gives you pleasure of immeasurable proportions."
    burn "A little bump under blanket"
    $ ashley_face = "confuse"
    burn "A tangle of the flesh, if you get what I mean"
    $ burns_face = "normal"
    $ ashley_face = "angryt"   
    ashley "Oh. . . you're so going to jail for this"
    "*Ashley goes to call the police, but Burn blocked all the exit with iron barrier*"
    scene main hall blur with vpunch
    show burn_base at left with dissolve
    show ashley_base at right with dissolve
    $ ashley_face = "angry"  
    $ burns_face = "normal_t"
    burn "Not so fast Ms. Grant. I've locked all the exit to this house, and you won't be able to call anyone outside either. You see, I've never paid home phone bills so now it's unusable, hahah!"
    $ ashley_face = "angryt"
    $ burns_face = "normal"   
    ashley "What the hell do you think you're doing ?!"
    $ ashley_face = "angry"
    $ burns_face = "normal_t"
    burn "Also, I knew you were going to refuse, so I put this in place"
    burn "WEYLON!"
    show gas bg with dissolve
    $ burns_face = "normal"
    "*Suddenly the room is filled with gas*"
    $ ashley_face = "angryt"
    ashley "what?! Are you seriously trying to poison me? This is murder!”"
    $ ashley_face = "confuse"
    $ burns_face = "normal_t"
    burn "don’t worry, this is just a sleeping gas. I’ll see you again, in my special chamber, hahahaha !"
    $ ashley_face = "confuset"
    $ burns_face = "normal"
    ashley "Urgh, curse. . . you. ."
    "*Ashley fainted and Weylon comes in*"
    $ ashley_face = "sleep"
    $ weylon_accessory = "gasmask"
    show weylon_base:
        xalign .27
        yalign .9
        xzoom -1

    weylon "Splended work sir, everything goes as you planned"
    $ burns_face = "normal_t"
    burn "Of course, this is MY brilliant plan after all. Wait, weylon where's my gas mask?"
    $ burns_face = "normal"
    weylon "We don't have any sir, I brought mine from the store"
    $ burns_face = "hmm"
    burn ".......oh, fiddlesticks"
    $ burns_hands = "4"
    $ burns_face = "sleep"    
    "burns fainted"
    pause
    jump chamber_ashley_bedscene

label chamber_ashley_bedscene:
    scene black with dissolve
    burn "Argh... my head hurts a bit"
    burn "Wait, do I hear something?"
    pause
    $ ashley_scene_face = "angry"
    $ ashley_scene_clothe = "panty"
    $ ashley_special_clothe = "rope"
    scene bed_scene_chamber with dissolve
    show ashley_scene_base with dissolve
    pause
    burn "What the, she looks all roped up"
    burn "*God bless Weylon, he executed my plan just perfectly, even the rope idea*"
    $ ashley_scene_face = "angry_t"
    ashley "What ARE YOU DOING?!?"
    ashley "I swear, once I get out. I will report you !"
    $ ashley_scene_face = "angry"
    burn "hahahaaaaa, and how will you get out when you are tied up? Miss. Ashley Grant"
    ashley " . . ."
    $ ashley_scene_face = "please"
    ashley ".."
    $ ashley_scene_face = "please_t"
    ashley "Oh no...."
    $ ashley_scene_face = "please"
    burn "That's right, you shall be punished with your rudeness"
    burn "It's about time, I teach you a solid lesson , Miss. Ashley"
    $ ashley_scene_face = "please_t"
    ashley "... what are you going to do to me?..."
    $ ashley_scene_face = "please"
    burn "You will see"

label chamber_ashley_scene: 
 #   $ ashley_scene_clothe = "panty"
    $ ashley_scene_tit = "base"
    scene bed_scene_chamber
    show progress_ui
    if progress_bar == 1:
        show progress_bar
    elif progress_bar == 2:
        show progress_bar2
    elif progress_bar == 3:
        show progress_bar3
    elif progress_bar == 4:
        show progress_bar4
    elif progress_bar == 5:
        show progress_bar5

    if progress_bar == 4:
        $ ashley_scene_face = "ahego"

    if progress_bar == 5:
        $ ashley_scene_face = "ahego2"
        $ ashley_scene_orgasm = "wetclose"

    show ashley_scene_base
    if progress_bar == 5:
        burn "She seems pretty much done, I exhasted her. Don't think I can continue any further at this point"
        jump ashley_scene_leave
    menu:
       # $ gui.navigation_xpos = 200
        "Whip her left leg":
            if left_leg_pain == 3:
                show left_leg_whip
                pause
                $ ashley_scene_face = "ouch"
                hide left_leg_whip
                ashley "Ouch. .  *I see my bruise now... but.. it kinda feels good?*"
                $ ashley_leftpain = "leftleg"
                $ ashley_scene_face = "ahego"
                $ left_leg_pain += 1
                jump chamber_ashley_scene

            if left_leg_pain == 4:
                burn "I shouldn't go any futher, she probably will get more piss if I keep doing this"
                jump chamber_ashley_scene

            else:
                show left_leg_whip
                pause
                $ progress_bar += 1
                hide left_leg_whip
                $ ashley_scene_face = "ouch"
                ashley "ow...."
                $ ashley_scene_face = "please"           
                $ left_leg_pain += 1
                jump chamber_ashley_scene


        "Whip her right leg":
            if right_leg_pain == 3:
                show right_leg_whip
                pause
                $ ashley_scene_face = "ouch"
                ashley "Ouch. .  . . this is feeling good ?.. NO I must not admit it*"
                $ ashley_rightpain = "rightleg"
                $ ashley_scene_face = "ahego"
                $ right_leg_pain += 1
                jump chamber_ashley_scene

            if right_leg_pain == 4:
                burn "I shouldn't go any futher, she probably will get more piss if I keep doing this"
                jump chamber_ashley_scene

            else:
                show right_leg_whip
                pause
                $ ashley_scene_face = "ouch"
                ashley "ow...."
                $ progress_bar += 1
                $ ashley_scene_face = "please"           
                $ right_leg_pain += 1
                jump chamber_ashley_scene


        "Take off rope":
            if ashley_special_clothe == "none":
                burn "It is already off"
                jump chamber_ashley_scene

            if ashley_dominance > 2:
                burn "About time, I take that rope off so I could. . hehe"
                $ ashley_special_clothe = "none"
                burn "Nice, there we go . Got it off"
                ashley " . . ."
                jump chamber_ashley_scene
            else:
                burn "Nope, don't have such power to take it off"
                jump chamber_ashley_scene


        "Caress her boobs":
            if ashley_special_clothe == "rope":
                burn "I can't caress her with that rope on, need to take it off"
                jump chamber_ashley_scene
            else:
                show tit_hand_ashley
                $ ashley_scene_tit = "none"
                pause
                burn "Nice, that felt sort of soft"
                ashley ". . . ."
                $ progress_bar += 1
                jump chamber_ashley_scene

        "????????" if ashley_dominance < 5:
            "Not unlocked"
            jump chamber_ashley_scene

        "????????" if ashley_dominance < 5:
            "Not unlocked"
            jump chamber_ashley_scene


        "????????" if ashley_dominance < 5:
            "Not unlocked"
            jump chamber_ashley_scene

        "????????" if ashley_dominance < 5:
            "Not unlocked"
            jump chamber_ashley_scene

        "Take off her panty" if ashley_dominance > 5:
            if ashley_dominance > 5:
                burn "Let's get that panty off, got enough dominace on her to do it"
                $ ashley_scene_clothe = "none"
                burn "There we go"
                $ ashley_scene_face = "please"
                ashley ". . . ."
                jump chamber_ashley_scene
            else:
                burn "Don't have such dominane yet"
                jump chamber_ashley_scene


        "Vibrator" if ashley_dominance > 6:
            if ashley_dominance > 6 and ashley_scene_clothe == "none":
                show pic ashley vibrator
                burn "I guess, this is where it should simulate her"
                $ ashley_scene_face = "please_t"
                ashley "Sir, please. Not there !"
                burn "Alrite, let's start it up"
                $ ashley_scene_face = "please"
                "triggers it"
                $ ashley_scene_face = "please_t"
                ashley "Nooo"
                $ ashley_scene_face = "ahego2"
                hide pic ashley vibrator
                show ashley_vibrator
                pause
                burn "I guess we should keep it going and more faster"
                ashley ". . no...n.."
                hide ashley_vibrator
                show ashley_vibrator_fast
                $ ashley_scene_face = "ahego3"
                pause

                if ashley_scene_pose == "1":
                    $ ashley_scene_orgasm = "wetclose" 
                if ashley_scene_pose == "2":
                     $ ashley_scene_orgasm = "wetopen"
                hide ashley_vibrator
                hide ashley_vibrator_fast
                burn "Ah nice !"
                burn "Her face looks kinda well satisfied... even her area got pretty wet hahah !"
                jump chamber_ashley_scene

            if ashley_dominance > 6 and ashley_scene_clothe == "panty":
                "She has her panties on, can't do it"
                jump chamber_ashley_scene
            else:
                "Don't have such dominance to do it"
                jump chamber_ashley_scene

        "Command to open her legs" if ashley_dominance > 8:
            if ashley_dominance > 8:
                burn "open your legs Ashley"
                ashley "Yes, [ashley_call_burn]" 
                $ ashley_scene_pose = "2"
                jump chamber_ashley_scene
            else:
                burn "Don't have such dominance yet to command her"
                jump chamber_ashley_scene

        "Penetrate" if ashley_dominance > 10:
            if ashley_dominance > 10 and ashley_scene_pose == "2" and ashley_scene_clothe == "none":
                show pic ashley penis
                burn "This is about the right position"
                $ ashley_scene_face = "normal"
                ashley "*He is really about to put it in, couldn't wait any longer with the torture*"
                burn "OK"
                hide pic ashley penis
                show ashley_penetrate
                $ ashley_scene_face = "ahego2"
                burn "Ahha, this feels real goodd"
                pause
                burn "Let's thrust it even faster"
                ashley " . . ."
                ashley "*I cant, I'm about to . .*"
                $ ashley_scene_orgasm = "wetopen"
                $ ashley_scene_face = "ahego3"
                hide ashley_penetrate
                show ashley_penetrate_fast
                burn "I think I'm going too "
                burn "ARGh haaa"
                ashley "*orgasm*"
                hide ashley_penetrate_fast
                $ ashley_scene_orgasm = "cum"
                $ ashley_scene_face = "ahego4"
                scene black with dissolve
                pause
                scene bed_scene_chamber
                show ashley_scene_base
                "Seems like the cum is flowing out of her pussy"
                burn "ha.... *haaa...* wow, that felt real good"
                ashley ". . . ."
                hide ashley_penetrate_fast
                jump chamber_ashley_scene

            if ashley_scene_pose == "1":
                "Can't stick it in when she is in this pose, need to open her legs more"
                jump chamber_ashley_scene

            if ashley_dominance > 10 and ashley_scene_pose == "2" and ashley_scene_clothe == "panty":
                "She has her panty on, can't do it"
                jump chamber_ashley_scene

            else:
                "Don't have such dominace yet to penetrate her her"
                jump chamber_ashley_scene

        "Leave":
            if ashley_dominance == 0:
                if left_leg_pain == 2 or right_leg_pain == 2 and ashley_dominance == 0:
                    burn "There we go, punished enough"
                    jump ashley_scene_leave
                else:
                    "Still need to punish her"
                    jump chamber_ashley_scene
            else:
                jump ashley_scene_leave


label ashley_scene_leave:
    if left_leg_pain > 1 and right_leg_pain > 1 and ashley_dominance == 0:
        $ ashley_dominance += 2
        "You have increased Ashley's dominance by [ashley_dominance]"
    # if ashley_scene_face == "ahego3" and ashley_dominance == "2"

    $ ashley_leftpain = "none"
    $ left_leg_pain = 0
    $ right_leg_pain = 0
    $ ashley_leftright = "none"
    $ ashley_scene_orgasm = "none"
    $ ashley_scene_face = "normal"

    if ashley_dominance == 1:
        $ burns_face = "normal"
        $ burns_hands = "3"
        $ ashley_face = "confuse"
        $ ashley_clothe = "none"
        $ ashley_underwear = "panty"
        hide ashley_scene_base with dissolve
        scene bed_scene_chamber with dissolve
        show burn_base at left with dissolve
        show ashley_base at right with dissolve
        burn "Have you learned your lesson ?"
        $ ashley_face = "confuset"
        ashley ". . .yes sir."
        $ burns_face = "normal_t"
        $ ashley_face = "confuse"
        burn "Good. Now go back and continue your work, and pretend nothing has happened here"
        burn "Is that clear Miss. Ashley Grant ?"
        $ ashley_face = "confuset"
        ashley "Yes, [ashley_call_burn]"
        $ ashley_story += 1
        jump chamber 
    else:
        jump chamber




label give_ashley_business_suit:
    show burn_base onlayer screens at left with dissolve
    $ ashley_clothe = "maid"
    $ burns_face = "normal"
    $ burns_hands = "3"
    $ bathroom_map.rem(bathroom_ashley_loc)
    show ashley_base onlayer screens at right with dissolve
    $ burns_face = "normal_t"
    burn "Hello again, Miss. Ashley. Good to see you"
    $ burns_face = "normal"
    $ ashley_face = "confuse"
    ashley ". . . ."
    ashley " . ."
    burn "What with the Silent?"
    $ ashley_face = "confuset"
    ashley "I just. . . . . anyways why are you here again ?"
    $ burns_face = "normal"
    $ ashley_face = "confuset"
    ashley "What do you want from me this time . . you faked the whole offer and even.. gave me that.....puni.. ugh..."
    $ ashley_face = "confuse"
    $ burns_face = "hmm"
    burn "Are you going to keep being more rude ? Miss. Ashley"
    $ burns_face = "normal"
    $ ashley_face = "confuset"
    ashley "No please, sir. I'm just being very light here"
    ashley ". . . wha.. what do you need sir ?"
    $ burns_face = "normal_t"
    burn "About the fake offer, it wasn't fake. I was being very sincere on the offer, but you decided to turn on me and you got what has happened to you"
    $ burns_face = "normal"
    $ ashley_face = "normalt"
    ashley "Wait, you mean the offer was real ?"
    $ burns_face = "smirkleft"
    $ ashley_face = "confuse"
    burn "*tf.. ba hehehe*.."
    pause
    $ burns_face = "smirkright"
    burn "only if you knew.*"
    pause
    $ burns_face = "normal_t"
    burn "Yes, It was. However, like I said. You must fall under the condition if you want this job"
    $ burns_face = "normal"
    $ ashley_face = "normalt"
    ashley "ugh............*It's not too bad.... I don't think he will go any futher with me since all he did was...whip me with those thing.... anyways I'M sure It's worth the risk, this offer is literally my dream and I should take the opportunity*"
    $ burns_face = "normal_t"
    $ ashley_face = "normal"
    burn "Well ?"
    $ burns_face = "normal"
    $ ashley_face = "normalt"
    ashley "I'l... I'll take it Mr. Burn"
    $ burns_face = "normal_t"
    $ ashley_face = "normal"
    burn "That is what I wanted to hear *hehe..*"
    burn "Before I leave, you must wear this outfit ."
    $ burns_face = "normal"
    $ ashley_face = "confuset"
    ashley ". . .ok"
    pause
    $ player.drop(ashley_business_suit, 1)
    $ burns_face = "normal"
    $ ashley_face = "normalt"
    ashley "Ohh, this outfit looks really cool. I'll wear it and will head to the office asap"
    $ burns_face = "normal_t"
    $ ashley_face = "normal"
    burn "Now, that's a good attitude I wanted to see"
    burn "Now, I shall take my leave and I better see you at the office"
    $ burns_face = "normal"
    $ ashley_face = "confuset"
    ashley ". . . . .right way , sir"
    $ ashley_story += 1
    hide burn_base onlayer screens at left with dissolve
    hide ashley_base onlayer screens at right with dissolve
    jump bathroom







label ask_allison_ashley_waist:
    $ main_hall_map.rem(hallway_allison_loc)
    show allison_base onlayer screens at right with dissolve
    show burn_base onlayer screens at left with dissolve

    $ burns_face = "normal_t"
    burn "Hello allison, I need to ask you something"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "Uhm, depends on what it is"
    $ burns_face = "normal_t"
    $ allison_face = "normal"
    burn "It's related to Ashley"
    $ burns_face = "normal"
    $ allison_face = "normalt"
    allison "What about Ashley ?"
    $ burns_face = "normal_t"
    $ allison_face = "normal"
    burn "Well.... I want to know what her waist size is"
    burn "Do you happen to know what her waist size is?"
    $ burns_face = "normal"
    $ allison_face = "suprise"
    pause
    $ allison_face = "normalt"
    allison "Oh, I'm not entirely sure, sir. She is possibly 33 inch or 32, looking at her waist. It sure is small.. compared to mine... "
    $ burns_face = "normal_t"
    $ allison_face = "normal"
    burn ".... Thanks. I hope you are right about this"
    burn "Better go ask the other maid... to be precise.."
    $ burns_face = "normal"
    $ allison_face = "normal"
    $ main_hall_map.discover(hallway_allison_loc) 
    $ ashley_waist += 1
    hide allison_base onlayer screens at right with dissolve
    hide burn_base onlayer screens at right with dissolve
    jump main_hall


label ask_mindy_ashley_waist:
    $ front_hall_map.rem(fhall_mindy_loc)
    $ front_hall_map.rem(fhall_smoke_loc)
    show mindy_base onlayer screens at right with dissolve
    show burn_base onlayer screens at left with dissolve

    $ burns_face = "normal_t"
    burn "Hello there, Miss. Mindy"
    $ burns_face = "normal"
    $ mindy_face = "normalt"
    mindy "Hello, sir"
    $ mindy_face = "normal"
    $ burns_face = "normal_t"
    burn "Just quick question..."
    $ mindy_face = "normalt"
    $ burns_face = "normal"
    mindy "Oh. .oh okay"
    $ mindy_face = "normal"
    $ burns_face = "hmm"
    burn "What's Ashley's waist size ?"
    $ mindy_face = "normalt"
    $ burns_face = "normal"
    mindy "Oh my..... uhm.."
    $ mindy_face = "normal"
    $ burns_face = "normal"
    mindy ". . ."
    burn ". . . "
    $ mindy_face = "normalt"
    mindy "32 inch"
    $ mindy_face = "normal"
    $ burns_face = "normal_t"
    burn "Bye."
    $ burns_face = "normal"
    burn "*I'll go with that as an answer*"
    "Burns quickly leaves without a bye"
    $ ashley_waist += 1
    hide mindy_base onlayer screens at right with dissolve
    hide burn_base onlayer screens at left with dissolve   
    $ front_hall_map.discover(fhall_mindy_loc)
    $ front_hall_map.discover(fhall_smoke_loc)
    jump front_hall