init offset = -1

## Confirm screen ##############################################################
style quit_text is text:
    size 70
    color "#ffff"
  #  spacing 10

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "yn"
    add "0GUI/yn/bg.jpg"
    frame:
        align .9,.8
        xsize 1000 background None
        vbox:
            label _(message) text_style "quit_text" background None at btn
            hbox:
                spacing 100
                button:
                    # text _("Yes")
                    background None
                    add "0GUI/yn/yes.png"
                    action yes_action at btn
                button:
                    # text _("No")
                    background None
                    add "0GUI/yn/no.png"
                    action no_action at btn

    key "game_menu" action no_action


## Skip indicator screen #######################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        margin(40,40) align(0,0)
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_triangle:
    font "DejaVuSans.ttf"


## Notify screen ###############################################################

screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        margin(40,40) align(0,0)
        text "[message!tq]"
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0