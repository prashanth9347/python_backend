#arthematic opeartors
# +,-,*,/,%, //,**

x=10
y=20

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

print(x//y)
print(x**y)


#compound assignment operators
#instead of ++,-- we will use +=

x=10

x+=5

print(x)

#relation operators/comparison
#< > >= <= == !=

x=10
y=20
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x>y)
print(x<y)

#logical operators
#and or not

a=2
b=5
c=8
d=10

x=a>b and b<c
print(x)

x=a>b or b<c

print(x)

x=a>b
print(not x)
print("============")
#Membership operators

#in , not in

x="i am learning python full stack"
y= "a" in x
z="a" not in x
print(y)
print(z)
print("============")

#identity operators

#is ,is not

x=[1,2,3]
y=[3,4,5]

print(x is y )
print(x is not y)

print("============")


#bitwise operators

#& | ^ ~ >> <<

x=5  #0000 0101
y=3  #0000 0011

z=x&y
print(z)
p=x|y
print(p)

q=x^y
print(q)

r=~x
print(r)

x=10

print(x<<2)
y=20
print(y>>2)