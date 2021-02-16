# TUPLE

# Differnce between TUPLE and LIST
empty_tuple = ()
print(type(empty_tuple))
empty_list=[]
print(type(empty_list))

try_tuple = ('love')
print(try_tuple)
print(type(try_tuple)) # <class 'str'>  it's not tuple type. 

# If you want to create a single element tuple, you should use a comma.

try_tuple = ('love',)
print(try_tuple)
print(type(try_tuple)) # it's a tuple type.

planets = 'mercury', 'jupiter', 'saturn'
print(planets)    # ('mercury', 'jupiter', 'saturn')
print(type(planets)) #<class 'tuple'>

empty_tuple_1 = tuple()
print(empty_tuple_1)    #()
print(type(empty_tuple_1)) # <class 'tuple'>

# It is easy to convert between list and tuple as in the examples below
my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)
my_list = list(my_tuple)
print(type(my_list), my_list)  # <class 'list'> [1, 4, 3, 4, 5, 6, 7, 4]


my_list = [1, 4, 3, 4, 5, 6, 7, 4]
my_tuple = tuple(my_list)
print(type(my_tuple), my_tuple) # <class 'tuple'> (1, 4, 3, 4, 5, 6, 7, 4)

# An iterable string can be converted to a tuple :
mountain = tuple('Alps')
print(mountain)     #('A', 'l', 'p', 's')

# You can also duplicate values or mix different data types in tuples.
mix_value_tuple = (0, 'bird', 3.14, True)
print(len(mix_value_tuple))

even_no = (0, 2, 4)
print(even_no[0])    
print(even_no[1])    
print(even_no[2])   

my_list=list(range(11))[1:]
my_list.sort(reverse=True)
print(my_list)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1::2])

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text =  "My two favorite flowers are {[0][2]} and {[0][1][1]}, two favorite colors are {[1][0]} and {[1][1][1]}.".format(flowers,flowers,colors,colors)
print(text)

text =  "My two favorite flowers are {0[0][2]} and {0[0][1][1]}, two favorite colors are {1[1][0]} and {1[1][1][1]}.".format(flowers,colors)
print(text)

text="upper"
print(* text)
