init python:
    import os.path
    class player_units:
        def __init__(self, name):
            self.name = name
            self.cash = 0
        def got_cash(self, a):
            self.cash += a
default mr_burns = player_units("Burns")
screen map_stats(m):
    modal True
    tag place
    fixed:
        align 1.0,0.0 offset -40,40 fit_first True
        add "stats/ui_base.png"
        button:
            background None foreground None xoffset -135
            add "stats/ui_quest.png"
        hbox:
            offset 10,55 spacing 0
            button:
                background None foreground None 
                add "stats/ui_settings.png"
                action ShowMenu("preferences")
            button:
                background None foreground None 
                add "stats/ui_skip.png"
                action Skip() alternate Skip(fast=True, confirm=True)
        hbox:
            offset 150, -34 spacing 0 xalign 0.0
            add "stats/money.png"
            text str(mr_burns.cash)
        text m.name xalign 0.0 offset 175, 4

