
# Actually, the examples in the previous lesson show us how backslash 
# 👉🏻\ works. 👉🏻\ is a special sign used in expressions called escape sequences, 
# which behaves according to the character immediately after 👉🏻\. Here are basic escape sequences in Python:
# \n : means new line,
# \t : means tab mark,
# \b : means backspace. It moves the cursor one character to the left.
# Look at these examples carefully:

text1 = 'it'
text2 = 'easy'
print(text1 + '\'s very '  + text2)


print('C:\\november\number_expenditure.txt')
print("one", "two", "three", sep="\t") # separated by tab marks
print('we', '\bare', '\bunited') # remember, normally print() function separates expressions by spaces
print('it\'s funny to learn Python') 


# using sep= , and end=
print('www', 'clarusway', "com", sep='.', end=' ')
print('will', end=' ')
print('open', end=' ')
print('your', end=' ')
print('path', end='.')



# Priority boolean "not" "and" "or"
print()
logic = True and False or not False or False
print(logic)  # What's the answer

# The following values are considered False, in that they evaluate to False when applied to a boolean operator:
# None.
# Zero of any numeric type: 0, 0.0, 0j
# Empty sequences and collections: '', [], {}.
# Other than above values, any remaining value is evaluated as True.
# Here are some and or  operations :
print()
print("2 and 3= ", (2 and 3) )
print("3 and 2= ", (3 and 2) )
print("2 or 3= ",(2 or 3) )
print("3 or 2= ",(3 or 2) )

print(1 and 0)
print(1 or 0)
print(1 and "I am doing good!")
print([] and "Hello World!")

# strings
fruit = 'Orange'

print('Word                   : ' , fruit)
print('First letter           : ' , fruit[0])
print('Second letter          : ' , fruit[1])
print("3rd to 5th letters     : " , fruit[2:5])
print("Letter all after 3rd   : " , fruit[2:])

# The formula syntax of string indexing is : string[start:stop:step].
# string[:] : returns the full copy of the sequence
# string[start:] : returns elements from start to the end element
# string[:stop] : returns element from the 1st element to stop-1
# string[::step] : returns each element with a given step
city = 'Phoenix'

print(city[1:])  # starts from index 1 to the end
print(city[:6])  # starts from zero to 5th index
print(city[::2])  # starts from zero to end by 2 step
print(city[1::2])  # starts from index 1 to the end by 2 step
print(city[-3:])  # starts from index -3 to the end
print(city[::-1])  # negative step starts from the end to zero

# You can use the len() function to find out the length (number of characters) of a text or a variable of any type.
vegetable = 'Tomato'

print('length of the word', vegetable, 'is :', len(vegetable))

# Arithmetic syntax (+, =, *) :
# We can use + operator for combining the two string together without any spaces. For example :

print('clarus' + 'way')
print(3*'no way!')
fruit = 'Orange'
vegetable = 'Tomato'
print("using + :", fruit + vegetable)
print("using * :", 3 * fruit)

#
fruit = 'orange'
fruit += ' apple'
print(fruit)

# 👉🏻% operator gets the values in order and prints them in order using several characters accordingly. Look at the example :
# For now, we used only s, d and f characters to specify the data type in a string.
# 💡Tips:
# In the '%s' syntax : s stands for 'string'.
# In the '%.2f' syntax : f stands for 'float'. In this example 2 digits after point.
# In the '%d' syntax : d stands for 'numeric'.
phrase = 'I have %d %s and %.2f brothers' % (4, "children", 5)  
print (phrase)

sentence = "apologizing is a virtue"

print("%.11s" % sentence)  # we get first 11 characters of the string
print('%(amount)d pounds of %(fruit)s left' % {'amount': 33, 'fruit':'bananas'})

# As in this example below, the value of expression comes from
# .format() method in order. Curly braces 👉🏻{} receives values from .format().

fruit = 'Orange'
vegetable = 'Tomato'
amount = 4
print('The amount of {} we bought is {} pounds'.format(fruit, amount))

print('{state} is the most {adjective} state of the {country}'.format(state='California', country='USA', adjective='crowded'))

print('{0} is the most {adjective} state of the {country}'.format('California', country='USA', adjective='crowded'))

print("{6} {0} {5} {3} {4} {1} {2}".format('have', 6, 'months', 'a job', 'in', 'found', 'I will'))
print("{9} {7} {1} {10} {3} {2} {5} {8} {6} {0} {4}".format('in', 'know', 'bring', 'to', 'students.', 'out', 'best', 'teachers', 'the', 'Good', 'how'))

# 'f-string' formatting :
# It makes string formatting easier. This method was introduced in 2015 with Python 3.6.
fruit = 'Orange'
vegetable = 'Tomato'
amount = 6
output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"

print(output)

result = f"{4 * 5}"

print(result)

my_name = 'JOSEPH'
output = f"My name is {my_name.capitalize()}"

print(output)

# If you want to use multiple f-string formatting lines without parentheses,
#  you will have the other option that you can use backslash 
# 👉🏻\ between lines.

name = "Joseph"
job = "teachers"
domain = "Data Science"
message = (
     f"Hi {name}. "
     f"You are one of the {job} "
     f"in the {domain} section."
)
print(message)



