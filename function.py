class Function:
    def __init__(self, expression, executor):
        self.exp = expression 
        self.executor = executor
    def f(self, x):
        return self.executor(x)
    def to_str(self):
        return self.exp