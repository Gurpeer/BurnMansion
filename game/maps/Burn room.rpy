image fish_tank_move:
    "maps/burn room/fish_tank.png"
    xpos 1330 yalign .4
    xzoom 1.0
    linear 2 xpos renpy.random.randint(1300,1480) yalign .4
    xzoom -1.0
    linear 2 xpos renpy.random.randint(1295,1356) yalign .4
    xzoom 1.0
    linear 2 xpos renpy.random.randint(1340,1390) yalign .38
    xzoom -1.0
    linear 2 xpos renpy.random.randint(1300,1323) yalign .4
    # pause 2
    # xpos 1330 
    # linear 4 xpos renpy.random.randint(1200,1270) yalign .4

    repeat

image bubble_tank:
    "maps/burn room/bubble1.png" with dissolve
    .7
    "maps/burn room/bubble2.png" with dissolve
    .7
    "maps/burn room/bubble3.png" with dissolve
    .7
    "maps/burn room/bubble4.png" with dissolve
    .7
    pause .4
    repeat    


screen cash_text():
    vbox:
        xalign .5
        yalign .1
        frame:
            text "You got $ [mr_burns.cash]"


default burn_room_sword_loc = place("sword", (53, 484), Jump('burn_room_sword'), "maps/burn room/knight sword.png")
default burn_room_camera_loc = place("camera", (1419, 727), Jump('burn_room_camera'), "maps/burn room/camera.png")
default burn_room_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")
default burn_room_bed_loc = place("bed", (650, 558), Jump('burn_room_bed'), "maps/burn room/bed.png")
default burn_room_mask_loc = place("beard mask", (749, 402), Jump('burn_room_beardmask'), "maps/burn room/beard mask.png")
default burn_room_seller_loc = place("Seller", (261, 454), Jump('burn_room_seller'), "maps/burn room/seller figure.png")
#default burn_room_sword_loc = place("fire", (0, 0), None, "office_fire")


default burn_room_map = maps(
    "Burn Room",
    [
        "water_tank",
        "fish_tank_move",
        "bubble_tank",
        "water_frame",
        burn_room_sword_loc,
        burn_room_camera_loc,
        burn_room_arrow_loc,
        burn_room_bed_loc,
        burn_room_mask_loc,
    ]
    )

label burn_room:
    if seller_npc == True:
        $ burn_room_map.discover(burn_room_seller_loc)
        

    scene burn room bg
    # show water_tank
    # show fish_tank_move
    # show bubble_tank
  #  show water_frame
    show screen map(burn_room_map)
    pause
    jump burn_room

label burn_room_sword:
    burn "A knight sword, but it looks pretty heavy to carry.."
    jump burn_room

