"""
1) lambda
2) map
3) filter
4) reduce


To define a function we will use a def keyword

def function_name():
"""
def add():
    num1 = 10
    num2 = 20
    print(num1+num2)
add()

def add(num1,num2):
    print(num1+num2)
add(15,16)


def square(num):
    return num ** 2
print(square(9))


#lambda arg : expession
square = lambda x : x **2
print(square(4))

my_sum = lambda x,y : x+y
print(my_sum(1,2))
'''
def even(x):
    if x % 2 ==0:
        return True
    else:
        False
        '''
even = lambda x: True if x%2!=0 else False
my_list = [1,2,3,4,5,6,7,8,9,10]
#for i in my_list:
    #print(square(i))
print(list(map(square,my_list)))

print(list(filter(even,my_list)))

print(reduce(lambda x,y : x+y , my_list))