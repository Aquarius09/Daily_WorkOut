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

'''