label burn_room_seller:
    hide screen map
    scene burn room blur
    show seller_base at seller_position 
    show screen cash_text
    show burn_base at left
    $ burns_face = "normal"
    $ seller_face = "normal"
    menu:
        "{color=#bf2b21} BUY ~ {/color} Scratchy Personal Instrument $ 85" if not player.bags[0].exist(cat_instrument, 0) and ask_instrument == 2:
            $ burns_face = "normal_t"
            burn "Is this the instrument that call Scratchy?"
            $ burns_face = "normal"
            $ seller_face = "happy"
            seller "Yes"
            $ burns_face = "normal_t"
            burn "Why you even have this item ? "
            $ burns_face = "normal"
            $ seller_face = "sad"
            seller "Scratchy personally left it to me to call him, but I never did and have no use for it"
            seller "So, I just decided to sell it "
            burn ". . . ."
            seller ". . . "
            $ burns_face = "hmm"
            burn "Just give me the damn instrument, I'll buy it"
            if mr_burns.cash < 86:
                $ burns_face = "smirkleft"
                burn "Shit. . ."
                seller "Sir ?"
                $ burns_face = "normal_t"
                burn "... *I don't have the cash to buy this..*"
                burn "Actually, you know what. Second thought, I'll come back and buy it later"
                $ burns_face = "normal"
                seller "Ok"
                jump burn_room_seller
            else:
                show instrument_cat_item_frame
                "Obtained Scratchy Instrument"
                pause
                hide instrument_cat_item_frame
                $ player.got(cat_instrument, 1)
                $ mr_burns.lose_cash(85)
                jump burn_room_seller       

        "{color=#59ab1a} SELL~ {/color} Doom Armour - $ [doom_armor.price]" if player.bags[0].exist(doom_armor, 1):
            burn "Selling this Doom armour"
            $ seller_face = "happy"
            seller "Why my, this is a very stunning hard armour"
            seller "Do you not know who Doom is ?"
            burn "No."
            $ seller_face = "normal"
            seller "*Hehe.. can trick him to selling it for cheap price despite not knowing the infamous villain*"
            seller "I'll take it for [doom_armor.price]"
            burn "Ok"
            $ player.drop(doom_armor, 1)
            $ mr_burns.got_cash(35)
            jump burn_room_seller

        "{color=#59ab1a} SELL~ {/color} Shield - $ [default_shield.price]" if player.bags[0].exist(default_shield, 1):
            $ burns_face = "normal_t"
            burn "Selling this Shield "
            $ burns_face = "normal"
            $ seller_face = "happy"
            seller "Ooohhh hooo, now this is some quality looking piece"
            burn "*... this shield was really cheap from where I brought it..... quality?.. seriously*"
            burn "135 bucks for this"
            $ burns_face = "normal"
            $ seller_face = "normal"
            seller "I'll take it"
            $ burns_face = "normal_t"
            $ seller_face = "happy"
            burn "Ok"
            $ burns_face = "normal"
            $ player.drop(default_shield, 1)
            $ mr_burns.got_cash(135)
            jump burn_room_seller

        "{color=#bf2b21} BUY ~ {/color} Ashley business outfit" if ashley_story == 9:
            $ burns_face = "hmm"
            burn "Ahem"
            burn "I heard you sell clothes aswell ? Mr. Seller"
            $ burns_face = "normal"
            $ seller_face = "happy"
            seller "Ahhh yes I do"
            $ burns_face = "normal"
            $ seller_face = "normal"
            seller "What are you looking for exactly ? Sir"
            $ burns_face = "normal_t"
            burn "A business outfit . ."
            $ burns_face = "normal"
            seller "For whom? sir? what's her waist size?"
            $ burns_face = "normal_t"
            burn ". . . waist size? why you need to know this?"
            $ burns_face = "normal"
            seller "For measurement purpose sir, and her needs"
            $ burns_face = "hmm"
            burn ".. I. . .well you see..*You seriously asking me to ask the rude Ashley her waist size?...*"
            burn "You know what, you just hang onto that , will you?"
            $ burns_face = "normal"
            $ seller_face = "happy"
            seller "Sure"
            burn "I should probably ask the other maid about her waist size...."
            $ ashley_story += 1
            jump burn_room_seller

        "{color=#bf2b21} BUY ~ {/color} Ashley business outfit $ 100 " if ashley_waist == 2:
            $ burns_face = "normal_t"
            burn "I'm back"
            $ seller_face = "happy"
            burn "and waist size is 32 inch"
            $ burns_face = "normal"
            $ seller_face = "normal"
            seller "Hmm"
            seller "Ok, I'll sell it for $ 100 "
            burn " . . ."
            if mr_burns.cash < 99:
                burn "*Don't have enough money to buy this business outfit, damn.*"
                $ burns_face = "hmm"
                burn "Well..... I'll come back to you later, got something else to do "
                $ burns_face = "normal"
                $ seller_face = "sad"
                seller "You always got something else to do, sir "
                $ burns_face = "normal_t"
                burn "Yes, way more important then this non sense business suit to be frank with you *... not really THIS SUIT IS IMPORTANT..... IT WILL ALLOW ME TO.... tangle..oh fiddlesticks*"
                burn "Well, I shall take my leave"
                $ burns_face = "normal"
                seller "Come back anytime, sir"
                jump burn_room_seller
            else:
                burn "*Good thing, I got money to buy this*"
                $ burns_face = "normal_t"
                $ seller_face = "normal"
                burn "I'll buy it, give it already"
                $ burns_face = "normal"
                $ seller_face = "happy"
                seller "Yes, of course but hold on sir, I have to craft this suit "
                seller "You will have to wait the next day for the delivery to arrive at your mail outside"
                seller "It will be there in nick of time, sir"
                $ burns_face = "normal_t"
                $ seller_face = "sad"
                burn "Alrite, what ever. Just take my money and I shall take my leave here Mr. Seller"
                $ burns_face = "normal"
                $ seller_face = "happy"
                seller "Anytime, sir."
                $ renpy.notify("- 100 cash")
                $ mr_burns.lose_cash(100)
                $ ashley_waist += 1
                $ ashley_story += 1
                jump burn_room_seller




        "{color=#59ab1a} SELL ~ {/color} Default Sword - $ [default_sword.price]" if player.bags[0].exist(default_sword, 1):
            seller "I'll take it for [default_sword.price]"
            burn "Ok"
            $ player.drop(default_sword, 1)
            $ mr_burns.got_cash(25)
            jump burn_room_seller      

        "{color=#59ab1a} SELL ~ {/color} Signed Football - $ [signed_ball.price]" if player.bags[0].exist(signed_ball, 1):
            seller "I'll take it for [signed_ball.price]"
            burn "Wait what !?!"
            seller "What?"
            burn "This is a SIGNATURE signed by a celebrity in Football and you want to sell me [signed_ball.price] !"
            $ seller_face = "sad"
            seller "Hmm..... I think he was a underrated not so popular football player, Mr. Burn"
            seller "The man barely was even a hall a famer, let alone his worth"
            seller "I'm being nice and buy it for that price otherwise, I can buy it for lower if you want"
            burn "HAHA..  ha nono, I think [signed_ball.price] is more then enough "
            $ seller_face = "happy"
            seller "Ok"
            $ player.drop(signed_ball, 1)
            $ mr_burns.got_cash(45)
            jump burn_room_seller
    

        "Leave":
            hide screen cash_text
            jump burn_room

    jump burn_room

