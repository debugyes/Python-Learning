invite_lists = ["kobe brant", "desiel", "Paul Walker"]
print("\n")
print(invite_lists[0] + ", welcome to the dinner")
print(invite_lists[1] + ", welcome to the dinner")
print(invite_lists[2] + ", welcome to the dinner")

print("\n")
print("Paul Walker can't come to the dinner")
invite_lists.pop()
invite_lists.append("Henny Ford")
print(invite_lists[0] + ", welcome to the dinner")
print(invite_lists[1] + ", welcome to the dinner")
print(invite_lists[2] + ", welcome to the dinner")

print("\n")
print("I just found a bigger dinner table")
invite_lists.insert(0, "Mike")
invite_lists.insert(2, "Jenny")
invite_lists.append("alex")
print(invite_lists[0] + ", welcome to the dinner")
print(invite_lists[1] + ", welcome to the dinner")
print(invite_lists[2] + ", welcome to the dinner")
print(invite_lists[3] + ", welcome to the dinner")
print(invite_lists[4] + ", welcome to the dinner")
print(invite_lists[5] + ", welcome to the dinner")
print(invite_lists)

print("\n")
print("Sorry guys, I can only invite two guests.")
print("sorry, " + invite_lists.pop() + " I can't invite you to the dinner")
print("sorry, " + invite_lists.pop() + "I can't invite you to the dinner")
print("sorry, " + invite_lists.pop() + "I can't invite you to the dinner")
print("sorry, " + invite_lists.pop() + "I can't invite you to the dinner")
print(invite_lists[0] + " you're still invited")
print(invite_lists[1] + " you're still invited")

del invite_lists[1]
del invite_lists[0]
print(invite_lists)