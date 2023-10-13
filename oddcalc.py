firstnum = input("Give me a number, any number...")
secondnum = input("Okay, give me a another number...")
operation = input("And what operation do you want? (mul/div/mod)")


if operation == "mul": 
    print(firstnum * secondnum)
elif operation == "div": 
    print(firstnum / secondnum)
elif operation == "mod": 
    print(firstnum % secondnum)
else: 
    print("INVALID OPERATION")
        