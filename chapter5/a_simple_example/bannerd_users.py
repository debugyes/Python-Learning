#测试元素是否在数组中用in
#测试这个元素是否不在数组中用not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a respone if you wish.")
