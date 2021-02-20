# Data Types and Useful Operations

text1 = "I have learned strings" # surrounded with double quotes
print(text1)
e_mail = 'joseph@clarusway.com' # surrounded with single quotes
print(e_mail)
print('632') # this is also a string type

example1 = 'sometimes what you say is less important than how you say it'
print(type(example1))   # <class 'str'>
example2 = '71'
print(type(example2))  # <class 'str'>

example3 = 71
print(type(example3))
example4 = 71.0
print(type(example4))
example5 = 3.14j
print(type(example5))
example6 = True
print(type(example6))   # <class 'bool'>
f = 3.14  # the type is float
print(type(f)) 
f = 3.14  # the type is float
s = str(f)  # converting float to string
print(type(s)) 
f = 3.14  # the type is float

i = int(f)  # while converting a float value to an integer its decimal part is disregarded
print(i, '\n')
print(type(i))  

i = 3

f = float(i)
print(f, '\n')
print(type(f)) 

x = 39
v = "11"
y = "2.5"
z = "I am at_"

print(x-int(v))
print(x-float(y))
print(z+str(x))

a = 36.5
b = '30'
c = '3.5'
d = ' F is enough for room temperature.'

print(str(a+int(b)+float(c))+d)

#---------------------------------------
color = 'red'  # str type variable
season = 'summer'
price = 250  # int type variable
pi = 3.14  # float type variable
color = 'blue'  # You can always assign a new value to a created variable
price = 100  # value of 'price' is changed
season = 'winter'  

print(color, price, season, sep=', ')

#---------------------------------------
a = 5
b = 55
c = 555
c = a
b = c
a = b

print(a, b, c, sep=', ')

#---------------------------------------
n='''2020'''
print(type(n))

print(4 + 11) # sum of integers gives integer
print(39 + 1.0) # sum of an integer and float gives float

#---------
no1, no2 = 46, 52
no3 = no1 - no2
print(no3)

no1 = 46
print(no1/23)  # division gives float
print((3 * 4)/2)  # parentheses are used as in normal mathematics operations
print(7 // 2)  # it gives integer part of division
print(9 % 2)  # remainder of this division is 1  it means 9 is an odd number 
print(3**2)
print(2**3)
print(64**0.5)  # square root
print('Result of this (12+7) sum :', 12 + 7)

# Unary Minus
age=10
print(-age)

number = 2020
text = "children deserve respect as much as adults in"
print(text, number)  # children deserve respect as much as adults in 2020
print("yesterday I ate", 2, "apples")    # yesterday I ate 2 apples

print('i', end=' ')
print('will say', end=' ')
print("'i missed you'", end=' ')
print('to my mother') 
#  i will say 'i missed you' to my mother

print('smoking', 'is', 'slowly', 'killing me', sep=' + ') 
# smoking + is + slowly + killing me

x = 5
print ('value of x       : ', x)

x += 2
print ("2 more of x      : ", x, "\n") # using string expression '\n', 
                                       # we produce extra line. 
                                       # So that we had empty line.
y = 10
print ('value of y       : ', y)

y -= 2
print ("2 minus y        : ", y, "\n")

z = 6
print ('value of z       : ', z)

z *= 2
print ("2 times z        : ", z, "\n")

# value of x       :  5
# 2 more of x      :  7 

# value of y       :  10
# 2 minus y        :  8 
    
# value of z       :  6

# 2 times z        :  12 

fruit = 'Orange'
vegetable = "Tomato"
print (fruit, """ and """ , vegetable)   #Orange  and  Tomato


print("one", "two", "three", sep="\t") # separated by tab marks

# remember, normally print() function  separates expressions by spaces
print('we', '\bare', '\bunited')   # weareunited

print('it\'s funny to learn Python')    # it's funny to learn Python

text = "Clarusway, Clarusway, Clarusway"

print(text,",\n\t", text,",\n\t\t",text, sep="")


word = 'clarusway'
n = 3
front = word[0:3]
back =word [4:]
print(front + back)

text = "{} I am a {} programmer and I {} Clarusway.".format("Hello", "new", "love")
print(text)


city = "SARAJEVO"
text = f"{city.capitalize()}"
print(text)

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http:'))

text = 'www.clarusway.com'
print(text.endswith('om'))
print(text.startswith('w'))

email = "clarusway@clarusway.com is my e-mail address"
print(email.startswith("@", 9))
print(email.endswith("-", 10, 32))


phrase = "myemailaddress@clarusway.com"

print(len(phrase))
print(phrase.startswith("@", 14))
print(phrase.endswith(".", 15, 24))

sentence = "I live and work in Virginia"
print(sentence.upper())  
print(sentence.lower())
print(sentence.swapcase())
print(sentence)  # note that, source text is unchanged

sentence = "I live and work in Virginia"
title_sentence = sentence.title() 
print(title_sentence)  
changed_sentence = sentence.replace("i", "+")
print(changed_sentence)  
print(sentence)  # note that, again source text is unchanged

sentence = "I live and work in Virginia"
swap_case = sentence.swapcase()
print(swap_case)
print(swap_case.capitalize())  # changes 'i' to uppercase and
# the rest to lowercase

name="MARIAM"
text=f"My name is {name.capitalize()} "
print (text)

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
     f"Hi {name}. "
     f"You are one of the {job} "
     f"in the {domain} section.")
print(message)

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = f"Hi {name}. " \
     f"You are one of the {job} " \
     f"in the {domain} section."

print(message)

space_string = "     listen first      "
print(space_string.strip())  # removes all spaces from both sides

source_string = "interoperability"
print(source_string.strip("yi"))  
# removes trailing "y" or "i" or "yi" or "iy" from both sides

source_string = "interoperability"
print(source_string.lstrip("in"))  
# removes "i" or "n" or "in" or "ni" from the left side

space_string = "     listen first      "
print(space_string.rstrip())  # removes spaces from the right side

source_string = "interoperability"
print(source_string.rstrip("yt"))  
# removes "y" or "t" or "yt" or "ty" from the right side
