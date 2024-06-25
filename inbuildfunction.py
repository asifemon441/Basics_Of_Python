'''
in build function:
    print()
    abs()
    min()
    max()
    sum()
    len()
    id()
    pow()  10**2
    list()
    type()
    range()
    reversed()
    round()
    int()
    float()
    sorted()


print("Hello ")
a = -1.12
print(a)
print(abs(a))
my_list = [ 11, -5, 16, 8,2,1,19, 13]
print(max(my_list))
print(min(my_list))
my_list = [ 11, -5, 16, 8,2,1,19, 13]
print(len(my_list))

name = "Rocky"
print(len(name))
num1 = 11
num2 = 11
num3 = 12
print(id(num1))
print(id(num2))
print(id(num3))

print(pow(num1,2))

numbers = (11, 12, 13)
list_num = list(numbers)
print(type(list_num))
print(type(numbers))
print(list_num)
range(5)
range(1,10)
range(1,10,2)
for i in range(1,10,3):
    print(i)
my_list = [ 11, -5, 16, 8,2,1,19, 13]
for i in reversed(my_list):
    print(i)
'''
my_list = [ 11, -5, 16, 8,2,1,19, 13]
print(sorted(my_list))