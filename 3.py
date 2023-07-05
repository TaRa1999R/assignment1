print (" * Educational Status * ")

name = input (" Please enter student's name :")
family = input (" Please enter student's family :")
a = float ( input (" Please enter first grade : "))
b = float ( input (" Please enter second grade : "))
c = float ( input (" Please enter third grade : "))

average = ( a + b + c ) / 3

if average >= 17 :
    status = " Great "

elif 12 > average :
    status = " Fail "

else :
    status = " Normal "

print ( name, family, "'s status is ", status)
print ("with the average of : ", average)