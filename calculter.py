print("Welcome to my calculator")

n1=float(input("enter your number 1 : "))
opr=input("enter your operation (* , / , - , + , % ,m) : ")
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
        if n2==0:
            raise("Divided by Zero!")
        else:
            result=n1/n2
    case "%":
        result=n1%n2
    case "m":
        result=(n1+n2)/2
    case _:
        raise("operation is wrong!")    

print(f"the result = {result}")