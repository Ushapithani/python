def reversed_number(num):
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse
    
num=int(input("enter to reverse a number"))
print("reversed number",reversed_number(num))








#return along with zeroes
def reversed_number(num):
    return num[::-1]  


num = input("Enter a number that is return along with zeroes: ")  
print("Reversed number:", reversed_number(num))




#reverse a string
def reverse_string(s):
    return s[: : -1]
string=input("enter string")
print("reversed string", reverse_string(string))







# swap only first and last index  and combine 
def swap(s):
    if len(s)<2:
        return s
    a=list(s)
    a[0] ,  a[-1]=a[-1] , a[0]
    return''.join(a)
string=input("enter anything nuumber or string")
print(" swap only first and last index  and combine",swap(string))





#swap first and last only
def swap_first_last(s):
    if len(s)<2:
        return s
    a=list(s)
    a[0] ,  a[-1]=a[-1] , a[0]
    

    return''.join(a)
string=input("enter anything nuumber or string")
print("#swap first and last only",swap_first_last(string))







    








