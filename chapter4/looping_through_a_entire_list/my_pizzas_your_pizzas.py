pizzas = ["fruit pizaa", "meat pizza", "beef pizza"]
friend_pizzas = pizzas[:]
pizzas.append("chocolate pizza")
friend_pizzas.append("vegatable pizza")
print("My favourite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favourite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)