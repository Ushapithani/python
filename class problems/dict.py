users = []
n = int(input("Number of users: "))


for i in range(n):
    user = {}
    user['name'] = input("Enter name: ")
    user['id'] = input("Enter id: ")
    users.append(user)

print(users)

keyword = input("Enter keyword: ")
filtered_list = []


for user in users:
    if keyword in user['name'] or keyword in user['id']:
        filtered_list.append(user)

print(filtered_list)