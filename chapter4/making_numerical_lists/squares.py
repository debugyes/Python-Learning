#squares = []
#for values in range(1, 11):
#	square = values**2
#	squares.append(square)

#简洁写法
#	squares.append(values**2)

#比上面还简洁的写法
squares = [value ** 2 for value in range(1, 11)]
print(squares)