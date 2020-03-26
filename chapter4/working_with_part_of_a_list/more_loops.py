my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for my_food in my_foods:
	print(my_food)
for friend_food in friend_foods:
	print(friend_food)

my_foods.append('cannoli')
friend_foods.append('ice cream')

for my_food in my_foods:
	print(my_food)
for friend_food in friend_foods:
	print(friend_food)