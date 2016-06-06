from todo import Todo

# Contains all rendering

def usage():
    print('Python Todo application')
    print('=======================')
    print('')
    print('Command line arguments:')
    print(' -l   Lists all the tasks')
    print(' -a   Adds a new task')
    print(' -r   Removes an task')
    print(' -c   Completes an task')

def error(err='Unsupported argument'):
    print(err)
    usage()

def list(todos):
    if len(todos) > 0:
        for i in range(len(todos)):
            print(str(i) + ' - ' + str(todos[i]))
    else:
        print('No todos for today! :)')
