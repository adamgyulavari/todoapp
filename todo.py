class Todo(object):

    def __init__(self, desc='', checked=False):
        self.desc = desc
        self.checked = checked

    def toggle(self):
        self.checked = not self.checked

    def array(self):
        return [self.desc, str(self.checked)]

    def __str__(self):
        return '[' +  ('x' if self.checked else ' ') + '] ' + self.desc
