init python:
    class item:
        def __init__(self,
                name, price, icon,
                info = "", type = None, usage = NullAction()
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
    "A fine craftsman by a amateur Blacksmith",
)

default office_key = item(
    "Key",
    0,
    "items/icons/key_icon.png",
    "Use it to access the entrance of the dungeon from the Office",
)

default red_perfume = item(
    "Red Perfume",
    0,
    "items/icons/perfume_unconsious_icon.png",
    "Looks like a regular perfume . .? not sure what use this is",
)

default eye_patch = item(
    "Eye blinder",
    0,
    "items/icons/eye_patch_icon.png",
    "Used to cover your eyes",
)

default spa_book = item(
    "Spa Book",
    0,
    "items/icons/spa_book_icon.png",
    "Contains useful information about massaging",
)

default default_sword = item(
    "Default sword",
    40,
    "items/icons/default_sword.png",
    "A basic default sword",
)

default spa_camera = item(
    "A spa camera",
    0,
    "items/icons/camera_icon.png",
    "A sneaky squared spa camera",
)

default blue_gem = item(
    "Blue Gem",
    0,
    "items/icons/blue_diamond_icon.png",
    "Part of the piece used on the dungeon door",
)

default red_gem = item(
    "Red Gem",
    0,
    "items/icons/red_gem_icon.png",
    "Part of the piece used on the dungeon door",
)

default green_gem = item(
    "Green Gem",
    0,
    "items/icons/green_gem_icon.png",
    "Part of the piece used on the dungeon door",
)