#hello wolrd welcome to django
#lowercase , no spl char ,space=>-

def slug_generator(string):
    string = string.lower()
    result = ""  
    for i in range(len(string)):
        if string[i].isalnum():
            result += string[i]
        elif string[i] == " ":
            result += "-"
        else:
            continue
    return result  

title = input("ENTER A TITLE: ")
result = slug_generator(title)
print(result)