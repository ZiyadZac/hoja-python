class shape:
    def area(self):
        return 0
class circle(shape):
    def area(self):
        return 3.14*5*5
class square(shape):
    def area(self):
        return 10*10

shapes={circle(),square()}
for s in shapes:
    print(s.area())

print()
print(circle().area())
print(square().area())