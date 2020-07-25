init python:
    class bag:
        def __init__(self, name, items = [], slots = 4):
            self.name = name
            self.items = items
            self.slots = slots
        
        def add(self, x, q): # x = item, q = Quantity
            if len(self.items):
                for i in self.items:
                    if i.item == x:
                        i.quantity += q
                        break
                else:
                    self.items.append(stack(x, q))
            else:
                self.items.append(stack(x, q))
        
        def rem(self, x, q):
            if len(self.items):
                for i in self.items:
                    if i.item == x and i.quantity >= q:
                        if i.quantity > q:
                            i.quantity -= q
                        elif i.quantity == q:
                            self.items.remove(i)
                        return True
                        break
                else:
                    return False
            else:
                return False
        
        def exist(self, x, q):
            if len(self.items):
                for i in self.items:
                    if i.item == x and i.quantity >= q:
                        return True
                        break
                else:
                    return False
            else:
                return False