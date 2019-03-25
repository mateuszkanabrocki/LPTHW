# numer of people types
types_of_people = 10       
# f-string                                      
x = "There are {types_of_people} types of people." 
# string          
binary = "binary"                                              
do_not = "don't"
# f-string
y = f"Those who know the {binary} and those who {do_not}."      
# printing f-string
print(x)                                                        
print(y)

# printing f-string with f-string in it (can't do it by puting the f-string directly into f-string - got to use the variable)
print(f"I said: {x}")                                           
print(f"I also said '{y}'")

# variable with value = 0 (can also type "False" or "True")
hilarious = bool(1)   
# string the empty braces - place for the variable to be formatted                                          
joke_evaluation = "Isn't that joke so funny?! {}"               

# printing the string and formating it right before printing
print(joke_evaluation.format(hilarious))                        

# string variable
w = "This is the left side of..."                               
e = "a string with the right side."

# printing "w" string variable followed by "e" string variable
print(w + e)                                                   