print (" * BODY MASS INDEX * ")

weight = float ( input (" Please enter weight in Kg : "))
height = float ( input (" Please enter height in  : "))

BMI = weight / ( height ** 2)

if BMI <= 18.5 :
    print (" * Underweight * ")

elif 18.5 < BMI <= 24.9 :
    print (" * Normal weight * ")

elif 25 <= BMI <= 29.9 :
    print (" * Overweight * ")

elif 30 <= BMI <= 34.9 :
    print (" * Obesity * ")

elif 35 <= BMI <= 39.9 :
    print (" * Extreme Obesity * ")