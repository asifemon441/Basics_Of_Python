"""
Loop statement
    - for
    - while
    for(inti,cond,inc/dec)
    while(cond)
"""
#for i in range(5,15,2):
    #print(i)
my_list = [1,2,3,4,5,6,7,8,9,10]


for each in my_list:
    if each % 2 ==0:
        print(each)
for i in range(len(my_list)):
    print(my_list[i])

print([ each for each in  my_list if each % 2 ==0])


k = 10
while(k>0):
    print(k)
    k-=1