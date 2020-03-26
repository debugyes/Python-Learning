#处理数组中的一小个片段
#格式：数组名[起始索引：终止索引]
#python会在终止索引的前一个位置停下
players = ['charles', 'martina', 'michale', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

#如果忽略了起始索引，python会默认从0索引开始
print(players[:4])

#如果忽略了终止索引，python会从起始索引开始到数组末尾
print(players[2:])

print(players[-3:])

print()
#使用循环遍历部分数组
print("Here're my first three players in my team:")
for player in players[:3]:
	print(player.title())