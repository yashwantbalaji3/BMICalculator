name = "YW"
height_m = 1.8288
weight_kg = 80.03

bmi = weight_kg / (height_m ** 2)
print ("bmi: ")
print(bmi)
if bmi <= 18.5:
    print(name + " is in the underweight range.")
elif bmi < 25:
    print(name + " is in the healthy range.")
else:
    print (name + " is overweight.")

    
