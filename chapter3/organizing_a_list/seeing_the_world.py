places = ['tokyo', 'Chongqin', 'LA', 'Las Vegas', 'Canada']
print(places)
print()

sorted(places)
print("The lists is still in its original order:")
print(places)
print()

print(sorted(places, reverse = True))
print("The lists is still in its original order:")
print(places)
print()

places.reverse()
print(places)
places.reverse()
print(places)
print()

places.sort()
print(places)
places.sort(reverse = True)
print(places)
print()