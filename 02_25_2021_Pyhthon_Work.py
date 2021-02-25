# Python program to find the L.C.M. of two input number

import time
lcm_list=([13, 9, 57, 18, 88, 20, 37])

#Solution 1

# This function computes G.C.D 
def lcm_of_list_2(numbers):
    a=sorted(list(set(numbers)), reverse = True)    
    if a==[1]: return [1]
    pf=[]  #Prime Factorization of an Integer    
    for i in a:
        if i>1:
            numbers = i
            k=[]
            for i in range(2,numbers+1):
                while numbers>1:
                    if numbers%i == 0:
                        numbers = numbers /i
                        k.append(i)
                    else:
                        break 
            pf.append(k)   
    pf2=pf[0]
    for i in pf:
        for j in i: 
            if pf2.count(j)< i.count(j): pf2.append(j)
    result=1
    for i in pf2: result = result*i
    return (result)


result=lcm_of_list_2(lcm_list)
print (result)



#Solution  2

def func_lcm_of_list(nums):
    b = max(nums)
    while True:
        if all([b%i==0 for i in nums]):
            break
        else:
            b+=max(nums)
            
    return b

print(func_lcm_of_list(lcm_list))




# Solution 3
# This function computes L.C.M More then two items
def lcm_of_list(numbers):
   lcm_numbers=compute_lcm(numbers[0], numbers[1])
   count_list=len(numbers)
   i=2
   while i <count_list :
       lcm_numbers=compute_lcm(lcm_numbers, numbers[i])
       i+=1
   return lcm_numbers


# This function computes G.C.D
def compute_gcd(a, b):
   while(b):
       a, b = b, a % b
   return a

# This function computes L.C.M
def compute_lcm(a, b):
   lcm = (a*b)//compute_gcd(a,b)
   return lcm


result=lcm_of_list(lcm_list)
print (result)


