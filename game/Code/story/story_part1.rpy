transform girl_pos:
    xalign 0.8
    ypos 0.3
transform girl_pos1:
    xalign 0.55
    ypos 0.3


style scene_text is text:
    color 'fe4911'
    font 'fonts/gadugib.ttf'
    outlines [(4, "#000000", 0, 0)] # this value is not final, just trying to see some results

label story_1:
    scene yesman_1
    pause
    scene yesman_2 with dissolve
    burn "isn’t that who I’m supposed to be?"
    scene yesman_3 with dissolve
    yes_men "yes sir, absolutely, no mistake about it."
    scene yesman_2 with dissolve
    burn "then tell me this. Why on earth has my business, and all my assets, been handed to people I have never even heard of?! That’s not all! I am now in debt! In debt! Of all things! So tell me, how could this happen? Did a make a wrong move?"
    scene yesman_4 with dissolve  
    yes_men "no sir, definitely not. You made all the right moves sir. Yes sir."  
    scene yesman_5 with dissolve
    burn ". . ."
    scene yesman_2 with dissolve
    burn "you bunch of imbeciles. Fine! No matter"
    burn "I had been in this hellhole before. If I have to begin from the start, I will do so"
    burn "That’s right, this will be as easy as taking candies from drunk old man sitting in the front porch of his retirement house"
    burn "After all, I still have my mansion. Yes, I know just what to do"
    scene burn_office blur with dissolve
    show burn_base at left
    show mindy normal at right with dissolve
    show allison normal at midright with dissolve
    show ashley normal at center with dissolve

    burn "From today on, you will work in this mansion until the day your contract expires."
    burn "As per the contract, you will work 24/7 during workdays, weekends, and holidays"
    burn "You will also work within questionable safety precautions with no insurance and receive salary below the minimum wages. Any questions?”"
    mindy "What about Christmas ?"
    burn "You will help with getting the Christmas tree and then decorating it"
    show ashley angry at center with dissolve
    pause
    ashley "this is bullshit! How can we possibly just accept all of this!?"

    burn "oh, then I guess you would rather go back to the fast food restaurant where you came from?"   
    show ashley normal at center with dissolve
    pause
    ashley "……on second thought, it’s basically the same thing"
    burn "Well then"
    burn "Since you are now the employees of this house, you shall call me ‘the honorable mr burns"
    pause 2.0

    burn "Wait wait, no, lord Montgomery burns"
    burn "Yes! That’s it! Brilliant! Alright, enough talking"
    # show burn rage with dissolve
    burn "Now get to it, chop-chop!”"
    allison "oh, I forgot to ask"
    burn "yes ?"
    allison "When will our contract end ?"
    burn "they don't."
    hide burn with dissolve
    hide mindy with dissolve
    hide ashley with dissolve
    hide allison with dissolve
    pause
    scene black
    centered "{=scene_text}Burns leaves the Maid out of his office. Leaving the maid all speechless{/=scene_text}" with dissolve
    centered "{=scene_text} . . . . {p} Weylon shows up to his office{/=scene_text}" with dissolve
    scene burn_office blur with dissolve
    show burn normal at left with dissolve
    show weylon normal at right with dissolve
    burn "Now then Weylon"
    burn "Tell me again about my brilliant plan to recliam what's rightfully mine"
    weylon "Certainly sir"
    # show weylon talk_calm with dissolve
    weylon "With your mansion as the new base of operation, you will open the rooms available to be used by would be residents and have them pay unreasonably expensive rent"
    weylon "You will then proceed to claim their wealth through coercion, blackmail, assassination, or any other means necessary."
    weylon "Afterwards, after you gain their money, properties, and probably their souls, you will reclaim everything one by one until you once again become the de facto king of America because who needs the president when you have capitalism. God bless America"
    burn "Perfect !"
    burn "Now all we have to do is find people to live here"
    weylon "Why don't we try putting up an ad sir ?"
    burn "and waste more of my money ?"
    # show burn rage with dissolve
    burn "Preposterous !"
    scene black
    centered "{=scene_text}Burns proceed to throw something at weylon's face{/=scene_text}" with dissolve
    scene burn_office blur with vpunch
    show burn normal at left with dissolve
    show weylon angry at right with dissolve
    # show weylon talk_angry at right with dissolve
    weylon "Ouch !"
    burn "spread it with of mouth, {p}or just kidnap someone I'm sure there are lots of homeless people around"
    weylon "But sir, homeless people don't have money"
    show weylon normal at right
    burn "ah, but they're alive aren't they? "
    burn "Then put them in the power generator or take them to the soul extractor to be used as fuel"
    weylon "right away sir."
    burn "good"
    burn "Now then, it's only a matter of time before I finally return to the billionaire club"
    burn "But for now"
    burn "Maybe I'll pester some of the maid"
    burn "Just for fun"
    weylon "oh, sir, in case you’re feeling stuck or if you’re unsure of what to do next, you know, in those rare instances where you kinda forgot what you should be doing, you can talk to me"
    weylon "and I might be able to provide some hints"
    burn "Are you suggesting that I have inadequate capacity to remember my plans ?"
    weylon "No sir"
    burn "Are you implying that I'm going senile"
    weylon "Definitly not sir"
    burn "Good"
    # show burn rage with dissolve
    # show weylon suprise with dissolve
    burn "Because I'm not !"
    # show weylon angry with dissolve
    # show burn idle with dissolve
    weylon ". . . . ."
    burn ". . . . ."
    weylon ". . . ."
    burn ". . . ."
    weylon ". . . . ."
    burn "Weylon, do you happen to remember what I plan to do this afternoon?"
    weylon "You were about to pester the maids for fun sir."
    burn "Right !"
    burn "Well, I'll be off now"
    weylon "take care sir"
    hide weylon with dissolve
    hide burn with dissolve
    pause
    centered "{=scene_text}Off to pester now.{/=scene_text}" with dissolve

    jump office

