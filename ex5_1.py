name        = "Mateusz Kanabrocki"
age         = 25        
height_cm   = 185     
height_inch = round(height_cm * 0.3937, 1)
weight_kg   = 78        
weight_lbs  = round(weight_kg * 2.204)
eyes        = 'blue'
teeth       = 'white'
hair        = 'blond'

print(f"Let's talk about {name}.")
print(f"He's {height_inch} inches tall.")
print(f"He's {weight_lbs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the coffe.")

print(f"Yes, I am {str(age)} years old.")

# this line it tricky, try to get it exactly right
total = age + height_inch + weight_lbs
print(f"If I add {age}, {height_inch} and {weight_lbs} I get {total}.")
