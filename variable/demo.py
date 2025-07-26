a=10
b=20

sum=a+b
print(sum)

sub=a-b
print(a-b)

mul=a*b
print(mul)

div=a/b
print(div)

fd=a//b   #floor divison
print(fd)

exp=a**a
print(exp)

student_name="prashanth"
print(type(student_name))
print(id(student_name))

student_name_1="prashu"

print(type(student_name_1))
print(id(student_name_1))

student_1_age=20        #both age is 20 so at same location it is pointing and refer
print(id(student_1_age))

student_2_age=20
print(id(student_2_age))

list_1=[1,2,3,4,]
list_2=[1,2,3,4]
print(id(list_1))
print(id(list_2))


x="python"
y=" is"
z=' awesome'

print(x + y + z)   #string concatination

x=10
y=20
print(x+y)  #addition operator
z="awesome"
#print(x+y+z)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(x,z)

x,y,z=19,12,11# here x=19,y=12,z=12

x=y=z="prashanth"

print(x)
print(y)
print(z)


