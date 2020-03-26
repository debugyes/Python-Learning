#for循环操作数组
#格式for 变量名 in 数组名
#python访问数组中的每一个元素，并且将那个元素存储在in前的临时变量中
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + " that was a good trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")	

print("Thank you, everyone. That was a great magic show!")