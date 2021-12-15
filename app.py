import functions

quit = False

print('Welcome to this simulation of a login system! Type h for help')

while quit == False:
    cmd = input('> ')
    if cmd == 'h':
        print('''
        Commands
        h - help
        q - quit
        s - sign up
        l - log in
        w - limitations of this program
        ''')
    elif cmd == 'q':
        print('Bye!')
        exit()
    elif cmd == 's':
        functions.signUp()
    elif cmd == 'l':
        functions.logIn()
    elif cmd == 'w':
        functions.limitations()
    else:
        print('Please enter a valid command!')