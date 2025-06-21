input_string=input()
reversed_string=""
for i in range(len(reversed_string)-1, -1, -1):
    reversed_string+= input_string[i]
print(reversed_string)