
label ashley_event1:
    hide screen map
    scene washroom blur
    show burn_base at left with dissolve
    $ burns_face = "normal"
    $ burns_hands = "3"
    show ashley_base at right with dissolve
    pause   
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
    $ ashley_face = "normalt"  
    $ burns_face = "angry"
    pause
    $ burns_face = "angry_t"
    burn "and waste my money? Ridiculous! If you really need one, you get one yourself"
    $ burns_face = "angry"
    $ ashley_face = "angryt"  
    ashley "……argh! Damn this stain! Oh well, since this is becoming quite the chore, I’m going to take a break. Now, might I ask you what business did you come here for?”"
    $ ashley_face = "angry"      
    $ burns_face = "normal_t"
    burn "oh, nothing much per se. I was only wishing to have a little chat. To get to… know my employees a little better, heheh"
    $ ashley_face = "normalt"  
    $ burns_face = "normal"
    ashley "hmm… are you trying to hit on me mr. burns"
    $ ashley_face = "normal"  
    $ burns_face = "hmm"
    burn "hah! That is the most outrageous idea I have heard all day, and you might be on to something. Just not as pleasant as you might think"
    $ ashley_face = "normalt"  
    $ burns_face = "normal" 
    ashley "ookaay… to be honest you’re creeping me out, so let’s get this over with. What do you want to know?"
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
    burn "huh, well… I guess you’re just not cut out for it then, Haha!”"
    $ burns_face = "laugh"
    pause
    $ burns_face = "normal"
    $ ashley_face = "normalt"  
    ashley "oh, I’m cut out to be a CEO alright, those men just don’t see things the same way I do"
    burn "I see. Well, I’ll be off now. Oh, and ms. grant, I recommend seeing a therapist. It might help with your condition, haahaa"
    $ ashley_face = "angryt"   
    $ burns_face = "laugh"    
    ashley "Screw you old man"
    pause
    hide burn_base with dissolve
    pause  
    $ ashley_face = "confuse"
    "*burns leaves and Ashley continued cleaning the floor, realizing her break time was wasted talking to Burn*"
    $ ashley_face = "normal"
    hide ashley_base with dissolve
    $ ashley_story += 1
    jump bathroom

