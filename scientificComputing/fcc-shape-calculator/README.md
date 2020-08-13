This project cotains a rectangle class and square subclass with methods to calculate certain measurements of the shapes and set the sides. The string method returns the measurements and a picture of the shape using "*" characters based on the side lengths

#### Usage example
```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())

rect.set_height(3)
print(rect.get_perimeter())

print(rect)

print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())

sq.set_side(4)
print(sq.get_diagonal())

print(sq)

print(sq.get_picture())


rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
