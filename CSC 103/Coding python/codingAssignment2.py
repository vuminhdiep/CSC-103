import math
pi = math.pi
print('1. Volumne')
print('2. Area')
print('3. Circumference')
cal = int(input('Calculation of what: '))
if cal == 1:
    print('1. Sphere')
    print('2. Rectangular prism')
    shape = int(input('Selection of shape: '))
    if shape == 1:
        radius = int(input('Radius: '))
        vol = (4/3) * pi * (radius**3)
        print('Volume = (4/3) * PI * Radius^3 = 1.33 * 3.14 *',radius,'^3 =',vol)
    elif shape == 2:
        length = int(input('Length: '))
        width = int(input('Width: '))
        height = int(input('Height: '))
        vol = length * width * height
        print('Volume = Length * Width * Height =', length,'*',width,'*',height,'=',vol)
    else:
        print('Wrong shape type')
elif cal == 2:
    print('1. Rectangle')
    print('2. Circle')
    print('3. Sphere')
    print('4. Rectangular prism')
    shape = int(input('Selection of shape: '))
    if shape == 1:
        length = int(input('Length: '))
        width = int(input('Width: '))
        area = length * width
        print('Area = Length * Width =',length,'*',width,'=',area)
    elif shape == 2:
        radius = int(input('Radius: '))
        area = pi * (radius**2)
        print('Area = PI * Radius^2 = 3.14 *',radius,'^2 =',area)
    elif shape == 3:
        radius = int(input('Radius: '))
        area = 4 * pi * (radius**2)
        print('Area = 4 * PI * Radius^2 = 4 * 3.14 *',radius,'^2 =',area)
    elif shape == 4:
        length = int(input('Length: '))
        width = int(input('Width: '))
        height = int(input('Height: '))
        area = 2*(length*width + length*height + height*width)
        print('Area = 2*(Length*Width + Length*Height + Width*Height) = 2*(',length,'*',width,'+',length,'*',height,'+',height,'*',width,'=', area)
    else:
        print('Wrong shape type')
elif cal == 3:
    print('1. Circle')
    shape = int(input('Selection of shape:'))
    radius = int(input('Radius: '))
    if shape == 1:
        circumference = 2*pi*radius
        print('Circumference = 2*PI*Radius = 2*3.14*',radius,'=',circumference)
    else:
        print('Wrong shape type') 
else:
    print('Wrong calculation type')
        
        

    
