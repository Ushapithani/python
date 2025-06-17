def custom_swap(s):
    if len(s) < 2:
        return s  
    
    s_list = list(s)  
    s_list[0], s_list[1] = s_list[1], s_list[0]  
    s_list[0], s_list[-1] = s_list[-1], s_list[0]  
    return ''.join(s_list)  


string = input("Enter a number: ")
print("Modified number:", custom_swap(string))