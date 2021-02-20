number=tuple(range(1,11))
print(number)
no1=1,[1,2,3],4
no1[1].append(5)
print(no1[1],type(no1[1]), no1)


dict_by_dict = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True)
print(dict_by_dict)
dict_by_dict = dict({'animal':'dog', "planet":'neptun', "number":40, "pi":3.14, "is_good":True})
print(dict_by_dict)
print(dict_by_dict['animal'])
dict_by_dict.update({'deneme':"22ss"})
del dict_by_dict['animal']
print(dict_by_dict)

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
print(school_records['grades_info']['teen']['joseph'])
print(list(school_records['grades_info']['teen']['joseph'].items()))