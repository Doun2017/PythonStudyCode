#5-8
print("#5-8")
names = ["admin", "niurou pisa", "haixian pisa", "liulian pisa",'pizza', 'falafel', 'carrot cake']
for item in names:
    if item == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+item+ ", Welcome！")
        

#5-9
print("#5-9")
names.clear()
if names:
    print("not empty")
else:
    print("We need to find some users!")
    
#5-10
print("#5-10")
current_users = ["Admin", "niurou pisa", "haixian pisa", "liulian pisa",'pizza', 'falafel', 'carrot cake']
current_users_lower = []
new_users = ["admin", "niurou piSa", "haixian asd", "liulian fds",'dd', 'falafel', '44 cake']
for name in current_users:
    current_users_lower.append(name.lower())
for new_name in new_users:
    if new_name.lower() in current_users_lower:
        print(new_name + " 存在")
    else:
        print(new_name + " 不存在")
