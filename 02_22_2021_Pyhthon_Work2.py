number = 0

while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6')


my_list = ["a", "b", "c", "d", "e"]

a = 0

while a < len(my_list):
    print('square of {} is : {}'.format(a, a**2))
    a += 1


flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1 > 0:
    print(flowers[count2])
    count1 -= 1
    count2 += 1


question = 'What number am I thinking of?  '
print("Let's play the guessing game!")
answer = 44
while True:
    guess = 44   # int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        break

for i in [1, 2, 3, 4, 5]:
    print(i)

seasons = ['spring', 'summer', 'autumn', 'winter']

for season in seasons:
    print(season)


text1 = set("TWELVE PLUS ONE")
text2 = set("ELEVEN PLUS TWO")

if text1 == text2:
    print("we are the same")

b = list(range(11))

print(b)


text = ['one', 'two', 'three', 'four', 'five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers):
    print(x, ':', y)

who = ['I am ', 'You are ']
mood = ['happy', 'confident']
for i in who:
    for ii in mood:
        print(i + ii)


word12 = "Yes"       # input('Write Yes or No')

if word12 == "Yes":
    word12 = True
    print(word12, "You entered True")
if word12 != "Yes":
    word12 = False
    print(word12, "You not entered True")


number = 2
if (number % 2) == 0:
    print(number, " is even")
else:
    print(number, " is even")


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in range ( len  (weekdays)):
    print('Day', day+1, ':', weekdays[day])

number = 3 # int(input('Please enter a number: '))
i=0
while i< number :
    print(i**2)
    i+=1

sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for item in sample_list :
    print("The type of", item, "is", type (item))
