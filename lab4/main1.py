# 1

# def printme(str):
#     print(str)
#     return

# printme("This is first call")
# printme("Again second")

# 2.1

# def changeme( mylist ):
#    print ("Values inside the function: ", mylist)
   
#    mylist[2]=50
#    print ("Values inside the function after change: ", mylist)
#    return

# mylist = [10,20,30]
# changeme( mylist )
# print ("Values outside the function: ", mylist)

# 2.2

# def changeme( mylist ):
#    mylist = [1,2,3,4] 
#    print ("Values inside the function: ", mylist)
#    return

# mylist = [10,20,30]
# changeme( mylist )
# print ("Values outside the function: ", mylist)

# 2.3

# def changeme( myvar ):
#    myvar = 100
#    print ("Values inside the function: ", myvar)
#    return

# myvar = 99
# changeme( myvar )
# print ("Values outside the function: ", myvar)

# 3.1

# # Function definition is here
# def printme( str ):
#    print (str)
#    return

# # Now you can call printme function
# printme("sssss")

# 3.2

# # Function definition is here
# def printme( str ):
#    print (str)
#    return

# # Now you can call printme function
# printme( str = "My string")

# 3.3

# # Function definition is here
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age = 50, name = "miki" )

# 3.4

# Function definition is here
# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age = 50, name = "miki" )
# printinfo( name = "miki" )

# 3.5

# def show_info(name, salary = 84360, lang = "Python"):
#     print("Name: %s" % name)
#     print("Salary: %d" % salary)
#     print("language: %s" % lang)
#     print()

# show_info("Mateo")
# show_info("Mateo", 105000)
# show_info("Danny", 120000, "Java")

# 3.6

# def create_button(id, color = "#ffffff", text = "Button", size = 16):
#     print("Button: %d" % id)
#     print("Attributes:")
#     print("Color: %s" % color)
#     print("Text: %s" % text)
#     print("Size: %s" % size)
#     print()

# create_button(10)
# create_button(11, color = "#4286f4", text = "Sign up")
# create_button(id = 12, color = "#323f54", size = 24)
# create_button(color = "#1cb22b", text = "Log in", size = 32, id = 13)

# 3.7

# # Function definition is here
# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
   
#    for var in vartuple:
#       print (var)
#    return

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50 )

# 4
