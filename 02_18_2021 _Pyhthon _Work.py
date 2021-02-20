escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]
sentence = "I am 40 years old. {0[0]} I have two children. {0[2][1]} Data Science is my IT domain.".format(
    escapes)
print(sentence)

# The syntax for accessing an item is very simple. 
# We write a key that we want to access in square brackets. 
# This method works both for adding items to a dict and for reading them from there.

state_capitals = {'Arkansas': 'Little Rock', 'Colorado': 'Denver',
                 'California': 'Sacramento', 'Georgia': 'Atlanta'
                  }
print(state_capitals['Colorado'])  # accessing method

state_capitals['Virginia'] = 'Richmond' # adding a new item
print(state_capitals)
mix_values = {'animal': ('dog', 'cat'),  # tuple type
              'planet': ['Neptun', 'Saturn', 'Jupiter'],  # list type
              'number': 40,  # int type
              'pi': 3.14,  # float type
              'is_good': True}  # bool type

mix_keys = {22 : "integer",
            1.2 : "float",
            True : "boolean",
            "key" : "string"}


dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)
print(dict_by_dict)


dict_by_dict = {'animal': 'dog',
                'planet': 'neptun',
                'number': 40,
                'pi': 3.14,
                'is_good': True}

print(dict_by_dict.items(), '\n')
print(dict_by_dict.keys(), '\n')
print(dict_by_dict.values())


dict_by_dict.update({'is_bad': False})
print(dict_by_dict)


del dict_by_dict['animal']
print(dict_by_dict) 

dict_by_dict = {'planet': 'neptun',
               'number': 40,
               'pi': 3.14,
               'is_good': True,
               'is_bad': False}

print('pi' in dict_by_dict) 
print('animal' not in dict_by_dict)  # remember, we have deleted 'animal'


student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }
print(student_ages['Clark'])
school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },               
        },
        
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },               
        },        
}
print(school_records)
print(school_records['personal_info']['teen']['marry']['age'])

empty_set = set()

# Note that, to create an empty set you have to use set() function.
#  Do not use {} to create an empty set. Otherwise, you will create an empty dictionary.

print(type(empty_set))
colorset = {'purple', 'orange', 'red', 'darkblue', 'yellow', 'red'}

print(colorset)
print(colorset)
print(colorset)
print(colorset)

flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flowerset = set(flower_list)
flowerlist = list(flowerset)

print(flowerset) 
print(flowerlist)


a = set('abracadabra')
b = set('alacazam')

print(a)  

print(a - b)  # same as '.difference()' method
print(a.difference(b)) # a difference from b

print(a | b)  # same as '.union()' method
print(a.union(b)) # unification of a with b

print(a & b)  # same as '.intersection()' method
print(a.intersection(b)) # intersection of a and b


a.remove('c') # we delete 'c' from the set
print(a)
a.add('c') # we add 'c' again into the set
print(a)

print(len(set('listen to the voice of enlisted')))

numbers = {}

numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)

