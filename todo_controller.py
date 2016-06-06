import views
from error_handler import ErrorHandler
from io_controller import IoController

class TodoController(object):
    def __init__(self, filebase='todos'):
        self.error_handler = ErrorHandler()
        self.io_controller = IoController(filebase + '.csv')
        try:
            self.todos = self.io_controller.load()
        except FileNotFoundError:
            self.todos = []
            self.save()

    def list(self):
        views.list(self.todos)

    def add(self, desc):
        if desc == None:
            return views.error(self.error_handler.handle('add', 'No task is provided'))
        self.todos.append(Todo(desc))
        self.save()

    def remove(self, i):
        try:
            self.todos.remove(self.todos[int(i)])
            self.save()
        except Exception as e:
            views.error(self.error_handler.handle('remove', e))

    def check(self, i):
        try:
            self.todos[int(i)].toggle()
            self.save()
        except Exception as e:
            views.error(self.error_handler.handle('check', e))

    def save(self):
        self.io_controller.save(self.todos)
