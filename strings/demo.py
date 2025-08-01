data_1="hello"
data_2='hello'
data_3=""" hello"""

print(data_1)
print(data_2)
print(data_3)



#python_des="Python is a high-level, interpreted,
#general-purpose programming language. It was created
#by Guido van Rossum and first released in 1991. Python is known for its emphasis on code readability, employing a clear and concise syntax that often resembles natural language."

#if string is in more than 1 line definitely we need to use """"""

python="""Python is a high-level, interpreted, general-purpose programming language. It was created by Guido van Rossum and first released in 1991. Python is known for its emphasis on code readability,
employing a clear and concise syntax that often resembles 
natural language."""

#using single quote inside single quote is error
#we can use single quote in double quote


q="how are you?"
a="i'm fine"

print(a)

#we can use double quotes in single quotes
a='im "good"'
print(a)

text="python"
#to get single single char
#forward direction positive means
print(text[0])
print(text[1])
#backward direction negative means
print(text[-2])


#invalid range
#print(text[10])  #index error:string index out of range

text="python"
print(text[1])
print(text[2])
print(text[3])

text="python is very easy to learn"

print(text[0:3])  #pyt
print(text[1:4]) #yth
print(text[1:]) #ython is very easy to learn

print(text[:])

#if step is not defined default step is 1

text="python"

print(text[-4:-1]) #  tho

print(text[-4:-1:-1])  #not going to print anything



#string immutability
text="python"
#text[0]="P"
#print(text)    #'str' object does not support item assignment

text="python"
text="Python"
print(text)

new_text="j"+text[1:]
print(new_text)

str="hi"
print(str*5)  #it is going to print hi 5 times
#to know string methods we will use
print(dir(str))

mobile_no=input("enter the number:")
valid_no=mobile_no.isdigit()
print(valid_no)

pan_num=input("enter the pan details")
valid_pan=pan_num.isalnum()
format_valid_pan=pan_num.upper()
print(format_valid_pan)


