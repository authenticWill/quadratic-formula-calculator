import cmath
a = float(input('a value:'))
b = float(input('b value:'))
c = float(input('c value:'))

d = (b**2) - (4*a*c)

sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)
print('The soluions are {0} and {1}'.format(sol1,sol2))
