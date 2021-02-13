text1 = "I bought"
text2 = "kg. of apple this morning"
amount = 6
text3 = text1 + " " + str(amount) + " " + text2
print(text1, amount, text2)
print("I bought", 6, "kg. of apple this morning")
print("I bought " + "6 " + "kg. of apple this morning")
print(text3)


print("we are", "\boosting our", "\brotherhood")
print('it\'s funny to learn Python') 

print(True and False or not False or False)

# None.
# Zero of any numeric type: 0, 0.0, 0j
# Empty sequences and collections: '', [], {}.
# Other than above values, any remaining value is evaluated as True.


# And operator : The and operator evaluates all expressions and 
# returns the last expression if all expressions are evaluated True. 
# Otherwise, it returns the ﬁrst value that evaluated False.

# Or operator : The or operator evaluates the expressions left to right and 
# returns the ﬁrst value that evaluated True 
# or the last value (if none is True)

print(None and 2)  #  false
print(2 and None)  #  false
print( "                 False and 2")  #  false
print( False and 2)  #  false
print(2 and False )  #  false
print( "                 2 0")  #  false
print( 0 and 2)  #  false
print(2 and 0 )  #  false

 # result is first true otherwise last falsy
print()

print({} or None)

print()
print( False or 2 or True  )   
print( False or "" or [] or None)

print(2 and 3)  #  3

#STrings
Fruit="orange"
print(type(Fruit))
print("Word         :", Fruit)
print("First        :", Fruit[0])
print("Second       :", Fruit[1])
print("3rd to 5th   :", Fruit[2:5])
print("3rd to end       :", Fruit[2:])
print("Second       :", Fruit[-1])