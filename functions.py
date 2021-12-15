def signUp():
    print('Welcome to the Sign Up page! Type "cancel" to go back to the main page.')
    data = open("data.txt", "a+")
    quit = False
    username = ''
    while quit == False:

        # No system to check if username already exists
        username = input('Please create a username: ')
        if len(username) > 20:
            print('Please enter a shorter name!')
        elif len(username) < 3:
            print('Please enter a longer name!')
        else:
            quit = True
    
    quit = False
    pwd = ''
    while quit == False:
        pwd = input('Please create a password: ')
        reCheck = input('Please re-enter the password for confirmation: ')  
        if pwd == reCheck:
            print(f'''
            Successfully created user '{username}' with password '{pwd}'


            ''')
            quit = True
            inFull = f'''{username}:{pwd} \n'''
            data.write(inFull)
            data.close()
        else:
            print('The passwords do not match, please retry!')


def  logIn():
    data = open("data.txt", "a+")
    username = input('Username: ')
    pwd = input('Password: ')

    data.seek(0)

    # username checking
    listOfUsers = data.readlines()
    validUser = False
    userDetails = []
    for i in range(len(listOfUsers)):
        name = listOfUsers[i]
        namePartitioned = name.partition(':')
        if username == namePartitioned[0]:
            validUser = True
            userDetails = namePartitioned
    
    if validUser:
        passwdTemp = userDetails[2]
        passwd = passwdTemp.partition(' ')


        if pwd == passwd[0]:
            print(f'''Successfully logged in to {username}!''')
        else:
            # does not return to re enter password, rather it quits the logIn() function
            print('Incorrect password!')

    else:
        print('Please enter a valid username!')


def limitations():
    print('''
        This program is still incomplete and has a few limitations.
        1. This program does not check if a username has already been taken when registering a new user.
        2. The user interface in this program is not friendly
        3. Passwords are stored in plain text in the data.txt file
        
        I am working on removing these limitations in the next release

    ''')