def cal(num1,num2,way = "+"):
    if way == "+":
        result = num1 + num2
    elif way == "-":
        result = num1 - num2
    elif way == "*":
        result = num1 * num2
    elif way == "/":
        result = num1 / num2
    elif way == "**":
        result = num1 ** num2
    return result


