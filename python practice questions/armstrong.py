def is_armstrong(num):
    num_str = str(num)  
    num_digits = len(num_str)  
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  

    return sum_of_powers == num  


num = 370
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is NOT an Armstrong number.")








def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

def find_armstrong_in_range(start, end):
    armstrong_numbers = [num for num in range(start, end + 1) if is_armstrong(num)]
    return armstrong_numbers


start = 1
end = 10000  
armstrong_numbers = find_armstrong_in_range(start, end)
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")

