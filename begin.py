# 1.Program to display Welcome Message
print("Welcome to official-tech")

###############################################################################################################################################

# 2.Program to accept input and display message
print("Welcome",input("Please Enter your name: "))

**************************************************

# Another way to write 2
name = input("Enter your name: ")
print("Welcome back ",name)

###############################################################################################################################

# 3.Program to accept two numbers and perform Addition, Multiplication, Substraction, Division
a, b = int(input("First Integer: ")), int(input("Second Integer: "))
print('addition', a+b,'\nsubtract',a-b,'\nmultiplication',a*b,'\ndivide',a/b)
# You can write any variable name

****************************************************************************

# Another way to write 3
var1, var2 = int(input("First Integer: ")), int(input("Second Integer: "))
add,multi,sub,div = print("Addition",var1+var2), print("Multiplication",var1*var2), print("Subtraction",var1-var2), print("Division",var1/var2)

***************************************************************************************************

# Another way to write 3
var1 = int(input("First Integer: "))
var2 = int(input("Second Integer: "))
print()
add = print("Addition of var1&var2 is ", var1 + var2)
print() # for newline or empty line space
multi = print("Multiplication of var1&var2 is ", var1 * var2)
print()
sub = print("Subtraction of var1&var2 is ", var1 - var2)
print()
div = print("Division of var1&var2 is ", var1 / var2)

##################################################################################################

# 4.Program to find the type of a Variable
_int, _float, _str, _bool,  = 10, 20.33, 'official-tech', True
print(type(_int), type(_float), type(_str), type(_bool))

****************************************************************************************************************************************

# Another way to write 4
type(print("This is None Type"))

****************************************************************************

# Another way to write 4
_int = 944
_float = 944.808
_str = 'official-tech'
_bool =  True
print(type(_int))
print(type(_float))
print(type(_str))
print(type(_bool))

#########################################################################################################################################

# 5.Program to accept first and last name and display full name
print("Hello Mr/Miss ",input("Enter your First name "), input("Enter your Last name "))

*********************************************************************************************

# Another way to write 5
_first, _last = input("Enter your First name "), input("Enter your Last name ")
print("Hello Mr/Miss ", _first, _last)


#####################################################################################################################################

# 6.Program to input two numbers and swap those values
#__string, _string = _string, __string = input("1.Integer = "), input("2.Integer = ")
#print("After swapping ", __string, _string)


********************************************************************************************

# Another way to write 6
_string, __string = input("1.Integer = "), input("2.Integer = ")
print("Before swapping ", _string, __string)
_string, __string = __string, _string
print("After swapping ", _string, __string)

#################################################################################################################################

# 7.Program to accept a string value and convert the string value to int 
_string_ = print("Integer value is ",int(input("String value: ")))

************************************************************************************************

# Another way to write 7
_string_ = input("String value: ") #input from keyboard, here, by default whatever input() take is string value
print(type(_string_)) #
_string = int(_string_) #typecasting, string to integer
print("Integer ", _string)
print(type(_string))















