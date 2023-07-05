print (" Triangle : YES or NO")

print (" Please enter the length of the sides of the triangle :")
a = float ( input ( " first : ") )
b = float ( input (" second : ") )
c = float ( input (" third : ") )

if a >= b + c :
    print (" NO ")

elif b >= a + c :
    print (" NO ")
    
elif c >= a + b :
    print (" NO ")

else :
    print (" YES ")