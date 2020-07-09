init -100 python:
    class gui0_menu:
        def __init__(self, name, act, mm, nav, rep):
            self.name = name
            self.act = act
            self.mm = mm
            self.nav = nav
            self.rep = rep
    class gui0_menuz:
        def __init__(self):
            self.list = []
        def add(self, x):
            self.list.append(x)
init -99:
    define mmm = gui0_menuz()

init -98 python:
    try:
        mmm.add(
            gui0_menu(
                _("Start"),
                Start(),
                False, True, True
                ),
            )
    except:
        pass

init -80 python:
    try:
        mmm.add(
            gui0_menu(
                _("Main Menu"),
                MainMenu(),
                True, False, True
                ),
            )
        mmm.add(
            gui0_menu(
                _("Quit"),
                Quit(confirm=not main_menu),
                False, False, True
                ),
            )
    except:
        pass

init offset = -1

## Navigation screen ###########################################################

screen navigation(m = mmm):
    style_prefix "nav"
    
    frame:
        align(.5,1.0)
        hbox:
            for i in m.list:
                if (main_menu and i.mm) or (not main_menu and i.nav) and i.rep:
                    pass
                else:
                    button:
                        at btn
                        text i.name
                        action i.act


## Main Menu screen ############################################################
image mm_fire:
    "0GUI/mm/fire1.png"
    .1
    "0GUI/mm/fire2.png"
    .1
    "0GUI/mm/fire3.png"
    .1
    "0GUI/mm/fire4.png"
    .1
    "0GUI/mm/fire5.png"
    .1
    repeat
image mm_fire1:
    "0GUI/mm/fire3.png"
    .1
    "0GUI/mm/fire1.png"
    .1
    "0GUI/mm/fire4.png"
    .1
    "0GUI/mm/fire5.png"
    .1
    "0GUI/mm/fire2.png"
    .1
    repeat
screen main_menu(m = mmm):
    style_prefix "mm"
    tag menu
    add "0GUI/mm/main_menu_bg.jpg"
    add "mm_fire" align .225,.66
    add "mm_fire1" align .78,.66
    hbox:
        align(.5,1.0)
        button:
            at btn
            add "0GUI/mm/start_btn.png"
            action Start()
        button:
            at btn
            add "0GUI/mm/load_btn.png"
            action ShowMenu("load")
        button:
            at btn
            add "0GUI/mm/setting_btn.png"
            action ShowMenu("preferences")
        button:
            at btn
            add "0GUI/mm/credit_btn.png"
            action Start()
        button:
            at btn
            add "0GUI/mm/quit_btn.png"
            action Quit(confirm=not main_menu)

style mm_button:
    background None
    foreground None
## Game Menu screen ############################################################

screen game_menu(title):
    style_prefix "gm"
    # add bgs[1]
    transclude

    use navigation
    button:
        xysize 200,200 foreground None align 0.94,0.05
        hover_background "0GUI/mm/exit_h.png"
        background "0GUI/mm/exit.png"
        at btn 
        action Return()
    # label title margin(40,40) align(1.0,0.0) at btn
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style gm_viewport:
    xfill True xalign .5