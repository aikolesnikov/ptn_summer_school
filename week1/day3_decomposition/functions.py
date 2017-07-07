'''
def f1(x, y):
    return x < y

print(f1(ord("q"), 5))
print(min(2, 3, 5, 6))


def f2(x, y=2):
    return x * y

print(f2(2, 3))
print(f2(2))


def f3(a=1, b=2, c=3):
    return a + b + c


f3()
f3(5)
f3(5, 7)
f3(5)
print(f3(b=3, c=4))


def f4(*args, **kwargs):
    print(args, kwargs)

f4(1, 2, 3, a=4, b=5)


# print(sum(3,2,4)) do not work
# make our with _ at the end
def sum_(*args):
    s = 0
    for arg in args:
        s += arg
    return s
print(sum_(3,2,4))
'''

def f5(x):
    return 2*x

double = f5
print(double(2))


def execute(f,x):
    return f(x)
print(execute(double,3))

print(list(map(double, [1,2,3,4])))



def odd(x):
    return x % 2

print(list(filter(odd, [1,2,3,4])))



print(list(map(lambda x: 3*x, [1,2,3,4,5])))
print(list(map(lambda x: 2*x, range(10))))
print([3*x for x in range(10) if x%2])

l = [(3,7),(2,8),(4,2)]
l.sort()
print(l)
l.sort(key=lambda x: x[1])
print(l)

l = [1, 'a', (2,3)]
l.sort(key=str)
print(l)