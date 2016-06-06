import csv
from todo import Todo

class IoController(object):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        todos = []
        with open(self.filename) as f:
            reader = csv.reader(f, delimiter=';')
            for todo in reader:
                todos.append(Todo(todo[0], todo[1]=='True'))
        return todos

    def save(self, todos):
        with open(self.filename, 'w') as f:
            writer = csv.writer(f, delimiter=';')
            for todo in todos:
                writer.writerow(todo.array())
