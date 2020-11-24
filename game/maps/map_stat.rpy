init python:
    import os.path
    class player_units:
        def __init__(self, name):
            self.name = name
            self.cash = 0
        def got_cash(self, a):
            self.cash += a
        def lose_cash(self, a):
            self.cash -= a

default mr_burns = player_units("Burns")
screen map_stats(m, p = mr_burns):
    modal True
    tag place
    fixed:
        align 0.97,0.02 offset -0,-1 fit_first True
        add "stats/ui_base1.png"
        button:
            background None foreground None offset -170, 1
            add "stats/journal_UI.png"
        # hbox:
        #     offset 40,110 spacing -10
        #     button:
        #         background None
        #         add "stats/ui_settings.png"
        #         action ShowMenu("preferences")
        #     button:
        #         background None
        #         add "stats/ui_skip.png"
        #         action Skip() alternate Skip(fast=True, confirm=True)

        hbox:
            offset 0, 20 spacing 0 xalign 0.0
           # add "stats/money.png"
            text "{color=#fff}{size=25}{font=fonts/gadugib.ttf}" + str(p.cash) + "{/color}{/size}{/font}" offset 60, 0
        text "{color=#fff}{size=25}{font=fonts/gadugib.ttf}" + m.name + "{/colffa391or}{/size}{/font}" xalign 0.0 offset 60, -25

    default inve = False
    if inve:
        button:
            align 0.0,0.0
            background None
            add "0GUI/inv/open.png"
            action SetLocalVariable("inve", False)
        use inventory
    else:
        button:
            align 0.0,0.0
            background None
            add "0GUI/inv/close.png"
            action SetLocalVariable("inve", True)
