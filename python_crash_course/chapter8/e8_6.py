#8-6
def city_country(city, country):
	return(city+", "+country)
#8-7
def make_album(name, zhuanji, num=0):
    if num == 0:
        return{"name":name, "zhuanji": zhuanji}
    else:
        return{"name":name, "zhuanji": zhuanji, "num":num}
#8-8
def make_album8():
    print("(enter 'q' at any time to quit)")
    name = input("name:")
    if name=="q":
        return {}
    zhuanji = input("zhuanji:")
    if zhuanji=="q":
        return {}
    num = input("num:")
    if num=="q":
        return {}
    return{"name":name, "zhuanji": zhuanji, "num":num}

print("#8-6")
print(city_country("Beijing", "China"))
print(city_country("Shanghai", "China"))
print(city_country(city="New York", country="America"))

print("#8-7")
print(make_album("周杰伦", "东风破"))
print(make_album("田馥甄", "不晚"))
print(make_album("苏慧伦", "鸭子", 1))

print("#8-8")
while True:
    result = make_album8()
    if result:
        print(result)
    else:
        break





