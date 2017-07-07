class Table:
    # pass
    def __init__(self, w, l):
        print('Init.')
        self.w = w;
        self.l = l;

    def set_w(self, w):
        self.w = w
        print(self)


'''
t1 = Table()
print(t1)
print(type(t1))
t2 = Table()
print(t1 == t2)

t1.w = 50
print(vars(t1))
print(dir(t1))
del t1.w
print(vars(t1))
print(dir(t1))
'''

t = Table(10,20)
print(vars(t))
t.set_w('qq')
print(vars(t))
