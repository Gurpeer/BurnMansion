init python:
    class item:
        def __init__(self,
                name, price, icon,
                info = "", type = None, usage = None
            ):
            self.name = name
            self.price = price
            self.info = info
            self.icon = icon
            self.type = type
            self.usage = usage

# Define all items here
default signed_ball = item(
    "signed Ball",
    200,
    "items/icons/football_icon.png",
    "Signed John, must be worth millions!",
)

default knight_sword = item(
    "A Knight Sword",
    80,
    "items/icons/knight_sword_icon.png",
    "A fine craftman by a amatuer Blacksmith",
)