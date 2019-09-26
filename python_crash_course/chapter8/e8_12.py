#8-12
def make_sanwich(*food):
    print("the sanwich includes：")
    for item in food:
        print(item)
#8-13
def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
#8-13
def build_carinfo(company, type, **car_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    profile = {}
    profile['company'] = company
    profile['type'] = type
    for key, value in car_info.items():
        profile[key] = value
    return profile




print("#8-12")
make_sanwich("boluo pisa", "niurou pisa", "haixian pisa")
make_sanwich("niurou pisa", "haixian pisa")
make_sanwich("haixian pisa")

print("#8-13")
user_profile = build_profile('shi', 'liu',
    location='xinweijiayuan',
    field='software',
    weight=75)
print(user_profile)

print("#8-14")
user_profile = build_carinfo('tongyong', 'lingzhi',
    color='blue', tow_package=True)
print(user_profile)


