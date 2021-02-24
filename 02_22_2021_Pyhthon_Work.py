if True:
    print('it is true')

empty_seat = 14

if empty_seat > 3:  # in this case, 14>3=True, so the body will execute
    print('there is still seat to sit')

x = 6
y = 9
print ("is x equal to y?                 :" , x == y)
print ("is x not equal to y?             :" , x != y)
print ("is x less than y?                :" , x < y)
print ("is x greater than y?             :" , x > y)
print ("is x less than or equal to y?    :" , x <= y)
print ("is x greater than or equal to y? :" , x >= y)


course = 'clarusway'

if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")

number = 5
if number <= 3:    
    print("Number is smaller than or equal to 3") 
else:  # Optional clause (you can only have one else)
    print("Number is bigger than 3")

weight = 80

if weight > 100:
    print("That's too heavy!")
elif weight > 75:
    print("I can lift that!")
else:
    print("That's too light!")


audience = "baby"

if audience == "kid":
    print("it is free to go to cinema")
elif audience == "teen":
    print("discounted price!")
elif audience == "adult":
    print("normal price")
else:
    print("No such audience, stay at your home!")

number=8
if number >= 10:
    print("The number is equal or greater than 10")
else:
    print("The number is less than 10")

audience_group = 'kid', 'teen', 'adult'

audience = "teen"

if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")

    score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
else:
    Score_letter="below B"

print ("Your degree: %s" % Score_letter)


