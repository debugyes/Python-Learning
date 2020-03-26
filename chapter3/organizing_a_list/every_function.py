contries = ['China', 'Canada', 'United States', 'United Kindom', 'Australia']
print(contries)
contries.append('Roma')
contries.insert(0, 'Australia')

del contries[5]
contries.remove('Canada')
contries.pop()

print(sorted(contries))
print(sorted(contries, reverse = True))
contries.sort()
print(contries)
contries.sort(reverse = True)
print(contries)
contries.reverse()
print(contries)