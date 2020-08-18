init python:
    class inventory:
        def __init__(self, cash = 0, bags = [bag(10)]):
            self.cash = cash
            self.bags = bags
            self.uniqueID = []
            self.offs = 0
        def ret(self):
            r = []
            for i in range(4):
                if i < len(self.bags[0].items):
                    r.append(self.bags[0].items[i+self.offs])
                else:
                    r.append(None)
            return r
        def offs_up(self):
            if self.offs > 0:
                self.offs -= 1
        def offs_down(self):
            if self.offs < len(self.bags[0].items)-4:
                self.offs += 1

        def has(self, item, quantity = 1):
            if self.bags[0].exist(item, quantity):
                return True
            else:
                return False
        def gotcash(self, a, u):
            if u and u in self.uniqueID:
                pass
            else:
                self.cash += a

        def paidcash(self, a):
            self.cash -= a

        def got(self, x, q, u = None): # x = item, q = Quantity, u = Unique ID
            if u and u in self.uniqueID:
                pass
            else:
                if len(self.bags):
                    self.bags[0].add(x, q)
                    self.uniqueID.append(u)
                    msg.msg("You have got {} of {}".format(q, x.name))

        def drop(self, x, q):
            if len(self.bags):
                self.bags[0].rem(x, q)
                msg.msg("You have dropped {} of {}".format(q, x.name))

default player = inventory()
screen inventory(p = player):
    modal True
    style_prefix "inv"
    vbox:
        align 0.0,1.0
        spacing 0
        button:
            add "0GUI/inv/inv_uparrow.png"
            background None
            action Function(p.offs_up)
        for i in p.ret():
            if i:
                button:
                    background "0GUI/inv/slot.png"
                    tooltip i
                    fixed:
                        fit_first True
                        add i.item.icon
                        text str(i.quantity) align 1.0,1.0
                    action i.item.usage
            else:
                button:
                    background "0GUI/inv/slot.png"
                    xysize 175,175
        button:
            add "0GUI/inv/inv_downarrow.png"
            background None
            action Function(p.offs_down)