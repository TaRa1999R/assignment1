import math

print (" * CALCULATOR * ")

print(" + : sum ")
print(" - : subtraction ")
print(" * : multiplication ")
print(" / : division ")
print(" sin : sinus ")
print(" cos : cosine ")
print(" tan : tatngen ")
print(" cot : cotangent ")
print(" log : logaritm ")
print(" ^ : power ")
print(" sqrt : square ")
print(" ! : factorial ")

op = input( " Please choose your operation : ")

if op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
    a = float( input(" Please enter first number : ") )
    b = float( input(" Please enter second number : ") )

else :
    a = float( input(" Please enter the number : "))
    if op == "sin" or op == "cos" or op == "tan" or op == "cot" :
        a = a * (math.pi / 180)
    
    elif op == "!" :
        a = int (a)
    

if op == "+" :
    result = a + b

elif op == "-" :
    result = a - b

elif op == "*" :
    result = a * b

elif op == "/" :
    if b == 0 :
        print (" *Cannot divide by zero* ")
    else :
        result = a / b

elif op == "^" :
    result = a ** b

elif op == "sqrt" :
    result = math.sqrt (a)

elif op == "sin" :
    result = math.sin (a)

elif op == "cos" :
    result = math.cos (a)

elif op == "tan" :
    result = math.tan (a)

elif op == "cot" :
    result = 1 / math.tan (a)

elif op == "log" :
    result = math.log10 (a)

elif op == "!" :
    if a == 0 :
        result = 1
    elif a < 0 :
        print (" NOT DEFINED ")
    else :
        result = math.factorial (a)

else :
    print (" Your operation has't been defined")

print (" The result is : ", result )
print (" Your Welcom :)")