default office_desk_loc = place("Desk", (422, 691), Jump('office_desk'), "maps/office/desk.png")
default office_weylon_loc = place("Weylon", (855, 613), Jump('office_weylon'), "maps/office/weylon.png")
default office_firecamp_loc = place("Fire Camp", (1392, 742), Jump('office_firecamp'), "maps/office/fireplace.png")
default office_picture_loc = place("Picture", (1352, 0), Jump('office_picture'), "maps/office/picture.png")
default office_arrow_loc = place("Back", (962, 952), Jump('main_hall'), "maps/office/arrow.png")

default office = maps(
    "Office",
    [
        office_desk_loc,
        office_weylon_loc,
        office_firecamp_loc,
        office_picture_loc,
        office_arrow_loc,
    ]
    )

label office:
    scene burn office bg
    show screen map(office)
    pause

label office_desk:
    burn "This desk isn't for sale."
    jump office

label office_weylon:
    burn "How much would you pay for a Weylon?"
    jump office

label office_firecamp:
    burn "You can burn a body in it."
    jump office

label office_picture:
    burn "Ah, yessss, my great grand dad! he's for sale."
    jump office




