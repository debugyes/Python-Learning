#true
cars = 'subaru wrx sti'
print("is car == subaru wrx sti? I predict true")
print(cars == 'subaru wrx sti')

cars = 'audi rs7'
print("is car == audi rs7? I predict true")
print(cars == 'audi rs7')

cars = 'lamborghini huracan'
print("is car == lamborghini huracan? I predict true")
print(cars == 'lamborghini huracan')

cars = 'lamborghini aventador'
print("is car == lamborghini aventador? I predict true")
print(cars == 'lamborghini aventador')

cars = 'mclaren 720s'
print("is car == mclaren 720s? I predict true")
print(cars == 'mclaren 720s')


#false
cars = 'subaru wrx sti'
print("is car == audi rs7? I predict false")
print(cars == 'audi rs7')

cars = 'audi rs7'
print("is car == subaru wrx sti? I predict false")
print(cars == 'subaru wrx sti')

cars = 'lamborghini huracan'
print("is car == lamborghini aventador? I predict false")
print(cars == 'lamborghini aventador')

cars = 'lamborghini aventador'
print("is car == mclaren 720s? I predict false")
print(cars == 'mclaren 720s')

cars = 'mclaren 720s'
print("is car == lamborghini huracan? I predict false")
print(cars == 'lamborghini huracan')
print('\n')



#测试字符串的boolean值
print("string:")
print("katou" == "megumi")
print("katou" == "katou")

#测试lower()函数
print("lower:")
name1 = "KATOU"
name2 = "MEGUMI"
print(name1.lower() == name2.lower())
name1 = "KATOU"
name2 = 'KATOU'
print(name1.lower() == name2.lower())

#测试数字，相等、不相等、大于、大于等于、小于、小于等于
print("numerical:")
print(2 == 2)
print(1 != 2)
print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)

#测试and和or
print("and or:")
print((2 == 2) and (1 == 1))
print((1 == 1) or (2 == 2))

#测试in和not
print("in not:")
names = ['andrew', 'carolina', 'david']
print('andrew' in names)
print('carolina' not in names)