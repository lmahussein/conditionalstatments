num1 = int(input("Enter the base:"))
num2 = int(input("Enter the height:"))


def  traingle_area(base,height):
     area = 0.5*base*height
     if area>=10:
         print("area is large")
     elif area < 10 and area > 0:
             print("area is small")
     return area
area = traingle_area(num1,num2)
print(area)

radius = int(input("Enter the radius:"))
def circle_area(radius ):
     area = 3.14*(radius**2)
     if area >= 10:
         print("area is large")
     elif area < 10 and area > 0:
         print("area is small")
     return area
area = circle_area(radius)
print(area)

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))

def rectangle_area(length,width ):
    area = length*width
    if area >= 10:
        print("area is large")
    elif area < 10 and area > 0:
        print("area is small")
    return area
area = rectangle_area(length,width)
print(area)






