class Table:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def get_area(self):
        return self.w * self.l


t = Table(10, 20)
print(t.get_area())
