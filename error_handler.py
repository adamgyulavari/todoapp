class ErrorHandler(object):
    def handle(self, method, cause):
        if type(cause) is str:
            return self.error(method) + cause
        else:
            return self.error(method) + self.cause(cause)

    def error(self, method):
        return 'Unable to ' + method + ': '

    def cause(self, what):
        if type(what) is TypeError:
            return 'No index is provided'
        if type(what) is IndexError:
            return 'Index is out of bound'
        if type(what) is ValueError:
            return 'Index is not a number'
