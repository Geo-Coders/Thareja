# Write a program that deliberately raises a user-defined SocketError with 
# any number of arguments and derived from class Runtime

class SocketError(RuntimeError):
    def __init__(self, *arg):
        self.args = arg

try:
    raise SocketError('Socket', 'Establishment', 'Error')

except SocketError as e:
    print(e.args)