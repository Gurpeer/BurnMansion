init python:
    import os.path
    class place:
        def __init__(self, name, xy, act, icon = None):
            self.name = name
            self.xy = xy
            self.act = act
            self.icon = icon
            self.hover_icon = os.path.splitext(self.icon)[0]+"_h"+os.path.splitext(self.icon)[1]
    class maps:
        def __init__(self, name, p = []):
            self.name = name
            self.p = p # places
        def discover(self, x):
            self.p.append(x)
            msg.msg("Discovered {}".format(x.name))
        def rem(self, w):
            self.p.remove(w)

screen map(m):
    modal True
    tag place
    
    for i in m.p:
        button:
            pos i.xy anchor 0.0,0.0 padding 0,0
            if i.icon:
                background None foreground None hover_background i.hover_icon
                add i.icon
            else:
                text i.name
            action Hide("map"), i.act
    use map_stats(m)