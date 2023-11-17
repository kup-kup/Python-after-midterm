'''
def printme(str):
    print(str)
    return
printme("This is first call")
printme("Again second")
'''
'''
def changeme( mylist ):
    print ("Values inside the function: ", mylist)
   
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
    return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
'''
'''
def changeme( mylist ):
     mylist = [1,2,3,4] 
     print ("Values inside the function: ", mylist)
     return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

'''
'''
def changeme( myvar ):
   myvar = 100
   print ("Values inside the function: ", myvar)
   return

myvar = 99
changeme( myvar )
print ("Values outside the function: ", myvar)
'''
'''
#Function definition is here
def printme( str ):
   print (str)
   return

   #Now you can call printme function
printme("sssss")
'''
'''
# Function definition is here
def printme( str ):
    print (str)
    return

 # Now you can call printme function
printme( str = "My string")
'''
"""
# Function definition is here
def printinfo( name, age ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return
 # Now you can call printinfo function
printinfo( age = 50, name = "miki" )
Function definition is here
"""
'''
def printinfo( name, age = 35 ):
    "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return

 # Now you can call printinfo function
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )
'''
'''
def show_info(name, salary = 84360, lang = "Python"):

     print("Name: %s" % name)
     print("Salary: %d" % salary)
     print("language: %s" % lang)
     print()

show_info("Mateo")
show_info("Mateo", 105000)
show_info("Danny", 120000, "Java")
'''
'''
def create_button(id, color = "#ffffff", text = "Button", size = 16):
    print("Button: %d" % id)
    print("Attributes:")
    print("Color: %s" % color)
    print("Text: %s" % text)
    print("Size: %s" % size)
    print()

create_button(10)
create_button(11, color = "#4286f4", text = "Sign up")
create_button(id = 12, color = "#323f54", size = 24)
create_button(color = "#1cb22b", text = "Log in", size = 32, id = 13)
'''
'''
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   
   for var in vartuple:
      print (var)
   return

Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

# Now you can call sum function
total = sum( 10, 20 )
print ("Outside the function : ", total )
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
'''
'''
f = lambda x: x + 1
print(f(2))
print(f(8))


g = lambda a, b: (a + b) / 2
print(g(3, 5))
print(g(10, 33))
numbers = [2, 15, 5, 7, 10, 28, 30]
print(list(filter(lambda x: x % 5 == 0, numbers)))
print(list(map(lambda x: x * 2, numbers)))

numbers = [2, 15, 5, 7, 10, 28, 30]
is_even = lambda n : n % 2 == 0
print(list(map(is_even, numbers)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled = map(lambda n: n * 2, numbers)
print(list(doubled))
total = 0   # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )
def count_vowel(str):
    vowel = 0
    for c in str:
        if c in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'):
            vowel += 1
    return vowel
    
print(count_vowel("Hello world, today is a good day"))
def area(width, height):
    c = width * height
    return c

print(area(80, 16.3))
print(area(2, 6.3))
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()
# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Close opened file
fo.close()


'''