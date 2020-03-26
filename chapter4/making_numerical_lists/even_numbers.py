#使用range()函数跳过某些数字
#实际上就是在range的实参中多传一个，改变步长

#生成1-10中的偶数
even_numbers = list(range(2, 11, 2))
print(even_numbers)