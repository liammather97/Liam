def factorial(number):
    count = number
    if number == 0:
        return number
    else:
        for i in range(1,count):
            number *= i
        return number
def reverse_factorial(number):
    count = number
    if number ==0:
        return number
    else:
        while number > 1:
            for i in range(1,(count+1)):
                number /=i
                if number ==1:
                    return i
        return "None"
