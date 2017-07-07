class Furniture:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def get_area(self):
        return self.w * self.l


class Table(Furniture):
    def __init__(self, l, w):
        super().__init__(l, w)
        self.is_closed = True

    def open_drawer(self):
        self.is_closed = False
        print('Open')

    def close_drawer(self):
        self.is_closed = True
        print('Close')

    def get_type(self):
        return 'Table'


class Chair(Furniture):
    def get_type(self):
        return 'Chair'


t = Table(10, 20)
print(t.get_area())
t.open_drawer()

l = [Chair(50,50), Table(100,100), Chair(20,80)]
for furn in l:
    print(furn.get_type(), furn.get_area())