colorset = {'purple', 'orange', 'red', 'darkblue', 'yellow', 'red'}
color = 'purple', 'orange', 'red', 'darkblue', 'yellow', 'red'
print(color)
print(colorset)




s = set('unselfishness')

print(s) 

flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
flowerset = set(flower_list)
flowerlist = list(flowerset)

print(flowerset) 
print(flowerlist)

a = set("abracadabra")
b = set('alacazam')
print(a)
print(b)
print(a - b)  # same as '.difference()' method
print(a.difference(b)) # a difference from b
print(b.difference(a)) # b difference from a