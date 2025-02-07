test = "salam"

def add_numbers(a,b,c):
    print(a+b+c)
    return a+b+c

number1 = add_numbers(15,1,1)  #17
number2 = add_numbers(10,1,1)  #12
number3 = add_numbers(40,1,1)  #42

x = add_numbers(number1,number2,number3)
print(x) #71