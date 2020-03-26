current_names = ['katou megumi', 'johhny', 'james', 'mike', 'alex']
new_users = ['katou megumi', 'alex', 'emma', 'ava']

current_names_new = [current_name.title() for current_name in current_names]

for new_user in new_users:
	if new_user.title() in current_names_new:
		print("You need to enter a new name.")
	else:
		print("The username:" + new_user + " is available")