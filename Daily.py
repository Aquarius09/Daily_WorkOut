'''
1.
____*  
   * * 
  * * * 
 * * * * 
* * * * * 


def start_fun(num):

   for i in range(num):
        for k in range(1,(num-i)):
           print("",end= " ")
        for j in range(i+1):
            print("*",end= " ")
        print()
num1 = int(input("Enter the number : "))
start_fun(num1)

 
# 2.
# Python Program to Convert Kilometers to Miles
# mi =km * 0.62137
# 

def km_miles(km):
    mi = km * 0.62137
    print("Kilometers to Miles {}".format(mi))

num1 = int(input("Enter the number : "))

km_miles(num1) 

# 3.

                   * * * * * * * * * * 
                    * * * * * * * * * 
                     * * * * * * * * 
                      * * * * * * * 
                       * * * * * * 
                        * * * * * 
                         * * * * 
                          * * * 
                           * * 
                            *

def star_fun(num):
    
    for i in range(num,-1,-1):
        for k in range(num-i):
            print("",end=" ")
        for l in range(i+1):
            print("*",end=" ")
        print()

num = int(input("Enter the number :"))

star_fun(num)

# 4.

    Python Program to Print the Fibonacci sequence with for loop and while loop.

    0,1,1,2,3,5,8,13,.........


# With For_loop : ------->>>
def fibo(num):
    a,b = 0,1
    if num < 0:
        print("Do not enter negtive values") 
    elif num == 0 :
        print(a)
    elif num ==1 :
        print(b)
    else:
        print(a , b ,end= " ")
        for i in range(1,num):
            c = a + b
            a = b
            b = c
            print(c,end= " ")
        print()

num = int(input("Enter the values : "))
fibo(num)

'''
# With While_Loop :------->>
"""
def fibonacci(num):
    
    '''  0,1,1,2,3,5,8,13,.........'''
    set = 1 
    a,b = 0,1
    if num < 0:
        print("inncorrect input")

    elif num == 0:
        print(a)
    elif num == 1:
        print(b) 
    else:
        print(a,b, end= " ")
    while set < num:
        c = a + b
        a = b
        b = c
        set = set + 1
        print(c,end= " ")
            
    print()
num = int(input("Enter the values : "))
fibonacci(num)



# 5.
# Python Program to Swap Two Variables

x = 2
y = 3
temp = x
x = y
y = temp
print('x value is' , x)
print('y value is ', y)

"""