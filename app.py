# Basic syntax & variables
# STRING 
# name ="alice"
age = 25 #integer
height = 5.6 #float
is_student = True #boolean

# print -get output
# print ("Name", name)
# print(f"Height": {height} ,"Age": {age})

# Datatypes
# 1 list /arrays 
fruit =["apple", "mango","pears"]
print([0])
fruit.append("orange")

# 2 tuple
coordinate =(10,20)
# 3 objects 
person={
    "name": "ALICE",
    "AGE" : 25
}
print(person["name"])
# for value in person.value():
#     print(value)

# 4 set - unique values
unique_numbers= {1,7,9,9}

# control flow
# 1. if...else
if age<8:
    print("adult")
else:
    print("under age")

grade = 70
if grade <60:
    print("avarage")
elif grade >60:
    print("above avarage ")
elif grade>=70:
    print("good")
else:
    print("Fail")

    # loops
    # for ..loop --if  number of  times  is known
for fruits in fruit :
    print(fruit)
# range
# for i in range(5):
#     print(i)
# using break/ continou
for i in range(5):
    if i == 3:
     continue #skips
    print(i)

    # nested
for x in range(3):
    for y in range(2):
     print(x,y)

    #  while loop
count = 0
while count > 3:
   print("COUNT",count)
   count +=1

#    functions 
# def - define the function
# return sending back results
# parameters --- inputs
# avoid repition 
# def  function_name( paramenter)
#    function_name() call back 
# parameters 
def greet(name):
   print("hello",name)
greet("bob")

# return value 
def add (a,b):
   return a+b
result = add(4,6)
print(result)

# keywords argurment
def introduce(name, age ):
   print(f"My name is{name}, am {age}years old")
introduce(name= "mike",age =25)

# local/ global 
x = 10 #global
def my_function():
   x = 5 #local
   print("inside",x)
my_function()
print("outside",x)

# ERROR HANDLING  TRY,EXCEPT, ELSE,FINALLY
# try:
# #    code:
# except Someerror:ERROR OCCURS 
# #    RUUN IF 
 # catch all errors  
try:
   num = int("abc")
except ValueError:
# value error--- wrong value 

# type error =--- wron data type 
   print("cannot convert to integer")

# zeroDivisionError =--- divide by 0
try: # try  this code
   x = int(input("enter number"))
   results = 10/x
except ValueError: # if it fails do something
   print("Error occured")
except ZeroDivisionError:
   print("you cannot divide by 0")
else:  #runs if no error occurs
   print("no error , value is:", x)
finally: #runs no matter what 
   print("this works")


def check_age(age):
   if age<18:
      raise ValueError("you must be 18+")
   return "access grnted"
print(check_age(20))


