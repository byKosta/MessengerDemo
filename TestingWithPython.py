#https://www.tutorialspoint.com/python3/python_variable_types.htm
#Python supports three different numerical types −

#int (signed integers)
#float (floating point real values)
#complex (complex numbers)

integer = 10
floatLike = 100.0
string = "string"

print("--- Integer, Float, String ---")
print(integer)
print(floatLike)
print(string)
print("------------------------------")

print("--- Multiple Assignment(A, B, and C should be 1) ---")
a = b = c = 1
print(a)
print(b)
print(c)
print("------------------------------")

print("--- Multiple Assignment with different values---")
a, b, c = 1, 2.1, 'test'
print(a)
print(b)
print(c)
print("------------------------------")

print("--- Python Numbers ---")
var1 = 1
var2 = 2
print(var1)
print(var2)
del var2
#print(var2) - this will cause a "not defined" issue.
print("------------------------------")

print("--- Python Strings ---")
str = "hello world"

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
print("------------------------------")

print("--- Python Lists ---")
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists
print("------------------------------")

print("---  Python Tuples (READ ONLY LISTS) ---")
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple
print("------------------------------")

print("---  Python Dictionary(kind of hash-table type) ---")
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (dict.keys())
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print("------------------------------")