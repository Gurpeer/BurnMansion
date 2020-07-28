init python:
    import os.path
    class player_units:
        def __init__(self, name):
            self.name = name
            self.cash = 0
        def got_cash(self, a):
            self.cash += a
default mr_burns = player_units("Burns")
screen map_stats(m, p = mr_burns):
    modal True
    tag place
    fixed:
        align 1.0,0.0 offset -50,-1 fit_first True
        add "stats/ui_base.png"
        button:
            background None foreground None offset -120, 4
            add "stats/ui_quest.png"
        hbox:
            offset 40,70 spacing -10
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
            offset 180, -8 spacing 0 xalign 0.0
            add "stats/money.png"
            text str(p.cash) offset 10, -10
        text m.name xalign 0.0 offset 240, 30

