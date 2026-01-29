string="Hi this is string"
string2='hi this is also a string '


string3=""" hi this i s
also 
a 
string
"""

print(string3)

string_mul="hi " *3
print(string_mul)
print(len(string_mul))

print ("a" in string)
print(string2.startswith("hi"))
print(string.startswith("hi"))

print("String2 is "+str(len(string2))+" character long")


print("------place holder Format method--------")
name='Sneha'
print("hello my name is {1} and this is {0} character long ".format (len(name),name))
