# Faulty Calculator (Restricted Calculations "10 + 5 = -4"
#                                            "8 - 2 = 108"
#                                            "6 * 4 = 87"
#                                            "70 / 5 = 22"
#                                            "5 ^ 2 = 50"
print("1. for +")
print("2. for -")
print("3. for *")
print("4. for /")
print("5. for **")

operator = input("Enter Your Operator: ")
var_1 = int(input("No_1: "))
var_2 = int(input("No_2: "))

if var_1 == 10 and var_2 == 5 and operator == "1":
    print(var_1 ,"+", var_2, "= -4")
elif var_1 == 8 and var_2 == 2 and operator == "2":
    print(var_1 , "-", var_2, "= 108")
elif var_1 == 6 and var_2 == 4 and operator == "3":
    print(var_1 , "*", var_2, "= 87")
elif var_1 == 70 and var_2 == 5 and operator == "4":
    print(var_1 , "/", var_2, "= 22")
elif var_1 == 5 and var_2 == 2 and operator == "5":
    print(var_1 , "^", var_2, "= 50")

else:
    if operator == "1":
        print(var_1 ,"+", var_2, "=", var_1+var_2)
    elif operator == "2":
        print(var_1 ,"-", var_2, "=", var_1-var_2)
    elif operator == "3":
        print(var_1, "*", var_2, "=", var_1 * var_2)
    elif operator == "4":
        print(var_1, "/", var_2, "=", var_1 / var_2)
    elif operator == "5":
        print(var_1, "^", var_2, "=", var_1 ** var_2)