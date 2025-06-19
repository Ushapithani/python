def mail(gmail):
    if '.' in gmail and '@' in gmail:
        return True
    else:
        return False

name = input("Enter a mail: ")
print(mail(name))