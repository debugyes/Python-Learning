# 数组的排序
# 按字母顺序排序的函数有
# 永久性排序
#   数组名.sort()	顺序排序
#   数组名.sort(reverse = True)逆序排序
#
# 暂时性排序
#   sorted(数组名)顺序排序
#   sorted(数组名, reverse = True)逆序排序


# 不按字母逆序排序
# 数组名.reverse()
#   reverse方法并不会按照字母排序，只是简单的逆序排序
#   此方法永久排序，但是第二次调用会回到初始顺序


# sort()方法，永久性排序
# 按照字母表的顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']
print()

# 按照字母表逆序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)  # ['toyota', 'subaru', 'bmw', 'audi']
print(cars)
print()

# sorted()方法，暂时性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here's the original list:")
print(cars)
print("here's the sorted list:")
print(sorted(cars))
print("here's the original list again:")
print(cars)
print("here's the reverse list:")
print(sorted(cars, reverse=True))
print()

# 不按字母顺序逆序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
