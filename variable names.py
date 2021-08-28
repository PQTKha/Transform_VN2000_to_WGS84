#Python - variable names
#A Variable can have a short name (like x and y) or more descriptive name (age, carname, total_volume)
#Rules for python variable names:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha_numeric characters and underscores (A-z, 0-9 and _)
#A variable name are case-sensitive (age, Age and AGE are three different variables)

#Example: legal variables:
myvar = "John"
my_var="John"
_my_var = "John"
myVar ="John"
MYVAR ="John"
myvar2 ="John"

#Illegal variable names:
2myvar = "John" #variable name start by number
my-var ="John" #varibale has hyphen character 
my var ="John" #variable has space

#Multi words variable names
#variable names with more than one word can be difficult to read
#There are several techniques you can use to make them more readable
#Camel case: Each word, except the first, starts with a capital letter
myVariableName ="John"
#Pascal case: Each word starts with a capital letter
MyVariableName ="John"
#Snake case: Each word is separated by an underscore character:
my_variable_name = "John"
