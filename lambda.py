# WAP a function to add 2 numbers:

add = lambda a,b,c: a+b+c
print(add(50,10,40))

# WAP to double each element in a list :

element = [2,3,4,5,6]
square = list(map(lambda x: x*x, element))
print(square)

# Add each element by 10 :

numbers = [1,2,3,4,5,6]
result = list(map(lambda x:x+10,numbers))
print(result)
