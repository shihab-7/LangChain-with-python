name = "Alvi is running"
# print(name)

str1 = """ alvi is running
fariha is eating 
soumic is sleeping
"""

# print(str1)
# age1 = input("alvi enter your age: ")
# age2 = input("faria enter your age: ")

# str2 = f"alvi is {age1} years old and fariha is {age2} years old"
# print(str2)

# functions i python

# def sum(num1,num2):
#     print(num1+num2)


def sum(num1,num2):
    return num1+num2

x = sum(2,4)
# print(x)
# print(sum(12,12))

# python *args == args=[1,2,3,4.....]
def sum2(*num):
    sum=0
    for i in num:
        sum+=i
    return sum

# print(sum2(1,2,3,3,4,5,5,100,101,1010))

x = lambda x,x1 : x<x1
print(x(2,3))


# name='alvi', age=23, roll=29