

n1=float(input("enter your number 1 : "))
opr=input("enter your opertion (* , / , - , + , % ) : ")
n2=float(input("enter your number 2 : "))
result=0
match opr:
    case "+":
        result=n1+n2
    case "-":
        result=n1-n2    
    case "*":
        result=n1*n2
    case "/":
        result=n1/n2
    case "%":
        result=n1%n2

print(result)