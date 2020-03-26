#数组的增加删除
#数组增加元素
#	数组名.append()      在末尾增加一个元素
#	数组名.insert(下标)   在下标处插入一个元素
#	del 数组名[下标]      删除下标处的元素
#	数组名.pop()         删除最后一个元素，但该元素值可以被使用
#	数组名.pop(下标）     删除下标处的元素，该元素可以被使用
#	数组名.remove(元素值) 通过元素值来删除元素


motorcycles = ['honda', 'kawaski', 'suzuki']
print(motorcycles)

#用append方法在数组末尾添加一个元素
motorcycles.append('ducati')
print(motorcycles)

#新建一个空数组，用appen()方法来向其中添加元素
bikes = []
bikes.append('honda')
bikes.append('kawaski')
bikes.append('suzuki')
bikes.append('ducati')
print(bikes)

#用insert方法向数组中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')#在第一个元素位置插入一个元素，将其他元素向后移
print(motorcycles)

#在知道索引的情况下，用del来移除一个元素
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
#不能再访问已经移除的元素！

#用pop()方法来移除数组中最后一个元素，但仍然可以访问这个元素，和del不同，del在删除元素后无法访问
#pop()方法把数组当成一个栈
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
#当pop()方法带索引时，就可以pop任何一个位置的元素
motorcycles4 = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles4.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
#在使用pop()方法后，那个元素就不存在数组里了
#所以，如果要删除一个元素时，若以后不再用那个元素了，就用del；如果还要再用那个元素，就用pop()

#如果不知道要删除的元素下标，只知道要删除元素的值，就只能用remove()方法了
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#移除ducati但用一个变量来保存它，这样以后还能使用这个值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive to me")
#remove只会删除第一个出现的元素