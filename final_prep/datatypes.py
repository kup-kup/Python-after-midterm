'''
Basic Datatypes
    Single Value
        1. string   
        2. int
        3. float
        4. bool
    Array (เก็บหลายค่า)
        1. list
        2. tuple
        3. dict
        4. set
'''

"""string"""
str_var = "string value yuyuyu"

# #string indexing
# print(str_var[0])       # s
# print(str_var[1:5])     # trin
# print(str_var[-1])      # u
# print(str_var[:-1])     # string value yuyuy
# print(str_var[3:-1])    # ing value yuyuy
# print(str_var[3:])      # ing value yuyuyu
# print(str_var[1::2])    # tigvleyyy
# print(str_var[:])       # ?

"""int"""
int_var = "1234"

"""float"""
float_var = "1234.01"

"""list"""
list_var = [1, "string type", "1234.1", 13.6, float_var]
# print(list_var[-1]) # ?

list_empty1 = []
list_empty2 = list()

"""tuple"""
tuple_empty1 = tuple()
tuple_empty2 = ()

tuple_var = tuple(list_var)
# print(tuple_var)

"""dict"""
dict_var = {"value_1" : 1,
            "value_2" : 2,
            3 : "value_3"}

dict_empty1 = {}
dict_empty2 = dict()

# print(dict_var.items())     # key-value pair
# print(dict_var.keys())      # keys only
# print(dict_var.values())    # values only

# print(dict_var["value_1"])    # or
# print(dict_var.get("value_1"))

# print(type(())) 
# print(type({}))
# print(type([]))
# print(type(set()))