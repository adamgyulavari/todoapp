import sys
import views
from todo_controller import TodoController

def main():
    todo_controller = TodoController()
    if len(sys.argv) == 1:
        return views.usage()
    elif len(sys.argv) == 2 and command() == '-l':
        return todo_controller.list()
    elif command() == '-a':
        return todo_controller.add(param())
    elif command() == '-r':
        return todo_controller.remove(param())
    elif command() == '-c':
        return todo_controller.check(param())
    else:
        views.error()

def command():
    return sys.argv[1]

def param():
    if len(sys.argv) > 2:
        return sys.argv[2]

main()
