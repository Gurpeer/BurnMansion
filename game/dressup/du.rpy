init python:
    class dress_up:
        def __init__(self, cloths, dir):
            self.dir = dir
            self.cloths = cloths
        def generate(self):
            pass
            # c = []
            # c.append(renpy.image_size(self.dir+self.cloths[0][1]))
            # for i in self.cloths:
            #     c.append((0, 0))
            #     c.append("{}{} {}.png".format(c.dir, i[0], i[2][i[1]]))
            return Composite()
        def next(self, s):
            if self.cloths[s][1] < len(self.cloths[s][2])-1:
                self.cloths[s][1] += 1
        def back(self, s):
            if self.cloths[s][1] > 0:
                self.cloths[s][1] -= 1
        def add(self, s, x):
            self.cloths[s][2].append(x)
        def ret(self, s):
            return self.cloths[s][2][self.cloths[s][1]]

default dressup1 = dress_up(
    [
        ["base", 0, ["1"], 600],
        ["face", 0, ["angry", "laugh", "normal"], 400],
        ["hands", 0, ["1", "2", "phone"], -400],
        ["holding", 0, ["cash", None], 300]
    ],
    "char/burn/01/",
    )

transform du_zoom(z, y):
    ease .4 zoom z yoffset y

screen dressup(c= dressup1):
    modal True

    for i in c.cloths:
        if i[2][i[1]] is not None:
            add "{}{} {}.png".format(c.dir, i[0], i[2][i[1]])
    vbox:
        spacing 0 xalign 0.1
        for ii, i in enumerate(c.cloths):
            button:
                action NullAction()
                # background None
                hbox:
                    button:
                        text "<<"
                        action Function(c.back, ii)
                    vbox:
                        xsize 120 spacing 4
                        text i[0]
                        if i[2][i[1]]:
                            text i[2][i[1]]
                        else:
                            text "None"
                    button:
                        text ">>"
                        action Function(c.next, ii)
