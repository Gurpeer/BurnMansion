init -96 python:
    try:
        mmm.add(
            gui0_menu(
                _("Settings"),
                ShowMenu("preferences"),
                False, False, True
                ),
            )
    except:
        pass

init offset = -1

## Preferences screen ##########################################################

screen preferences():
    tag menu
    style_prefix "pre"
    add "0GUI/settings/frame_bg.jpg"
    use game_menu(_("Settings")):
        if renpy.variant("pc"):
            hbox:
                align 0.55,0.7 spacing 140
                if _preferences.fullscreen:
                    button:
                        xysize 200,200 foreground None
                        hover_background "0GUI/settings/windowed_h.png"
                        background "0GUI/settings/windowed_I.png"
                        at btn 
                        action Preference("display", "window") 
                else:
                    button:
                        xysize 200,200 foreground None
                        hover_background "0GUI/settings/windowed_h.png"
                        background "0GUI/settings/windowed_I.png"
                        at btn 
                        action Preference("display", "any window")
                button:
                    xysize 200,200 foreground None
                    hover_background "0GUI/settings/fullscreen_h.png"
                    background "0GUI/settings/fullscreen_I.png"
                    at btn 
                    action Preference("display", "fullscreen")

            # frame:
            #     has hbox
            #     label _("Rollback Side") at btn
            #     textbutton _("Disable") action Preference("rollback side", "disable") at btn
            #     textbutton _("Left") action Preference("rollback side", "left") at btn
            #     textbutton _("Right") action Preference("rollback side", "right") at btn

            # frame:
            #     has hbox
            #     label _("Skip") at btn
            #     textbutton _("Unseen Text") action Preference("skip", "toggle") at btn
            #     textbutton _("After Choices") action Preference("after choices", "toggle") at btn
            #     textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) at btn
    vbox:
        align 0.19,0.32
        if config.has_music:
            bar value Preference("music volume") at btn

        if config.has_sound:
            bar value Preference("sound volume") at btn
            if config.sample_sound:
                textbutton _("Test") action Play("sound", config.sample_sound)

    vbox:
        align 0.74,0.39
        bar value Preference("text speed") at btn
        # bar value Preference("auto-forward time") at btn

        # if config.has_voice:
        #     frame:
        #         has fixed
        #         bar value Preference("voice volume") at btn
        #         label _("Voice Volume") at btn
        #         if config.sample_voice:
        #             textbutton _("Test") action Play("voice", config.sample_voice)
                        

            # if config.has_music or config.has_sound or config.has_voice:
            #     frame:
            #         has hbox
            #         textbutton _("Mute All"):
            #             at btn
            #             action Preference("all mute", "toggle")




style pre_slider:
    xysize(300,100)
    left_bar "0GUI/settings/bar_left.png"
    right_bar "0GUI/settings/bar_right.png"
    thumb "0GUI/settings/bar_ball.png"
    thumb_offset 20
style pre_fixed:
    fit_first True
style pre_label:
    background None
    foreground None