label burn_room_camera:
    burn "Oh yes, forgot I had a small sqaured camera"
    burn "If I have the sneaky advantage and timing to place this camera somewhere secretly..."
    burn "I could be watching a premium nudity .. HAHAHA HA!"
    burn "*coughh* *cough*.. ahh...."
    jump burn_room


label burn_room_bed:
    hide screen map
    scene burn room blur
    menu:
        "Sleep":
            if ashley_story == 4:
                $ ashley_story += 1

                if seller_npc == True:
                    $ seller_npc = False
                    $ burn_room_map.rem(burn_room_seller_loc)

                scene black with dissolve
                pause
                "Next morning"
                weylon "*Calling Burn*"
                burn " . . . what the... who's call is this "
                burn "Yes ?"
                weylon "It's me sir, the gas is activated. It's about time you talk to Ashley "
                burn "Finally *HAHAHAHAAAAAAAAAA*"
                burn "Ok, be ready and don't fail me"
                weylon "Don't worry sir, I won't"
                burn "*Hangs the phone....*"
                burn "Ok, my energy is high today for some reason"
                scene burn room blur with dissolve
                "Ah, my back feels nice"
                jump burn_room

            if ashley_waist == 3 and ashley_story == 11 and mail_ashley_business_suit == False:
                scene black with dissolve
                pause
                "Next morning"
                "{color=#d61f0b}Alert {/color}: A delivery has arrived to the mail box."
                $ mail_ashley_business_suit = True   
                scene burn room blur with dissolve
                "Ah, my back feels nice"
                jump burn_room            

            else:
                if seller_npc == True:
                    $ seller_npc = False
                    $ burn_room_map.rem(burn_room_seller_loc)
                    
                scene black with dissolve
                pause
                "Next morning"
                scene burn room blur with dissolve
                "Ah, my back feels nice"
                jump burn_room
        "Nah":
            jump burn_room     
            


    burn "Don't really feel sleepy yet"
    jump burn_room

label burn_room_beardmask:
    burn "This is definitly sellable"
    burn "Hell, this mask was a purchase from Zues himself"
    burn "Don't know why he was selling these kind of mask"
    burn "It probably had some sort of abilites or passive traits , but... I wore this and it does nothing..."
    jump burn_room