my_dict = {'user1' : 123, 'user2' : 456}
username = input("Enter your user name - ")
password = int(input('Enter your password - '))


def username_password_input():

	global username
	global password
	username = input("Enter your user name - ")
	password = int(input('Enter your password - '))

def username_check():

	global username
	global password

	try:

		if username in my_dict.keys():
			password_check()

		elif username == '':
			raise RuntimeError

		elif username not in my_dict.keys():
			raise KeyError

	except KeyError:
		print('The username is incorrect.Pl., enter the correct username: ')
		username_password_input()
		username_check()
		password_check()

	except RuntimeError:
		print('The username field is empty.Pl., enter the correct username: ')
		username_password_input()
		username_check()
		password_check()


def password_check():
	if password == my_dict[username]:
		print("You are welcome to our site")
	else:
		print('Pl., enter the correct username and password again:')
		username_password_input()

# def password_input():
# 	password = int(input('Enter your password - '))


username_check()




