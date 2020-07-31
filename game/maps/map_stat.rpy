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
        align 1.0,0.0 offset -0,-1 fit_first True
        add "stats/ui_base.png"
        button:
            background None foreground None offset -135, 4
            add "stats/ui_quest.png"
        hbox:
            offset 40,110 spacing -10
            button:
                background None
                add "stats/ui_settings.png"
                action ShowMenu("preferences")
            button:
                background None
                add "stats/ui_skip.png"
                action Skip() alternate Skip(fast=True, confirm=True)
            button:
                text "Inv"
                action ToggleScreen("inventory")
        hbox:
            offset 200, -14 spacing 0 xalign 0.0
            add "stats/money.png"
            text "{color=#fff}" + str(p.cash) + "{/color}" offset 10, -0
        text "{color=#fff}{size=33}" + m.name + "{/colffa391or}{/size}" xalign 0.0 offset 260, 30

