transform larry_middle_position:
    xalign 0.65
    yalign 1.0

transform larry_middle_position1:
    xalign 0.3
    yalign 1.0

default larry_face = "normal"
default larry_hands = "1"
image larry_base = Composite((471,850),
    (0,0), "char/larry/base.png",
    (0,0), "char/larry/face [larry_face].png",
    (0,0), "char/larry/arm [larry_hands].png",
)


