# Lists

country = ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand']
print(country)

#-------------------------
string_1 = 'I quit smoking'

new_list_1 = list(string_1)  # we created multi element list
print(new_list_1)

new_list_2 = [string_1]  # this is a single element list
print(new_list_2)

#---------------------
mixed_list = [11, 'Joseph', False, 3.14, None, [1, 2, 3]]

#--------------
warning = 'You must quit smoking!'

print(len(list(warning)))

empty_list_1= []
empty_list_2 = list()
empty_list_1.append('114')
empty_list_1.append('plastic-free sea')
print(empty_list_1) 

# .append() : Append an object to end of a list. Using only list.append(element) syntax, returns none. 
#If you want to see the new appended list, you have to call or print it.
city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
city.append('Addis Ababa')
print(city) 

# .insert() : Add a new object to list at a speciﬁc index.
# The syntax looks like list.insert(index, object). 
city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.insert(2, 'Stockholm')
print(city)

# We can remove the elements in lists using list.remove() method
city = ['New York', 'London', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.remove('London')
print(city)  # we have deleted 'London'

# or sort the elements using list.sort() method. Examine the example :
city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.sort()  # lists the items in alphabetical order
print(city)   

# Likewise, the length of the list elements can be calculated with the len() function also
city = ['Addis Ababa', 'Istanbul', 'New York', 'Seoul', 'Stockholm', 'Sydney']
print(len(city))

# Guess and figure out the output of this syntax :
my_list = [1, 3, 5, 7]
print(my_list * 3)

city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city[1] = 'Melbourne'  # we assign 'Melbourne' to index 1
print(city)   
# ['New York', 'Melbourne', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']

print()
city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
print (city)
del city[0]
print (city)

city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
del city[0:2]
print (city)   # ['Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']

city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city[0:2]=[]
print (city)   # ['Istanbul', 'Seoul', 'Sydney', 'Addis Ababa'] 

city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
s=city.pop(3)
print(s)
print (city)   # ['New York', 'Stockholm', 'Istanbul', 'Sydney', 'Addis Ababa']


city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.remove('Stockholm')
print (city)   # ['New York', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']

city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.reverse()
print (city) 


# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)


colors = ['red', 'purple', 'blue', 'yellow', 'green']
print(colors[2])  # If we start at zero, 
# the second element will be 'blue'.

city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']

city_list = []
city_list.append(city) # we have created a nested list

print(city_list) # city_list includes only one element which is the city list.
print(city_list[0]) # access to first and only element
# ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']

print(city_list[0][2])  # Istanbul
print(city_list[0][2][3])  #qs 

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(numbers[2:5])  # we get the elements from index=2 to index=5(5 is not included)

count = list(range(11))
print(count)


print(count[0:11:2])
animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[:])  # all elements of the list


animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[3:])

animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[:5])

animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[::2])

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(even_numbers[4:9])

print(len([[12, 34, 56]]))
print(len([[12, 34, 56]][0]))
a=[[12, 34, 56]][0]
print(a)


#negative
city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
print(city[-4])

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
print(reef[-3:])

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
print(reef[:-3])

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
print(reef[::-1])  # we have produced the reverse of the list

reef = ['swordfish', 'shark', 'whale', 'jellyfish', 'lobster', 'squid', 'octopus']
print(reef[::-2])

odd_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(odd_no[7:3])
print(odd_no[7:3:-1])
print(odd_no[2:6:-1])
print(odd_no[:])



